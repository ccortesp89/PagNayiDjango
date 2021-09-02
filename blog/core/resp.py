from django.http import request
from django.shortcuts import render
from .models import entrevista
import requests
import json

def go():    

    url = "https://login.salesforce.com/services/oauth2/token"

    payload={'client_id': '3MVG9cHH2bfKACZY.gnl_D.GBQynrdI2tQh7_bmW4T4mKn7NweZk.UY.4VKXfA2S3qqy1QvMDyLtODFtGnVpe',
    'grant_type': 'password',
    'client_secret': 'DBA8ABC92081FCB75786C50325673A24874D4A46A89A9B716D62992FDFF1218E',
    'username': 'ccortedpalma@wise-bear-smx2er.com',
    'password': '314159265.NcrzSw2pgFkYuZwvoNGLAKMjPo'}
    files=[

    ]
    headers = {
        #'Cookie': 'BrowserId=W7VZ_QRIEeuNf4VeKfQx0A; CookieConsentPolicy=0:0'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    
    
    x = response.text
    y = json.loads(x)
    # print(y["access_token"])
    return y["access_token"]

def env(foto):

    token = go()
    u = foto
    url = "https://wise-bear-smx2er-dev-ed.my.salesforce.com/services/apexrest/create"

    payload=json.dumps({
        "url": u
    })
    files=[

    ]
    headers = {
        'Authorization': 'Bearer '+token
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    #print(response.text)
    x = response.text
    y = json.loads(x)
    # print(y["access_token"])
    return y