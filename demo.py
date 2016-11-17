# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from jssdk import getWebAccessToken, getUserInfo, getSignature

import urllib, urllib2, json, time

app = Flask(__name__)

@app.route('/')
def hello_world():
        code = request.args.get('code', '')
        state = request.args.get('state', '')

        tokenJson = getWebAccessToken(code, state)
        access_token = tokenJson['access_token']
        openid = tokenJson['openid']

        infoJson = getUserInfo(access_token, openid)

        return infoJson

@app.route('/getT')
def getAT():
	timestamp = str(int(time.time()))
	nonceStr = 'duohuo'
	signature = getSignature(nonceStr, timestamp, request.url)

	return render_template('test.html',
		timestamp = timestamp,
		nonceStr = nonceStr,
		signature = signature)

@app.route('/upload', methods=['POST'])
def add_entry():
	media_id = request.form['media_id']
	print media_id

	return 'hello'


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080)

