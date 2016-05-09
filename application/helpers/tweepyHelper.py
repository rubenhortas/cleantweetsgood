#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    CleanTweetsGood
"""

import tweepy

from application.handlers.exception_handler import handle_exception
from configuration import ACCESS_TOKEN
from configuration import ACCESS_TOKEN_SECRET
from configuration import CONSUMER_KEY
from configuration import CONSUMER_SECRET


def login():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth
    except Exception as e:
        handle_exception(login.__name__, e)


def get_api(auth):
    try:
        return tweepy.API(auth, wait_on_rate_limit=True)
    except Exception as e:
        handle_exception(get_api.__name__, e)
