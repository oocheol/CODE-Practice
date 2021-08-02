from pywinauto import application
import time
import os
import json

app_info_file = os.getenv('App_info')
with open(app_info_file, 'r') as f:
    app_info = json.load(f)

id = app_info['creon']['login']['id']
pwd = app_info['creon']['login']['pwd']
pwdcert = app_info['creon']['login']['pwdcert']


os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
os.system('wmic process where "name like \'%DibServer%\'" call terminate')
time.sleep(5)        

app = application.Application()
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp /id:{} /pwd:{} /pwdcert:{} /autostart'.format(id,pwd,pwdcert)) #로그인 아이디/비밀번호/공인인증서비밀번호
time.sleep(60)