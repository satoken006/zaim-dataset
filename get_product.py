# coding: utf-8

import json
import requests
from requests_oauthlib import OAuth1
from oauth_keys import *


auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
endpoint = "https://api.zaim.net/v2/home/money"

r = requests.get(endpoint, auth=auth)
data = json.loads(r.text)

purchases = data["money"]
for purchase in purchases:
    category_id = purchase["category_id"]
    name = str(purchase["name"])
    comment = str(purchase["comment"])

    if len(comment) >= 0 and category_id == 108:
        print(category_id, name, "コメント: "+ comment)