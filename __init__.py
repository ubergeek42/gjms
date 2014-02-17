#coding: utf8

""" Setup GJMS. """

import os, sys, elixir, gjms.util.database
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

gjms.util.database.setup("tdb1.db")
