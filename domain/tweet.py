#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    tweet  
"""

from configuration import BLACK_LIST
from crosscutting.cleantweetsgood_messages import print_blacklisted, print_whitelisted


class Tweet:
    id = None
    text = None
    isBlackListed = False
    blacklisted_word = ""

    def __init__(self, tweet_id, text=None):
        self.id = tweet_id
        if text:
            self.text = "{0}\n".format(text.replace("\n", " ").lower())
            self.__setBlacklisted()
        else:
            self.blacklisted = True

    def print_info(self):
        if self.text:
            if self.isBlackListed:
                print_blacklisted(self.text, self.blacklisted_word)

            if not self.isBlackListed:
                print_whitelisted(self.text)
        else:
            print_blacklisted(self.id)

    # noinspection PyPep8Naming
    def __setBlacklisted(self):
        for element in BLACK_LIST:
            word = " {0} ".format(element)
            if word.lower() in self.text:
                self.isBlackListed = True
                self.blacklisted_word = word.lower()
                break
