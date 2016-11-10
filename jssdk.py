# -*- coding: utf-8 -*-

import urllib,urllib2,json

APPID = 'wx5f8976fb0725b9f9'
SECRET = '921b2a387dcc624d3d2b2d2a90707dbe'

def curl(url, para):
    """
    发送请求,并将返回结果解析成json格式
    """
    req = urllib2.Request(url + urllib.urlencode(para))
    res = urllib2.urlopen(req)
    jsonData = json.loads(res.read())

    return jsonData


def getAccessToken():
    """
    获取普通access_token
    """
    url = 'https://api.weixin.qq.com/cgi-bin/token?'
    para = {
        'grant_type': 'client_credential',
        'appid': APPID,
        'secret': SECRET
    }
    return curl(url, para)


def getWebAccessToken(code, state):
    """
    获取网页授权access_token
    引导关注者打开
    https://open.weixin.qq.com/connect/oauth2/authorize?appid=APPID&redirect_uri=REDIRECT_URI
    &response_type=code&scope=SCOPE&state=STATE#wechat_redirect
    scope值：snsapi_base （不弹出授权页面，直接跳转，只能获取用户openid），
            snsapi_userinfo （弹出授权页面，可通过openid拿到昵称、性别、所在地。并且，即使在未关注的情况下，只要用户授权，也能获取其信息）
    返回数据：
    {
        "access_token":"ACCESS_TOKEN",
        "expires_in":7200,
        "refresh_token":"REFRESH_TOKEN",
        "openid":"OPENID",
        "scope":"SCOPE"
    }
    """
    url = 'https://api.weixin.qq.com/sns/oauth2/access_token?'
    para = {
        'appid': APPID,
        'secret': SECRET,
        'code': code,
        'grant_type': "authorization_code"
    }
    return curl(url, para)


def getUserInfo(access_token, openid):
    """
    网页授权作用域为snsapi_userinfo，则可以通过access_token和openid拉取用户信息
    返回数据：
    {
        "openid":" OPENID",
        "nickname": NICKNAME,
        "sex":"1",
        "province":"PROVINCE"
        "city":"CITY",
        "country":"COUNTRY",
            "headimgurl": "http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/46", 
                "privilege":[
                    "PRIVILEGE1"
                    "PRIVILEGE2"
                ],
        "unionid": "o6_bmasdasdsad6_2sgVt7hMZOPfL"
    }
    """
    url = 'https://api.weixin.qq.com/sns/userinfo?'
    para = {
        'access_token': access_token,
        'openid': openid,
        'lang': 'zh_CN'
    }
    return curl(url, para)