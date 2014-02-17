#coding: utf8
""" Module for connecting and setting up a database. """

import os, sys, elixir

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

DB = elixir.metadata

def setup(database):
    """ Connect to database and setup all models """
    DB.bind = "sqlite:///%s" % (database)
    DB.bind.echo = True

    print "Database successfully initialized."
