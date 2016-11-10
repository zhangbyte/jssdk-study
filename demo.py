# -*- coding: utf-8 -*-
from flask import Flask, request
from jssdk import getAccessToken, getWebAccessToken, getUserInfo

import urllib,urllib2,json

app = Flask(__name__)

@app.route('/')
def hello_world():
        code = request.args.get('code', '')
        state = request.args.get('state', '')

        tokenJson = getWebAccessToken(code, state)
        access_token = tokenJson['access_token']
        openid = tokenJson['openid']

        infoJson = getUserInfo(access_token, openid)

        return json.dumps(infoJson, encoding='utf-8', ensure_ascii=False)

@app.route('/getAT')
def getAT():
        print getAccessToken()
        return 'hello'

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080)
