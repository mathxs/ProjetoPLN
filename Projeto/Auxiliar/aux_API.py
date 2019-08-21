# -*- coding: utf-8 -*-
#from TwitterAPI import TwitterAPI
import re
import json
#import requests
import glob

# Informacao base API busca
# api_token = 'acces_token'
# api_url_base = 'https://api.twitter.com/1.1/tweets/search/fullarchive/' # fullarchive
# api_url_base = 'https://api.twitter.com/1.1/tweets/search/30day/' # 30days

# Headers info
#headers = {'Content-Type' : 'application/json',
#            'charset' : 'utf-8',
#            'Authorization' : 'Bearer {0}'.format(api_token)}

# Params info. For GET method
# params = { 'maxResults' : 100,
#             'query' : "(#brumadinho OR #desastre OR #sobreviventes OR #barragem) lang:pt",
#             'fromDate' : '201901250000',
#             'toDate' : '201901290000',
#             'next' : 'next'}

# Json body for search POST method
#data ='{ "query": "(#chapecoense OR #voo OR #queda OR #forçachape OR #sobreviventes) lang:pt", "maxResults": "100", "fromDate": "201611290000", "toDate": "201611300000", "next": "eyJhdXRoZW50aWNpdHkiOiI2NzQzZGMwMjA2M2MyMzc1NzQ2MjYxYmFjYmVmOGQ4MWY1MTM3YTZiMTIwMGIxZTI2MDM1NDVmNzNjZjQ0YTM3IiwiZnJvbURhdGUiOiIyMDE2MTEyOTAwMDAiLCJ0b0RhdGUiOiIyMDE2MTEzMDAwMDAiLCJuZXh0IjoiMjAxNjExMzAwMDAwMDAtODAzNzQ3MjE2MTU4NTc2NjQxLTAifQ=="}'

#api_url = '{0}projetoPLN.json'.format(api_url_base)

path = "../../../TwitterResponse/*.json"

files = glob.glob(path)

#criando uma lista auxiliar
tweets = []

for name in files:
    with open(name, "r", encoding="UTF-8") as f:
        data = json.load(f)
        for search in data['results']:
            emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
            if 'retweeted_status' in search:
                text = search['text']
                m = re.search('RT (.+?):', text)
                if m:
                    m = m.group(1)
                m = emoji_pattern.sub(r'', m)
                tweets.append(re.sub(r'#\w+|@\w+|https?://\w+.\w+(/?\w?)*|\\\\\w', "", m))
            elif 'extended_tweet' in search:
                text = search['extended_tweet']['full_text']
                text = emoji_pattern.sub(r'', text)
                tweets.append(re.sub(r'#\w+|@\w+|https?://\w+.\w+(/?\w?)*|\\\\\w', "", text))
            else:
                text = search['text']
                text = emoji_pattern.sub(r'', text)
                tweets.append(re.sub(r'#\w+|@\w+|https?://\w+.\w+(/?\w?)*|\\\\\w', "", text))
        f.close()

#response = requests.post(api_url, headers=headers, data=data)

#searchRes = json.loads(response.content.decode('utf-8'))

#print(response)
#print(searchRes)

# Autenticando no conjunto de API do twitter utilizando Tweepy
# consumer_key = "consum_key"
# consumer_secret = "consum_secret"
# key = "key"
# secret = "secret"
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(key, secret)

# Chamando a API de busca com os parâmetros abaixo
# api = tweepy.API(auth) 
# query = "%23brumadinho OR %23desastre OR %23sobreviventes OR %23barragem"
# max_tweets = 10
# lang = "pt"
# searchRes = api.search(q=query, lang=lang, count=max_tweets, include_entities=True, tweet_mode="extended")

# Escreve no arquivos tweetsChapecoense.txt com codificacao em UTF-8
fi = open("tweetsChapecoense.txt", "a+", encoding="UTF-8")

# Limpa os tweets contendo #, @ e links
# e tambem emoticons
# e caracteres de escape

#print(searchRes['next'])

# Escreve os tweets para um arquivo txt
# Eliminando os espaços extras nas extremidades

for tweet in tweets:
    if tweet.strip():
        fi.write(tweet.strip() + "\n")

fi.close()