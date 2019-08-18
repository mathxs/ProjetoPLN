# -*- coding: utf-8 -*-
#Artigo referencia do trabalho de PLN
#https://pdfs.semanticscholar.org/7867/159013a9c10661fbfe8619a9c1cc76c3012c.pdf?_ga=2.107625477.667567004.1564233162-1809408230.1564233162
#
#Instrução do Virtual Env: http://libzx.so/main/learning/2016/03/13/best-practice-for-virtualenv-and-git-repos.html
#https://pt.stackoverflow.com/questions/391796/devo-commitar-meu-virtualenv-no-github

import sys

#informações do compilador
print(sys.version)
print(sys.executable+"\n")

#arquivo de aprendizado
arquivo_train_desastre = 'Arquivos/datasets_brumadinho.txt'
arquivo_train_formal = 'Arquivos/datasets_brumadinho.txt'
#testando acertividade
arquivo_batch = 'Arquivos/datasets_brumadinho.txt'
#arquivo twiter
arquivo_twiter = 'Arquivos/datasets_brumadinho.txt'
#porcentual dos n_grama
n = 0.65

print ("\nInformal é 1 e Formal é 0\nDesastre é 1 e Não Desastre é 0\n")

#O grafico de palavra
from Auxiliar.grafosPalavra import grafosPalavra
from Auxiliar.NBClassifier import NBClassifier

#naiveBayes
print ("\Sem NlTK, NBClassifier\n")

N1_NBC = NBClassifier(arquivo_train_desastre)
N1_NBC.train()
N1_NBC.test_batch(arquivo_batch)
N1_NBC.test_arquivo(arquivo_twiter)

print ("\Sem nltk, Unigrama\n")
N1_grama = grafosPalavra(arquivo_twiter,1,n)

print ("\Sem nltk, Bigrama\n")
N3_grama = grafosPalavra(arquivo_twiter,2,n)

print ("\Sem nltk, Trigrama\n")
N5_grama = grafosPalavra(arquivo_twiter,3,n)

print ("Formal:\n")
arquivo_temp = 'Arquivos/datasets_N1_0.txt'
N1_NBC.test_arquivo_formal(arquivo_train_formal,0,arquivo_temp)
N1_NBC.test_batch(arquivo_temp)
N1_NBC.test_arquivo(arquivo_temp)

print ("\Sem nltk, Unigrama\n")
N1_grama = grafosPalavra(arquivo_temp,1,n)

print ("\Sem nltk, Bigrama\n")
N3_grama = grafosPalavra(arquivo_temp,2,n)

print ("\Sem nltk, Trigrama\n")
N5_grama = grafosPalavra(arquivo_temp,3,n)

print ("Informal:\n")
arquivo_temp = 'Arquivos/datasets_N1_1.txt'
N1_NBC.test_arquivo_formal(arquivo_train_formal,1,arquivo_temp)
N1_NBC.test_batch(arquivo_temp)
N1_NBC.test_arquivo(arquivo_temp)

print ("\Sem nltk, Unigrama\n")
N1_grama = grafosPalavra(arquivo_temp,1,n)

print ("\Sem nltk, Bigrama\n")
N3_grama = grafosPalavra(arquivo_temp,2,n)

print ("\Sem nltk, Trigrama\n")
N5_grama = grafosPalavra(arquivo_temp,3,n)

print ("\Com NlTK,  word_tokenize, NBClassifier\n")

N2_NBC = NBClassifier(arquivo_train_desastre,True)
N2_NBC.train()
N2_NBC.test_batch(arquivo_batch)
N2_NBC.test_arquivo(arquivo_twiter)

print ("\Com NlTK,  word_tokenize, Unigrama\n")
N2_grama = grafosPalavra(arquivo_twiter,1,n,True)

print ("\Com NlTK,  word_tokenize, Bigrama\n")
N4_grama = grafosPalavra(arquivo_twiter,2,n,True)

print ("\Com NlTK,  word_tokenize, Trigrama\n")
N6_grama = grafosPalavra(arquivo_twiter,3,n,True)

print ("Formal:\n")
arquivo_temp = 'Arquivos/datasets_N2_0.txt'
N2_NBC.test_arquivo_formal(arquivo_train_formal,0,arquivo_temp)
N2_NBC.test_batch(arquivo_temp)
N2_NBC.test_arquivo(arquivo_temp)

print ("\Com NlTK,  word_tokenize, Unigrama\n")
N2_grama = grafosPalavra(arquivo_temp,1,n,True)

print ("\Com NlTK,  word_tokenize, Bigrama\n")
N4_grama = grafosPalavra(arquivo_temp,2,n,True)

print ("\Com NlTK,  word_tokenize, Trigrama\n")
N6_grama = grafosPalavra(arquivo_temp,3,n,True)

print ("Informal:\n")
arquivo_temp = 'Arquivos/datasets_N2_1.txt'
N2_NBC.test_arquivo_formal(arquivo_train_formal,1,arquivo_temp)
N2_NBC.test_batch(arquivo_temp)
N2_NBC.test_arquivo(arquivo_temp)

print ("\Com NlTK,  word_tokenize, Unigrama\n")
N2_grama = grafosPalavra(arquivo_temp,1,n,True)

print ("\Com NlTK,  word_tokenize, Bigrama\n")
N4_grama = grafosPalavra(arquivo_temp,2,n,True)

print ("\Com NlTK,  word_tokenize, Trigrama\n")
N6_grama = grafosPalavra(arquivo_temp,3,n,True)

#nltk
#from Auxiliar.aux_NLTK import aux_NLTK
#func_NLTK = aux_NLTK('Estamos fazendo o projeto da materia da UFABC de PLN do professor Jesus')

#ppmi
#from Auxiliar.aux_PPMI import aux_PPMI
#func_PPMI = aux_PPMI('Arquivos/Base/noticias/')

