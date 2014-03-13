#coding: utf8

"""

    gjms.backend

    Contains everything regarding the backend.
    This includes the forms for management as well as templates.

"""

import os
import sys

import gjms.util.report
import gjms.config
import gjms.core.users
import gjms.core.exceptions
import gjms.backend.forms

from flask.ext.login import login_required

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import flask
import flask.ext.login
from werkzeug.contrib.fixers import ProxyFix

app = flask.Flask(__name__, static_folder="media")
app.secret_key = os.urandom(24)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.debug = True

lm = flask.ext.login.LoginManager()
lm.init_app(app)

@lm.user_loader
def load_user(userid):
    """ Grab the user for the login manager. """
    return gjms.core.users.User.get(userid)

@app.route("/")
@login_required
def gjms_main():
    """ Setup root """

    config_form = gjms.backend.forms.gjms_config()

    return flask.render_template("backend-base.html", config=gjms.config, config_form=config_form)
gjms.util.report.output("Setup route /")

@app.route("/login/<name>/<pwd>")
def gjms_login(name, pwd):
    try:
        user = gjms.core.users.get(name)
        if gjms.core.users.login(name, pwd):
            flask.ext.login.login_user(user)
            return "YEP."
        else:
            return "NOPE."
    except gjms.core.exceptions.NonExistentUser:
        return "User does not exist. Sorry."

gjms.util.report.output("Setup route /login/<name>/<pwd>")

@app.route("/gjms-config/")
def gjms_config():
    """ Setup config """
    return "Config"
gjms.util.report.output("Setup route /gjms-config/")
