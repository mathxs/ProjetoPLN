# coding=utf8
import sys
import re
import os
import numpy
import math
import matplotlib.pyplot as plt

regex = r"[-'a-zA-ZÀ-ÖØ-öø-ÿ]+" 

M = 300

def hashF(word):
    k = 0
    for i in range(0, len(word)):
        k += (17**i) * ord(word[i])
    return k%M

if __name__ == '__main__':
    dirDB = sys.argv[1]
    
    Document   = dict([])
    Vocabulary = set([])

    # leitura das stopwords
    Stopwords       = set([]) 
    for s in open("stopwords-pt.txt",'r').readlines():
        Stopwords.add(s.strip().lower())

    # leitura dos documentos
    for fileName in os.listdir(dirDB):
        Document[fileName] = []
        document = open(dirDB+"/"+fileName,'r')
        content  = document.read().lower()

        for w in re.findall(regex, content):
            if w not in Stopwords and len(w)>=3:
                Document[fileName].append(w)
        Vocabulary.update( Document[fileName] )


    D = len(Document)
    V = len(Vocabulary)
    S = len(Stopwords)

    # contabilizando os pares de palavras
    k           = 3
    Mcontext    = numpy.ones((V, M))   # colunas: 0 .. M-1
    Vocabulary  = list(Vocabulary)
    iVocabulary = dict([])
    
    for (i,w) in enumerate(Vocabulary):
        iVocabulary[w] = i

    for d in Document.keys():
        print (d)
        for (i,w) in enumerate(Document[d]):
            context = []
            if i>k:
                context += Document[d][i-k:i]
            if i<len(Document[d])-k:
                context += Document[d][i+1:i+k+1]

            iw = iVocabulary[w]
            for wc in context:
                #Mcontext[iw, iVocabulary[wc]] += 1
                Mcontext[iw, hashF(wc) ] += 1


    # Calculando para cada palavra do vocabulario: PPMI
    N    = numpy.sum(Mcontext)
    PPMI = numpy.zeros((V, M))

    Fw   = numpy.sum(Mcontext, axis=1) # somatoria de cada linha
    Fc   = numpy.sum(Mcontext, axis=0) # somatoria de cada coluna

    for i in range(0, V): 
        for j in range(0, M): 
            PPMI[i,j] = max(0, math.log2((Mcontext[i,j]/N)/(Fw[i]/N*Fc[j]/N)) )

    import matplotlib.image as img
    import matplotlib.pyplot as plt
    plt.imshow(Mcontext[:,:], cmap=plt.cm.gray, interpolation='none')
    plt.show()


