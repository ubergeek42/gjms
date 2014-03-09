#coding: utf8

"""

    gjms

    The main module where everything goes together.
    Starts up the Flask app, and sets the routes.

"""

import os
import sys
import string

import flask

# noinspection PyUnresolvedReferences
import gjms.util.report
# noinspection PyUnresolvedReferences
import gjms.util
from werkzeug.contrib.fixers import ProxyFix

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

app = flask.Flask(__name__, static_folder="media")

@app.route("/")
def root():
    return "Hello."

app.wsgi_app = ProxyFix(app.wsgi_app)

w, h = gjms.util.terminal_size()
print ""
print string.center("-----------------------------------------------------", w)
print string.center("Welcome to the Game Jam Management System", w)
print string.center("-----------------------------------------------------\n", w)
print string.center("FIRST THINGS FIRST:", w)
print string.center("If you haven't set up your .htaccess yet, please do", w)
print string.center("so now. See http://github.com/Folis/gjms for a short", w)
print string.center("guide on this matter.", w)
print ""
print string.center("Otherwise:", w)
print string.center("Visit http://yoursite.com/gjms-config/ to get started", w)
print string.center("with the setup process of your game jam!", w)
print string.center("Enjoy!\n", w)
print string.center("________ Web server output below here ________\n", w)
