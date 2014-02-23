#coding: utf8

"""

    gjms.util.url

    A module for checking if the user has provided a valid URL and not
    a random string.

"""

import os, sys, gjms.core.exceptions
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import re

def validate(url):
    """ Check if the provided string matches a URL regex. """
    if re.match(ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))', url):
        return True
    else:
        raise gjms.core.exceptions.InvalidURL("URL not in a valid format.")
 