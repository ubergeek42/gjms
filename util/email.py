#coding: utf8

""" Check if a given e-mail fits the format x@y.z """

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import re
import gjms.core.exceptions


def validate(email):
    """ Validate e-mail according to regex """
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        raise gjms.core.exceptions.InvalidEmail("E-mail not in a valid format.")

