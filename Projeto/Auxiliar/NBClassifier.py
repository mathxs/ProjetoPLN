# -*- coding: utf-8 -*-
import sys
import re
import math
import re
from nltk import word_tokenize, pos_tag, ne_chunk
regex = r"[-'a-zA-ZÀ-ÖØ-öø-ÿ]+" 
at_nltk = False
class NBClassifier:

    def __init__(self, training_file=None,at_nltk=False):
        self.Data          = []
        self.Classes       = dict([])
        self.V             = set([])
        self.bigdoc        = dict([])
        self.at_nltk = at_nltk

        self.logprior      = dict([])
        self.loglikelihood = dict([])

        if training_file is not None:
            self.load_data(training_file)

    def negate_sequence(self,text):
        text2 = ""
        prefix = ""
        for w in re.findall(r"[-'a-zA-ZÀ-ÖØ-öø-ÿ]+|[.,;!?]", text):
            if w in ["not", "didn't", "no", "não"]:
                prefix = "not_"
                continue
            if w in ".,;!?":
                prefix = ""
            text2 += " "+prefix+w

        return text2

    def load_data(self, training_file):
        training_document = open(training_file,'r')

        for line in training_document.readlines():
            if '\t' in line:
                d, c = tuple(line.strip().split("\t"))
                if self.at_nltk:
                    for j in word_tokenize(d,language='portuguese'):                        
                        d = j
                self.Data.append((c,d))
            #print (d)
            
            if c not in self.Classes:
                self.Classes[c] = 0
                self.bigdoc[c] = []
            self.Classes[c] += 1
           
            # tratando a negação
            d = self.negate_sequence(d)
            for w in re.findall(regex, d):
                self.V.add(w)
                self.bigdoc[c].append(w)

        print("Total: classes={} documentos={} vocabulario={}".format(len(self.Classes), len(self.Data), len(self.V) ) )


    def train(self):
        for c in self.Classes:
            Ndoc = len(self.Data)
            Nc   = self.Classes[c]

            #self.logprior[c] = math.log(Nc/Ndoc)
            self.logprior[c]  = Nc/Ndoc

            count_wc = 0
            for w in self.V:
                count_wc += self.bigdoc[c].count(w)

            for w in self.V:
                #self.loglikelihood[(w,c)] = math.log( (self.bigdoc[c].count(w) + 1) / (count_wc + len(self.V) )  )
                self.loglikelihood[(w,c)]  = (self.bigdoc[c].count(w) + 1) / (count_wc + len(self.V) )  

        print("\n", self.logprior)


    def test_arquivo(self, texto_test):
        quant_linha = 0
        quant_posit = 0
        training_test = open(texto_test,'r')
        for line in training_test.readlines():
            quant_linha += 1
            s = dict([])
            for c in self.Classes.keys():
                s[c] = self.logprior[c]
                for w in re.findall(regex, line):
                    if w in self.V:
                        #s[c] += self.loglikelihood[(w,c)]
                        s[c]  *= self.loglikelihood[(w,c)]
            quant_posit += int(max(s, key=s.get))
        print ("Quantidade de linha: {} \t Quantidade de valores 1: {} \n".format(quant_linha, quant_posit))
        #return max(s, key=s.get)

    def test(self, testdoc):
        s = dict([])
        for c in self.Classes.keys():
            s[c] = self.logprior[c]
            for w in re.findall(regex, testdoc):
                if w in self.V:
                    #s[c] += self.loglikelihood[(w,c)]
                    s[c]  *= self.loglikelihood[(w,c)]

        return max(s, key=s.get)

    def test_batch(self, testing_file):
        testing_document = open(testing_file,'r')
        correct = 0
        total   = 0
        (tp, tn, fp, fn) = (0,0,0,0)

        for line in testing_document.readlines():
            total += 1
            d, c   = tuple(line.strip().split("\t"))
            result = self.test(d.lower())
            #print ("Classe_Verdadeira={} Classe_Identificada={}:\t{}".format(c, result, d))
            if c==result:
                correct += 1
            if c=='1' and result=='1':
                tp += 1
            if c=='0' and result=='1':
                fp += 1
            if c=='1' and result=='0':
                fn += 1
            if c=='0' and result=='0':
                tn += 1

        print ("Corretos={}/{}\tAcurácia={}".format(correct, total, correct/float(total) ))
        print ("Precisão  = {}".format(float(tp)/(tp+fp)))
        print ("Revocação = {}".format(float(tp)/(tp+fn)))