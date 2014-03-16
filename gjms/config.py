#coding: utf8

"""

    gjms.config

    A parser for the gjms.cfg file.
    Used for config updates within the scripts.

"""

import os
import sys
import ConfigParser

import gjms.util.report

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

parser = ConfigParser.RawConfigParser()
parser.read(os.path.abspath(os.path.dirname(__file__)+"/gjms.cfg"))

gjms.util.report.output(parser.sections())
