#Codigo baseado e utilizando os Scripts da aula 04 do dia 12/06 do projessor Jesus de PLN da UFabc
# coding=utf8
import re

class grafosPalavra:

    def __init__(self,caminho,peso):
        
        regex = r"[-'a-zA-ZÀ-ÖØ-öø-ÿ0-9]+"   # raw string
        fileName = caminho
        weight   = int(peso)

        # leitura das stopwords
        stopwordsfile = open('Arquivos/stopwords.txt','r')
        stopwords       = set([]) 
        for s in stopwordsfile.readlines():
            stopwords.add(s.strip().lower())

        # leitura do documento
        document = open(fileName,'r')
        content  = document.read()  # devolve o conteudo do arquivo
        
        Words    = re.findall(regex, content)
        Edges    = dict([])

        # contando a frequencia dos pares de palavras
        for i in range(0, len(Words)-1):
            if Words[i] not in stopwords and Words[i+1] not in stopwords:
                edge = (Words[i], Words[i+1])
                if edge not in Edges:
                    Edges[edge] = 0
                Edges[edge] += 1

        # criando o grafo direcionado (digraph)
        txtGraph = "\ndigraph{"
        for v in Edges.keys():
            if Edges[v]>=weight:
                txtGraph += '\n "{}" -> "{}"[label="{}"]'. format(v[0], v[1], Edges[v])
        txtGraph += "\n}"

        print(txtGraph)
        print ( "\nQuantidade de palavras: {}".format(len(Words)) )   
        print ( "Quantidade de arestas : {}".format(len(Edges)) )   

