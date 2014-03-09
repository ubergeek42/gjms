#coding: utf8

"""

	gjms.config

	Contains various information about the instance of GJMS.

"""

import os, sys, flask
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

version = "0.4.5"

label = ""

manager = ""
manager_email = ""

database = "sqlite:///gjms_database.db"
theme_voting = False
game_ratings = False
