import os
import json


def openjson(filename):
    total = []
    with open("./static/json/" + filename, 'r', encoding='utf-8') as f:
        temp = json.loads(f.read())
    return temp


#
# a = openjson("hmq_position.json")
# for key in a.items():
#     print(key[1]['position_id'])
#     print(key[1]['position_name'])
#     a = key[1]['monster_number']
#     print(a)
#     for i in range(0, a):
#         print(key[1]['monster_name'][i])
