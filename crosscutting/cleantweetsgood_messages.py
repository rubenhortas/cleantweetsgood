#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    cleantweetsgood_messages  
"""

from presentation.color import Color
from presentation.tag import Tag


def print_blacklisted(text, word=None):
    if word:
        highlighted_text = text.replace(word, "{0}{1}{2}".format(Color.red, word, Color.end))
        print("{0} {1}".format(Tag.black_list, highlighted_text))
    else:
        print("{0} {1}".format(Tag.black_list, text))


def print_whitelisted(text):
    print("{0} {1}".format(Tag.white_list, text))


def print_unfollow(user):
    print("{0} Unfollowing {1}".format(Tag.black_list, user))


def print_configuration_help():
    print("CleanTweetsGood is not configured.")
    print("Please get your credentials:")
    print("\t- Login on twitter with your account: https://twitter.com")
    print("\t- Go to: https://apps.twitter.com/")
    print("\t- Click on \"Create New App\"")
    print("\t- Fill the form")
    print("\t\tName: CleanTweetsGood")
    print("\t\tDescription: Twitter cleaner")
    print("\t\tWebsite: https://github.com/rubenhortas/cleantweetsgood")
    print("\t\tCallback URL: Leave this blank")
    print("\t\tAccept the Developer Agreement")
    print("\t- Go to \"Keys and Access Tokens\" tab")
    print("\t\tGet your access tokens: Consumer Key, Consumer Secret, Access Token and Access Token Secret")
    print("\t\tConfigure your tokens on the configuration.py file.")
    print("\t- Go to \"Permissions\" tab")
    print("\t\tChange \"Access\" to \"Read, Write and Access direct messages\"")
    print("\t- Update settings")
