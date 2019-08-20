# -*- coding: utf-8 -*-
#from TwitterAPI import TwitterAPI
import re
import json
import requests

# Informacao base API busca
api_token = 'AAAAAAAAAAAAAAAAAAAAADJ8%2FQAAAAAAY89JBq12pO0gTaAsPdJqMLLHEz4%3D1ckFxCKMFXLcvGcJDvyXY73whShU01odZntRSNMw8JDaKZPIss'
api_url_base = 'https://api.twitter.com/1.1/search/'

# Headers info
headers = {'Content-Type' : 'application/json',
            'Authorization' : 'Bearer {0}'.format(api_token)}

# Params info
params = {'lang' : 'pt',
            'include_entities' : True,
            'count' : 10,
            'q' : "%23brumadinho OR %23desastre OR %23sobreviventes OR %23barragem",
            'tweet_mode' : 'extended'}

api_url = '{0}tweets.json'.format(api_url_base)

response = requests.get(api_url, headers=headers, params=params)

searchRes = json.loads(response.content.decode('utf-8'))

# Autenticando no conjunto de API do twitter utilizando Tweepy
# consumer_key = "x5u9rCVgbFHZllSqSAuJgNuTv"
# consumer_secret = "q6mYHBSROEpQdHaeFayOpp2Nf9Y2MwvIjXWabKo8UOMAUx36vq"
# key = "1156898520030470144-dnFJuLoY5bk6xGQBwH9behG2QoRUnu"
# secret = "zDVR3WOKfFWeBR2bFPbM989OGPevyywHGmJRquKg9MnfB"
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(key, secret)

# Chamando a API de busca com os parâmetros abaixo
# api = tweepy.API(auth) 
# query = "%23brumadinho OR %23desastre OR %23sobreviventes OR %23barragem"
# max_tweets = 10
# lang = "pt"
# searchRes = api.search(q=query, lang=lang, count=max_tweets, include_entities=True, tweet_mode="extended")

# Cria um novo arquivo tweets.txt com codificacao em UTF-8
f = open("tweets.txt", "w+", encoding="UTF-8")

# Limpa os tweets contendo #, @ e links
# e tambem emoticons
# e caracteres de escape
for name in searchRes['statuses']:
    if 'retweeted_status' in name:
        text = name['full_text']
        m = re.search('RT (.+?):', text)
        if m:
            name['full_text'] = m.group(1)
    emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
    name['full_text'] = emoji_pattern.sub(r'', name['full_text'])
    print(re.search(r'https?://\w+.\w+(/?\w?)*', name['full_text']))
    name['full_text'] = re.sub(r'#\w+|@\w+|https?://\w+.\w+(/?\w?)*|[^a-zA-Z ]+', "", name['full_text'])

# Escreve os tweets para um arquivo txt
# Eliminando os espaços extras nas extremidades
for search in searchRes['statuses']:
    if search['full_text']:
        f.write(search['full_text'].strip() + "\n")

f.close()