#coding: utf8

"""

    gjms.util.url

    A module for checking if the user has provided a valid URL and not
    a random string.

"""

import os
import sys

import gjms.core.exceptions


sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import re


def validate(url):
    """ Check if the provided string matches a URL regex. """
    regex = re.compile(
        r'^(?:http|ftp)s?://'    # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'    # domain...
        r'localhost|'    # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'   # ...or ipv6
        r'(?::\d+)?'     # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if regex.match(url):
        return True
    else:
        raise gjms.core.exceptions.InvalidURL("URL not in a valid format.")
 