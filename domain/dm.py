#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    dm
"""

from crosscutting.cleantweetsgood_messages import print_blacklisted
from crosscutting.constants import ENCODING


class DM:
    id = None
    text = None

    def __init__(self, dm_id, text):
        self.id = dm_id
        self.text = "{0}\n".format(text.replace("\n", " ").lower().encode(ENCODING))

    def print_info(self):
        print_blacklisted(self.text)
