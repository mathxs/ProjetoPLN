# -*- coding: utf-8 -*-
#from TwitterAPI import TwitterAPI
import re
import json
import requests

# Informacao base API busca
api_token = 'access_token'
api_url_base = 'https://api.twitter.com/1.1/tweets/search/fullarchive/'

# Headers info
headers = {'Content-Type' : 'application/json',
            'charset' : 'utf-8',
            'Authorization' : 'Bearer {0}'.format(api_token)}

# Params info
params = { 'maxResults' : 100,
            'query' : "(#brumadinho OR #desastre OR #sobreviventes OR #barragem) lang:pt",
            'fromDate' : '201901250000',
            'toDate' : '201901290000',
            'next' : 'next'}

api_url = '{0}projetoPLN.json'.format(api_url_base)

response = requests.get(api_url, headers=headers, params=params)

searchRes = json.loads(response.content.decode('utf-8'))

print(response)
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

# Cria um novo arquivo tweets.txt com codificacao em UTF-8
f = open("tweetsBrumadinho.txt", "a+", encoding="UTF-8")

# Limpa os tweets contendo #, @ e links
# e tambem emoticons
# e caracteres de escape
for name in searchRes['results']:
    emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
    if 'retweeted_status' in name:
        text = name['text']
        m = re.search('RT (.+?):', text)
        if m:
            name['text'] = m.group(1)
        name['text'] = emoji_pattern.sub(r'', name['text'])
        name['text'] = re.sub(r'#\w+|@\w+|https?://\w+.\w+(/?\w?)*|\\\\\w', "", name['text'])
    elif 'extended_tweet' in name:
        name['extended_tweet']['full_text'] = emoji_pattern.sub(r'', name['extended_tweet']['full_text'])
        name['extended_tweet']['full_text'] = re.sub(r'#\w+|@\w+|https?://\w+.\w+(/?\w?)*|\\\\\w', "", name['extended_tweet']['full_text'])

print(searchRes['next'])

# Escreve os tweets para um arquivo txt
# Eliminando os espaços extras nas extremidades
for search in searchRes['results']:
    if 'retweeted_status' in search:
        if search['text']:
            f.write(search['text'].strip() + "\n")
    elif 'extended_tweet' in search and search['extended_tweet']['full_text']:
        f.write(search['extended_tweet']['full_text'].strip() + "\n")

f.close()