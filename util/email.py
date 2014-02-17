#coding: utf8
""" Check if a given e-mail fits the format x@y.z """

import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import re

def validate(email):
    """ Validate e-mail according to regex """
    return True if re.match(r"[^@]+@[^@]+\.[^@]+", email) else False
