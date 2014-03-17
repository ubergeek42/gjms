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

class ConfigParserFix(ConfigParser.RawConfigParser):
    """
        Apparently the getboolean method of the RawConfigParser is broken.
        Here's a fix.
    """

    def getboolean(self, section, option):
        result = self.get(section, option)
        try:
            trues = ["1", "yes", "true", "on"]
            falses = ["0", "no", "false", "off"]
            if result.lower() in trues:
                return True
            if result.lower() in falses:
                return False
        except AttributeError as err:
            if str(err) == "\'bool\' object has no attribute \'lower\'":
                return result
            raise err

parser = ConfigParserFix()
parser.read(os.path.abspath(os.path.dirname(__file__)+"/gjms.cfg"))

gjms.util.report.output(parser.sections())
