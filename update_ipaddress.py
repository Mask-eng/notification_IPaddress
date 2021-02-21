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

#------------------------------
# Library for 
#------------------------------
# - http request library
import requests
from requests.auth import HTTPBasicAuth

# posting to slack
import json

# password
import credential

#------------------------------
# Variable character
#------------------------------
MYDNS_URL           =   'https://www.mydns.jp/login.html'
WEBHOOK_URL         =    credential.WEBHOOK_URL

#--------------------------------------------------
# post to mydns service
#--------------------------------------------------
def post_to_mydns(username, password):
    response_from_mydns = requests.get(
            MYDNS_URL, auth=HTTPBasicAuth( username, password )
            )
    return response_from_mydns

#--------------------------------------------------
# post to slack
#--------------------------------------------------
def post_to_slack(payload_message):
    response_from_slack = requests.post(
            WEBHOOK_URL,
            json.dumps({"text" : payload_message }),
            headers={'Content-Type': 'application/json'}
            )

## exac
result_from_mydns = post_to_mydns(credential.MYDNS_USER, credential.MYDNS_PASSWORD)

#--------------------------------------------------
# check http post response
#--------------------------------------------------
if result_from_mydns.status_code == 200:
    # post succeed message
    post_to_slack('Login and IP address notification succeeded.')

else:
    # post failed message
    post_to_slack(
            '<!channel>\r' + 
            'Request to mydns returned an error ' +  
            '`' + str(result_from_mydns.status_code) + '`'
            ', the response is:\r' + 
            '```' + result_from_mydns.text + '```'
            )




