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
arquivo_train_desastre = 'Arquivos/datasets_desastres.txt'
arquivo_train_formal = 'Arquivos/datasets_pessoal.txt'
#testando acertividade
arquivo_batch = 'Arquivos/datasets_testaEficiencia.txt'

#Processamento 1º

#arquivo twiter
arquivo_twiter = 'Arquivos/data_twiter_brumadinho.txt'
#porcentual dos n_grama
n = 0.65

print ("\nPessoal é 1 e Objetivo é 0\nDesastre é 1 e Não Desastre é 0\n")

#O grafico de palavra
from Auxiliar.grafosPalavra import grafosPalavra
from Auxiliar.NBClassifier import NBClassifier

#naiveBayes
print ("----------------------------------------------------------------------------------")
print ("\nCompleto:" + arquivo_twiter + "\n")

print ("Sem NlTK, NBClassifier")

N1_NBC = NBClassifier(arquivo_train_desastre)
N1_NBC.train()
N1_NBC.test_batch(arquivo_batch)
N1_NBC.test_arquivo(arquivo_twiter)

print ("Sem nltk, Unigrama")
N1_grama = grafosPalavra(arquivo_twiter,1,n)
N1_NBC.test_grafh(N1_grama.resultado(),arquivo_train_desastre)
#print(N1_grama.resultado())

print ("Sem nltk, Bigrama")
N3_grama = grafosPalavra(arquivo_twiter,2,n)
N1_NBC.test_grafh(N3_grama.resultado(),arquivo_train_desastre)

#print ("Sem nltk, Trigrama")
#N5_grama = grafosPalavra(arquivo_twiter,3,n)
#N1_NBC.test_grafh(N5_grama.resultado(),arquivo_train_desastre)

print ("Com NlTK,  word_tokenize, NBClassifier")

N2_NBC = NBClassifier(arquivo_train_desastre,True)
N2_NBC.train()
N2_NBC.test_batch(arquivo_batch)
N2_NBC.test_arquivo(arquivo_twiter)

print ("Com NlTK,  word_tokenize, Unigrama")
N2_grama = grafosPalavra(arquivo_twiter,1,n,True)
N2_NBC.test_grafh(N2_grama.resultado(),arquivo_train_desastre)

print ("Com NlTK,  word_tokenize, Bigrama")
N4_grama = grafosPalavra(arquivo_twiter,2,n,True)
N2_NBC.test_grafh(N4_grama.resultado(),arquivo_train_desastre)

#print ("\Com NlTK,  word_tokenize, Trigrama\n")
#N6_grama = grafosPalavra(arquivo_twiter,3,n,True)
#N2_NBC.test_grafh(N6_grama.resultado(),arquivo_train_desastre)

print ("----------------------------------------------------------------------------------")
print ("\nFormal:" + arquivo_twiter + "\n")
arquivo_temp = 'Arquivos/Automatico/datasets_N1_0.txt'
N1_NBC.test_arquivo_formal(arquivo_train_formal,0,arquivo_temp)
N1_NBC.test_batch(arquivo_temp)
N1_NBC.test_arquivo(arquivo_temp)

print ("Sem nltk, Unigrama")
N1_grama = grafosPalavra(arquivo_temp,1,n)
N1_NBC.test_grafh(N1_grama.resultado(),arquivo_train_desastre)

print ("Sem nltk, Bigrama")
N3_grama = grafosPalavra(arquivo_temp,2,n)
N1_NBC.test_grafh(N3_grama.resultado(),arquivo_train_desastre)

#print ("\Sem nltk, Trigrama\n")
#N5_grama = grafosPalavra(arquivo_temp,3,n)
#N1_NBC.test_grafh(N5_grama.resultado(),arquivo_train_desastre)

arquivo_temp = 'Arquivos/Automatico/datasets_N2_0.txt'
N2_NBC.test_arquivo_formal(arquivo_train_formal,0,arquivo_temp)
N2_NBC.test_batch(arquivo_temp)
N2_NBC.test_arquivo(arquivo_temp)

print ("Com NlTK,  word_tokenize, Unigrama")
N2_grama = grafosPalavra(arquivo_temp,1,n,True)
N2_NBC.test_grafh(N2_grama.resultado(),arquivo_train_desastre)

print ("Com NlTK,  word_tokenize, Bigrama")
N4_grama = grafosPalavra(arquivo_temp,2,n,True)
N2_NBC.test_grafh(N4_grama.resultado(),arquivo_train_desastre)

#print ("Com NlTK,  word_tokenize, Trigrama")
#N6_grama = grafosPalavra(arquivo_temp,3,n,True)
#N2_NBC.test_grafh(N6_grama.resultado(),arquivo_train_desastre)

print ("----------------------------------------------------------------------------------")
print ("\nInformal:" + arquivo_twiter + "\n")
arquivo_temp = 'Arquivos/Automatico/datasets_N1_1.txt'
N1_NBC.test_arquivo_formal(arquivo_train_formal,1,arquivo_temp)
N1_NBC.test_batch(arquivo_temp)
N1_NBC.test_arquivo(arquivo_temp)

print ("Sem nltk, Unigrama")
N1_grama = grafosPalavra(arquivo_temp,1,n)
N1_NBC.test_grafh(N1_grama.resultado(),arquivo_train_desastre)

print ("Sem nltk, Bigrama")
N3_grama = grafosPalavra(arquivo_temp,2,n)
N1_NBC.test_grafh(N3_grama.resultado(),arquivo_train_desastre)

#print ("Sem nltk, Trigrama")
#N5_grama = grafosPalavra(arquivo_temp,3,n)
#N1_NBC.test_grafh(N5_grama.resultado(),arquivo_train_desastre)

arquivo_temp = 'Arquivos/Automatico/datasets_N2_1.txt'
N2_NBC.test_arquivo_formal(arquivo_train_formal,1,arquivo_temp)
N2_NBC.test_batch(arquivo_temp)
N2_NBC.test_arquivo(arquivo_temp)

print ("Com NlTK,  word_tokenize, Unigrama")
N2_grama = grafosPalavra(arquivo_temp,1,n,True)
N2_NBC.test_grafh(N2_grama.resultado(),arquivo_train_desastre)

print ("\Com NlTK,  word_tokenize, Bigrama")
N4_grama = grafosPalavra(arquivo_temp,2,n,True)
N2_NBC.test_grafh(N4_grama.resultado(),arquivo_train_desastre)

#print ("Com NlTK,  word_tokenize, Trigrama")
#N6_grama = grafosPalavra(arquivo_temp,3,n,True)
#N2_NBC.test_grafh(N6_grama.resultado(),arquivo_train_desastre)


#Processamento 2º
print ("----------------------------------------------------------------------------------")
print ("----------------------------------------------------------------------------------")
print ("----------------------------------------------------------------------------------")

#arquivo twiter
arquivo_twiter = 'Arquivos/data_twiter_predio.txt'
#porcentual dos n_grama
n = 0.65

print ("\nPessoal é 1 e Objetivo é 0\nDesastre é 1 e Não Desastre é 0\n")

#O grafico de palavra
from Auxiliar.grafosPalavra import grafosPalavra
from Auxiliar.NBClassifier import NBClassifier

#naiveBayes
print ("----------------------------------------------------------------------------------")
print ("\nCompleto:" + arquivo_twiter + "\n")

print ("Sem NlTK, NBClassifier")

N1_NBC = NBClassifier(arquivo_train_desastre)
N1_NBC.train()
N1_NBC.test_batch(arquivo_batch)
N1_NBC.test_arquivo(arquivo_twiter)

print ("Sem nltk, Unigrama")
N1_grama = grafosPalavra(arquivo_twiter,1,n)
N1_NBC.test_grafh(N1_grama.resultado(),arquivo_train_desastre)
#print(N1_grama.resultado())

print ("Sem nltk, Bigrama")
N3_grama = grafosPalavra(arquivo_twiter,2,n)
N1_NBC.test_grafh(N3_grama.resultado(),arquivo_train_desastre)

#print ("Sem nltk, Trigrama")
#N5_grama = grafosPalavra(arquivo_twiter,3,n)
#N1_NBC.test_grafh(N5_grama.resultado(),arquivo_train_desastre)

print ("Com NlTK,  word_tokenize, NBClassifier")

N2_NBC = NBClassifier(arquivo_train_desastre,True)
N2_NBC.train()
N2_NBC.test_batch(arquivo_batch)
N2_NBC.test_arquivo(arquivo_twiter)

print ("Com NlTK,  word_tokenize, Unigrama")
N2_grama = grafosPalavra(arquivo_twiter,1,n,True)
N2_NBC.test_grafh(N2_grama.resultado(),arquivo_train_desastre)

print ("Com NlTK,  word_tokenize, Bigrama")
N4_grama = grafosPalavra(arquivo_twiter,2,n,True)
N2_NBC.test_grafh(N4_grama.resultado(),arquivo_train_desastre)

#print ("\Com NlTK,  word_tokenize, Trigrama\n")
#N6_grama = grafosPalavra(arquivo_twiter,3,n,True)
#N2_NBC.test_grafh(N6_grama.resultado(),arquivo_train_desastre)

print ("----------------------------------------------------------------------------------")
print ("\nFormal:" + arquivo_twiter + "\n")
arquivo_temp = 'Arquivos/Automatico/datasets_N1_0.txt'
N1_NBC.test_arquivo_formal(arquivo_train_formal,0,arquivo_temp)
N1_NBC.test_batch(arquivo_temp)
N1_NBC.test_arquivo(arquivo_temp)

print ("Sem nltk, Unigrama")
N1_grama = grafosPalavra(arquivo_temp,1,n)
N1_NBC.test_grafh(N1_grama.resultado(),arquivo_train_desastre)

print ("Sem nltk, Bigrama")
N3_grama = grafosPalavra(arquivo_temp,2,n)
N1_NBC.test_grafh(N3_grama.resultado(),arquivo_train_desastre)

#print ("\Sem nltk, Trigrama\n")
#N5_grama = grafosPalavra(arquivo_temp,3,n)
#N1_NBC.test_grafh(N5_grama.resultado(),arquivo_train_desastre)

arquivo_temp = 'Arquivos/Automatico/datasets_N2_0.txt'
N2_NBC.test_arquivo_formal(arquivo_train_formal,0,arquivo_temp)
N2_NBC.test_batch(arquivo_temp)
N2_NBC.test_arquivo(arquivo_temp)

print ("Com NlTK,  word_tokenize, Unigrama")
N2_grama = grafosPalavra(arquivo_temp,1,n,True)
N2_NBC.test_grafh(N2_grama.resultado(),arquivo_train_desastre)

print ("Com NlTK,  word_tokenize, Bigrama")
N4_grama = grafosPalavra(arquivo_temp,2,n,True)
N2_NBC.test_grafh(N4_grama.resultado(),arquivo_train_desastre)

#print ("Com NlTK,  word_tokenize, Trigrama")
#N6_grama = grafosPalavra(arquivo_temp,3,n,True)
#N2_NBC.test_grafh(N6_grama.resultado(),arquivo_train_desastre)

print ("----------------------------------------------------------------------------------")
print ("\nInformal:" + arquivo_twiter + "\n")
arquivo_temp = 'Arquivos/Automatico/datasets_N1_1.txt'
N1_NBC.test_arquivo_formal(arquivo_train_formal,1,arquivo_temp)
N1_NBC.test_batch(arquivo_temp)
N1_NBC.test_arquivo(arquivo_temp)

print ("Sem nltk, Unigrama")
N1_grama = grafosPalavra(arquivo_temp,1,n)
N1_NBC.test_grafh(N1_grama.resultado(),arquivo_train_desastre)

print ("Sem nltk, Bigrama")
N3_grama = grafosPalavra(arquivo_temp,2,n)
N1_NBC.test_grafh(N3_grama.resultado(),arquivo_train_desastre)

#print ("Sem nltk, Trigrama")
#N5_grama = grafosPalavra(arquivo_temp,3,n)
#N1_NBC.test_grafh(N5_grama.resultado(),arquivo_train_desastre)

arquivo_temp = 'Arquivos/Automatico/datasets_N2_1.txt'
N2_NBC.test_arquivo_formal(arquivo_train_formal,1,arquivo_temp)
N2_NBC.test_batch(arquivo_temp)
N2_NBC.test_arquivo(arquivo_temp)

print ("Com NlTK,  word_tokenize, Unigrama")
N2_grama = grafosPalavra(arquivo_temp,1,n,True)
N2_NBC.test_grafh(N2_grama.resultado(),arquivo_train_desastre)

print ("\Com NlTK,  word_tokenize, Bigrama")
N4_grama = grafosPalavra(arquivo_temp,2,n,True)
N2_NBC.test_grafh(N4_grama.resultado(),arquivo_train_desastre)

#print ("Com NlTK,  word_tokenize, Trigrama")
#N6_grama = grafosPalavra(arquivo_temp,3,n,True)
#N2_NBC.test_grafh(N6_grama.resultado(),arquivo_train_desastre)



