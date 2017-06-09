# coding: utf-8

import json


with open('kakeibo.json', 'r') as f:
    print(f)
    data_json = json.load(f)
 
print(data_json)
print(type(data_json))

for entry in data_json:
    print(entry)