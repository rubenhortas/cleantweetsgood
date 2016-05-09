#!/usr/bin/env python
# _*_ coding:utf-8 _*


"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    error_handler  
"""

from crosscutting.condition_messages import print_error


def handle_error(err, ext):
    print_error(err.decode("UTF-8"))

    if ext:
        exit(1)
