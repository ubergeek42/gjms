#coding: utf8

"""

    gjms

    The main module where everything goes together.
    Starts up the Flask app, and sets the routes.

"""

import os
import string

import flask
import flask.ext.login

import gjms.backend
import gjms.util.report
import gjms.util

from werkzeug.contrib.fixers import ProxyFix

app = flask.Flask(__name__, static_folder="media")

lm = flask.ext.login.LoginManager()
lm.init_app(app)


@lm.user_loader
def load_user(userid):
    return gjms.core.users.User.get(userid)

gjms.backend.setup()

app.secret_key = os.urandom(24)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.debug = True

w, h = gjms.util.terminal_size()

print ""
print string.center("-----------------------------------------------------", w)
print string.center("Welcome to the Game Jam Management System", w)
print string.center("-----------------------------------------------------\n", w)
print string.center("FIRST THINGS FIRST:", w)
print string.center("If you haven't set up your .htaccess yet, please do", w)
print string.center("so now. See http://github.com/Folis/gjms#getting-started", w)
print string.center("for a short guide on this matter.", w)
print ""
print string.center("Otherwise:", w)
print string.center("Visit http://yoursite.com/gjms-config/ to get started", w)
print string.center("with the setup process of your game jam!", w)
print string.center("Enjoy!\n", w)
print string.center("________ Web server output below here ________\n", w)
