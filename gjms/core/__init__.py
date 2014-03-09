#coding: utf8

""" 

    gjms.core

    The main module of GJMS containing all the important stuff:
    Users, games, ratings, events, platforms etc.

    Be careful when messing around here, you might break something.
    If you intend to fix something, be sure to pass the unit tests before
    submitting a pull request.

"""

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
