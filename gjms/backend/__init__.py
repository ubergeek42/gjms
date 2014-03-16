#coding: utf8

"""

    gjms.backend

    Contains everything regarding the backend.
    This includes the forms for management as well as templates.

"""

import os
import sys

import gjms.util.report
import gjms.core.users
import gjms.core.events
import gjms.core.games
import gjms.core.platforms
import gjms.core.ratings
import gjms.core.exceptions
import gjms.backend.forms

from gjms.config import parser
from flask.ext.login import login_required

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import flask
import flask.ext.login
from werkzeug.contrib.fixers import ProxyFix

app = flask.Flask(__name__, static_folder="../media", template_folder="../templates")
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
#@login_required
def gjms_main():
    """ Setup root """
gjms.util.report.output("Setup route /")

@app.route("/login/<name>/<pwd>")
def gjms_login(name, pwd):
    """ Test login function. """
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

@app.route("/gjms/config/", methods=["GET", "POST"])
def gjms_config():
    """ Setup backend config """
    form = gjms.backend.forms.config(flask.request.form)

    if flask.request.method == "POST":
        if form.validate():
            gjms.config.parser.set("gjms", "label", form.label.data)
            gjms.config.parser.set("gjms", "manager", form.manager.data)
            gjms.config.parser.set("gjms", "manager_email", form.m_email.data)
            gjms.config.parser.set("gjms", "theme_voting", form.v_theme.data)
            gjms.config.parser.set("gjms", "game_ratings", form.ratings.data)

            cfgfile = open(os.path.abspath(os.path.dirname(__file__)+"/../gjms.cfg"), "w")
            gjms.config.parser.write(cfgfile)
    else:
        form.label.data = gjms.config.parser.get("gjms", "label")
        form.manager.data = gjms.config.parser.get("gjms", "manager")
        form.m_email.data = gjms.config.parser.get("gjms", "manager_email")
        form.v_theme.data = gjms.config.parser.getboolean("gjms", "theme_voting")
        form.ratings.data = gjms.config.parser.getboolean("gjms", "game_ratings")

    return flask.render_template("gjms-backend-config.html", config_form=form, config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)

gjms.util.report.output("Setup route /gjms/config/")
