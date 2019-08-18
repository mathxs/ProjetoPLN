# -*- coding: utf-8 -*-
#Codigo baseado e utilizando os Scripts da aula 04 do dia 12/06 do projessor Jesus de PLN da UFabc
# coding=utf8
import re
from nltk import word_tokenize, pos_tag, ne_chunk

at_nltk = False
class grafosPalavra:

    def __init__(self,caminho,n_grama,at_nltk=False):
        
        regex = r"[-'a-zA-ZÀ-ÖØ-öø-ÿ0-9]+"   # raw string
        fileName = caminho
        self.at_nltk = at_nltk
        # leitura das stopwords
        stopwordsfile = open('Arquivos/stopwords.txt','r')
        stopwords       = set([]) 
        for s in stopwordsfile.readlines():
            stopwords.add(s.strip().lower())

        # leitura do documento
        document = open(fileName,'r')
        content  = document.read()  # devolve o conteudo do arquivo
        
        #transformando o arquivo no n_grama requisitado
        Temp_Words = re.findall(regex, content.lower())
        Temp_frase = list([])
        for i in Temp_Words:
            if i not in stopwords:
                if self.at_nltk:
                    for j in word_tokenize(i):                        
                        Temp_frase.append(j)
                        #testando = j
                        #if testando != i:
                            #print ("Diferenca {} {}".format(i,j))
                else:
                    Temp_frase.append(i)            

        Words = list([])
        for i in range(-n_grama, len(Temp_frase)):
            Temp_grama = ""
            for j in range(i, i + n_grama):
                if j >= len(Temp_frase) or j < 0:
                    Temp_grama += " "
                elif Temp_grama != "":
                    Temp_grama += " " + Temp_frase[j]
                else:
                    Temp_grama += Temp_frase[j]
            #print(Temp_grama)
            Words.append(Temp_grama)
        Edges    = dict([])

        # contando a frequencia dos pares de palavras
        for i in range(0, len(Words)-1):
            #if Words[i] not in stopwords and Words[i+1] not in stopwords:
            #print ("Primeira palavra {} Segunda Palavra {}".format(Words[i],Words[i+1]))
            edge = (Words[i], Words[i+1])
            if edge not in Edges:
                Edges[edge] = 0
            Edges[edge] += 1

        #pegando o maior peso * 0.8
        weight = 0
        for v in Edges.keys():
            #print (Edges[v])
            if Edges[v]>weight:
                weight = Edges[v]

        weight = weight * 0.50
        # criando o grafo direcionado (digraph)
        txtGraph = "\ndigraph{"
        for v in Edges.keys():
            if Edges[v]>=weight:
                txtGraph += '\n "{}" -> "{}"[label="{}"]'. format(v[0], v[1], Edges[v])
        txtGraph += "\n}"

        print(txtGraph)
        print("Colocar a saída acima no site: http://graphs.grevian.org/graph/")
        print ( "\nQuantidade de palavras: {}".format(len(Words)) )   
        print ( "Quantidade de arestas : {} \n".format(len(Edges)) )   

