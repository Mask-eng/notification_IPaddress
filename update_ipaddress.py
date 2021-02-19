#!/usr/bin/env python
# -*- coding: utf-8 -*-
# revision 0
#
# description:
# This script works to notify of the updated address information.
#
# to update address infomation
# ->use BasicAuthentication to www.mydns.jp
#
# to notify updated address infomation
# -> use incoming webhooks(slack)
#
# class
# - basic_authentication and notify webhook
#
# data
# - message
#
# -> exac class(data)

# Variable chara
MYDNS_POST_URL      =   'https://www.mydns.jp/login.html'
WEBHOOK_URL         =    credential.WEBHOOK_URL

# to post lib
import requests
from requests.auth import HTTPBasicAuth

# slack
import json

# password
import credential

#post_to_mydns.py
print(credential.MYDNS_USER, credential.MYDNS_PASSWORD)

#------------------------------
# post to mydns service
#------------------------------
def post_to_mydns(username, password):
    #print(username, password, post_url)

    response_from_mydns = requests.get(
            MYDNS_URL, auth=HTTPBasicAuth( username, password )
            )
    #print(response.status_code)
    #return response.status_code
    return response_from_mydns
###end

result_from_mydns = post_to_mydns(credential.MYDNS_USER, credential.MYDNS_PASSWORD)
print(result.status_code)
print(result.text)
print(result.json())


#------------------------------
# post to slack
#------------------------------
def post_to_slack(message='hoge'):
    #slack_data = json.dumps({'blocks': message})
    print(webhook_url)
    #print(message)
    response = requests.post(
            webhook_url,
            json=({"text" :"I'm posting to Slack via webhook"}),
            headers={'Content-Type': 'application/json'}
            )
    print(response.status_code)
    print(response.headers)
    print(response.encoding)
    print(response.text)
    print(response.json())
    print ('-------')
    print(response.raw)


#post_to_slack()
#post_to_mydns(credential.userid , credential.userpass)

#print(post_to_mydns(credential.userid , credential.userpass))
#result = post_to_mydns(credential.userid , credential.userpass)
#print( result.status_code)

def hoge():
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
