# coding: utf8

"""

    gjms.util.report

    Output, logging and reporting of various things.

"""

import inspect
import time


def log(string):
    """ Log to gjms.log """

    module = inspect.currentframe().f_back
    gjms_log = open("gjms.log", "w")

    gjms_log.write("[%s] %s - %s \n" % (time.strftime("%d/%m/%Y | %H:%M:%S"), module.f_globals['__name__'], string))


def output(string):
    """ Log into console """

    module = inspect.currentframe().f_back
    print "[%s] %s - %s" % (time.strftime("%d/%m/%Y | %H:%M:%S"), module.f_globals['__name__'], string)
