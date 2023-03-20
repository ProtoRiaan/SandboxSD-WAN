import json
import requests

vManageIP = 'sandbox-sdwan-2.cisco.com'
username = 'devnetuser'
password = 'RG!_Yw919_83'

baseUrlStr = f'https://{vManageIP}:8443/'

actionLogin = 'j_security_check'
payloadLogin = {'j_username': username, 'j_password': password}

uriLogin = baseUrlStr + actionLogin

print(uriLogin)