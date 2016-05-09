#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    exception_handler  
"""

from crosscutting.condition_messages import print_exception


def handle_exception(function, e):
    print_exception("{0}: {1}".format(function, e))
    exit(2)
