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
#teste = grafosPalavra('Arquivos/teste.txt',30)

#nltk
from Auxiliar.aux_NLTK import aux_NLTK
#func_NLTK = aux_NLTK('Estamos fazendo o projeto da materia da UFABC de PLN do professor Jesus')

#ppmi
from Auxiliar.aux_PPMI import aux_PPMI
#func_PPMI = aux_PPMI('Arquivos/Base/noticias/')

#naiveBayes
from Auxiliar.NBClassifier import NBClassifier
NBC = NBClassifier('Arquivos/all_datasets-train.txt')
NBC.train()
NBC.test_batch('Arquivos/all_datasets-test.txt')
NBC.test_arquivo('Arquivos/all_datasets-test_twiter.txt')
