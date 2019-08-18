#Artigo referencia do trabalho de PLN
#https://pdfs.semanticscholar.org/7867/159013a9c10661fbfe8619a9c1cc76c3012c.pdf?_ga=2.107625477.667567004.1564233162-1809408230.1564233162
#
#Instrução do Virtual Env: http://libzx.so/main/learning/2016/03/13/best-practice-for-virtualenv-and-git-repos.html
#https://pt.stackoverflow.com/questions/391796/devo-commitar-meu-virtualenv-no-github

import sys

#informações do compilador
print(sys.version)
print(sys.executable+"\n")

#O grafico de palavra
from Auxiliar.grafosPalavra import grafosPalavra
print ("\Sem nltk, Unigrama\n")
N1_grama = grafosPalavra('Arquivos/data_twiter_brumadinho.txt',1,0.65)

print ("\Com NlTK,  word_tokenize, Unigrama\n")
N2_grama = grafosPalavra('Arquivos/data_twiter_brumadinho.txt',1,0.70,True)

print ("\Sem nltk, Bigrama\n")
N3_grama = grafosPalavra('Arquivos/data_twiter_brumadinho.txt',2,0.70)

print ("\Com NlTK,  word_tokenize, Bigrama\n")
N4_grama = grafosPalavra('Arquivos/data_twiter_brumadinho.txt',2,0.70,True)

print ("\Sem nltk, Trigrama\n")
N5_grama = grafosPalavra('Arquivos/data_twiter_brumadinho.txt',3,0.70)

print ("\Com NlTK,  word_tokenize, Trigrama\n")
N6_grama = grafosPalavra('Arquivos/data_twiter_brumadinho.txt',3,0.70,True)

#naiveBayes
print ("\Sem NlTK, NBClassifier\n")

from Auxiliar.NBClassifier import NBClassifier
N1_NBC = NBClassifier('Arquivos/datasets_brumadinho.txt')
N1_NBC.train()
N1_NBC.test_batch('Arquivos/datasets_brumadinho.txt')
N1_NBC.test_arquivo('Arquivos/datasets_brumadinho.txt')

print ("\Com NlTK,  word_tokenize, NBClassifier\n")

N2_NBC = NBClassifier('Arquivos/datasets_brumadinho.txt',True)
N2_NBC.train()
N2_NBC.test_batch('Arquivos/datasets_brumadinho.txt')
N2_NBC.test_arquivo('Arquivos/datasets_brumadinho.txt')

#nltk
#from Auxiliar.aux_NLTK import aux_NLTK
#func_NLTK = aux_NLTK('Estamos fazendo o projeto da materia da UFABC de PLN do professor Jesus')

#ppmi
#from Auxiliar.aux_PPMI import aux_PPMI
#func_PPMI = aux_PPMI('Arquivos/Base/noticias/')