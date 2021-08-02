# AutoConnect.py

import os
import json

app_info = os.getenv('App_info')
with open(app_info, 'r') as f:
    app_info = json.load(f)

id = app_info['creon']['login']['id']
pwd = app_info['creon']['login']['pwd']
pwdcert = app_info['creon']['login']['pwdcert']

# AutoTrade.py

import os
import json

app_info = os.getenv('App_info')
with open(app_info, 'r') as f:
    app_info = json.load(f)

t = app_info['creon']['token'].encode('utf-8').decode('utf-8')
token = f'"{t}"'

# json 파일 생성
import json

json_data = {

    'creon' :
            {'token' : "##",
            'login' : {'id' :'##',
                       'pwd' : '##',
                       'pwdcert' : '##'}}
            }


with open('C:/stockauto/secret/App_info.json', 'w', encoding='utf-8') as make_file:

    json.dump(json_data, make_file, indent='\t')