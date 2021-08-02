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

token = app_info['creon']['token']

