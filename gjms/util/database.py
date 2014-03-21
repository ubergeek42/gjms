#coding: utf8
""" Module for connecting and setting up a database. """

import os
import sys

import elixir
import gjms.util.report

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
gjms_database = elixir.metadata

def setup(database):
    """ Connect to database and setup all models """
    gjms_database.bind = "%s" % database
    gjms_database.bind.echo = False

    gjms.util.report.output("Database (%s) initialized." % database)
    gjms.util.report.log("Database (%s) initialized." % database)
