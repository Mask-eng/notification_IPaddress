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
# to post lib

import requests
from requests.auth import HTTPBasicAuth

# slack
import json

# password
import credential

# Variable character
MYDNS_URL           =   'https://www.mydns.jp/login.html'
WEBHOOK_URL         =    credential.WEBHOOK_URL


#post_to_mydns.py
print(credential.MYDNS_USER, credential.MYDNS_PASSWORD)

#--------------------------------------------------
# post to mydns service
#--------------------------------------------------
def post_to_mydns(username, password):
    response_from_mydns = requests.get(
            MYDNS_URL, auth=HTTPBasicAuth( username, password )
            )
    return response_from_mydns
###end

#--------------------------------------------------
# post to slack
#--------------------------------------------------
def post_to_slack(payload_message):
    print(payload_message)
    response_from_slack = requests.post(
            WEBHOOK_URL,
            json.dumps({"text" : payload_message }),
            headers={'Content-Type': 'application/json'}
            )

## exac
result_from_mydns = post_to_mydns(credential.MYDNS_USER, credential.MYDNS_PASSWORD)
###failed message example
# @channnel
# 
# Request to mydns returned an error %s, the response is:\n%s
# %  (result_from_mydns.status_code, result_from_mydns.text)
# 
#####

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

#-------------------------------------------------------------------------
#succeed_message='Login and IP address notification succeeded.'
#failed_message=(
#            '<!channel>\r' + 
#            'Request to mydns returned an error ' +  
#            '`' + str(result_from_mydns.status_code) + '`'
#            ', the response is:\r' + 
#            '```' + result_from_mydns.text + '```'
#        )
#
#if result_from_mydns.status_code != 200:
#    #post_to_slack('Login and IP address notification succeeded.')
#    post_to_slack(succeed_message)
#
#else:
#    post_to_slack(failed_message)
#def check_http_response(response):
#    if response != 200:
#        # post success message.
#        message = succeed_message
#        return message
#    else:
#        # post failed message and log.
#        message = failed_message
#        return message 
#print('hoge')
#print(result_from_mydns.status_code)
#print(check_http_response(result_from_mydns.status_code))
#post_to_slack(check_http_response(result_from_mydns.status_code))
