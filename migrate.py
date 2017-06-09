# coding: utf-8

import json
import requests
from datetime import datetime
from requests_oauthlib import OAuth1
from oauth_keys import *


auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
endpoint = "https://api.zaim.net/v1/pay/create.json"

with open('kakeibo.json', 'r') as f:
    print(f)
    data_json = json.load(f)
 
print(data_json)
print(type(data_json))

i = 0

for entry in data_json:
    #print(entry)
    sign = entry["sign"]
    
    if sign == "0":
        print("=" * 50)
        print("category:", entry["c_id"])
        print("sign: ", entry["sign"])
        print("amount: ", entry["amount"])
        print("updated_at: ", entry["updated_at"])
        print("detail:", entry["detail"])

        c_id = entry["c_id"]
        category_id = 101
        genre_id = 10101

        if c_id == "2":
            category_id = 103
            genre_id = 10301
        elif c_id == "3":
            category_id = 108
            genre_id = 10802

        data = {
            "category_id": category_id,
            "genre_id": genre_id,
            "price": entry["amount"],
            "date": entry["updated_at"],
            "comment": entry["detail"],
        }

        r = requests.post(endpoint, data=data, auth=auth)

        i += 1
        #if i == 5:
        #    break
