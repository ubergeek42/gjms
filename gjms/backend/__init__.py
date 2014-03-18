#coding: utf8

"""

    gjms.backend

    Contains everything regarding the backend.
    This includes the forms for management as well as templates.

"""

import os
import sys

import gjms.util.report
import gjms.util.password
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

@app.route("/gjms/")
def gjms_central():
    return flask.render_template("backend/home.html", config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
gjms.util.report.output("Setup route /gjms/")

@app.route("/gjms/users/")
def gjms_users():
    return flask.render_template("backend/users.html", config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
gjms.util.report.output("Setup route /gjms/users/")

@app.route("/gjms/games/")
def gjms_games():
    return flask.render_template("backend/games.html", config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
gjms.util.report.output("Setup route /gjms/games/")

@app.route("/gjms/events/")
def gjms_events():
    return flask.render_template("backend/events.html", config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
gjms.util.report.output("Setup route /gjms/events/")

@app.route("/gjms/config/", methods=["GET", "POST"])
def gjms_config():
    """ Setup backend config """
    form = gjms.backend.forms.config(flask.request.form)

    if flask.request.method == "POST":
        if form.validate_on_submit():
            gjms.config.parser.set("gjms", "label", form.label.data)
            gjms.config.parser.set("gjms", "manager", form.manager.data)
            gjms.config.parser.set("gjms", "manager_email", form.m_email.data)
            gjms.config.parser.set("gjms", "theme_voting", form.v_theme.data)
            gjms.config.parser.set("gjms", "game_ratings", form.ratings.data)
            gjms.config.parser.set("gjms", "game_comments", form.comments.data)

            gjms.config.parser.set("gjms", "database_engine", form.engine.data)
            gjms.config.parser.set("gjms", "database_host", form.host.data)
            gjms.config.parser.set("gjms", "database_port", form.port.data)
            gjms.config.parser.set("gjms", "database_user", form.user.data)
            gjms.config.parser.set("gjms", "database_password", form.password.data)
            gjms.config.parser.set("gjms", "database", form.db.data)

            if form.engine.data == "sqlite" and form.port.data == "":
                db_url = "sqlite:///%s" % form.host.data
            elif form.engine.data != "sqlite" and form.port.data == "":
                db_url = "%s://%s:%s@%s/%s" % (form.engine.data, form.user.data, form.password.data, form.host.data, form.db.data)
            else:
                db_url = "%s://%s:%s@%s:%s/%s" % (form.engine.data, form.user.data, form.password.data, form.host.data, form.port.data, form.db.data)

            gjms.config.parser.set("gjms", "db_url", db_url)

            cfgfile = open(os.path.abspath(os.path.dirname(__file__)+"/../gjms.cfg"), "w")
            gjms.config.parser.write(cfgfile)
    else:
        form.label.data = gjms.config.parser.get("gjms", "label")
        form.manager.data = gjms.config.parser.get("gjms", "manager")
        form.m_email.data = gjms.config.parser.get("gjms", "manager_email")
        form.v_theme.data = gjms.config.parser.getboolean("gjms", "theme_voting")
        form.ratings.data = gjms.config.parser.getboolean("gjms", "game_ratings")
        form.comments.data = gjms.config.parser.getboolean("gjms", "game_comments")

        form.engine.data = gjms.config.parser.get("gjms", "database_engine")
        form.host.data = gjms.config.parser.get("gjms", "database_host")
        form.port.data = gjms.config.parser.get("gjms", "database_port")
        form.user.data = gjms.config.parser.get("gjms", "database_user")
        form.password.data = gjms.config.parser.get("gjms", "database_password")
        form.db.data = gjms.config.parser.get("gjms", "database")

    return flask.render_template("backend/config.html", form=form, config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
gjms.util.report.output("Setup route /gjms/config/")
