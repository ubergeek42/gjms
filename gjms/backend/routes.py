"""

    gjms.backend.routes

    All backend routes.

"""

import os
import sys
import flask
import elixir
import datetime

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import gjms.util.report
import gjms.util.password
import gjms.util.database

import gjms.core.system
import gjms.core.users
import gjms.core.events
import gjms.core.games
import gjms.core.platforms
import gjms.core.ratings
import gjms.core.exceptions
import gjms.backend.forms

from gjms.backend.app import app
from gjms.config import parser

"""
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
"""

@app.route("/populate/<entries>")
def gjms_populate(entries):
    import gjms.util

    try:
        entries = int(entries)
    except TypeError:
        return "Please enter an integer."
    else:
        return gjms.util.populate_db(entries)

@app.route("/game/<id_slug>")
def gjms_game(id_slug):
    """ Display a game. """
    try:
        game = gjms.core.games.get(id_slug)
        system = gjms.core.system.get(1)
        return flask.render_template("frontend/game.html", game=game, time=datetime, system=system, config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
    except gjms.core.exceptions.NonExistentGame:
        try:
            game = gjms.core.games.by_slug(id_slug)
            system = gjms.core.system.get(1)
            return flask.render_template("frontend/game.html", game=game, time=datetime, system=system, config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
        except gjms.core.exceptions.NonExistentGame:
            return "We couldn't find the game you were looking for. Sorry."

@app.route("/gjms/home/")
def gjms_central():
    if parser.getboolean("gjms", "database_setup") == False:
        return flask.redirect("../../gjms/config/")
    system = gjms.core.system.get(1)
    return flask.render_template("backend/home.html", time=datetime, system=system, config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
gjms.util.report.output("Setup route /gjms/home/")

@app.route("/gjms/users/")
def gjms_users():
    if parser.getboolean("gjms", "database_setup") == False:
        return flask.redirect("../../gjms/config/")
    system = gjms.core.system.get(1)
    return flask.render_template("backend/users.html", time=datetime, system=system, config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
gjms.util.report.output("Setup route /gjms/users/")

@app.route("/gjms/games/")
def gjms_games():
    if parser.getboolean("gjms", "database_setup") == False:
        return flask.redirect("../../gjms/config/")
    system = gjms.core.system.get(1)
    return flask.render_template("backend/games.html", time=datetime, system=system, config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
gjms.util.report.output("Setup route /gjms/games/")

@app.route("/gjms/events/")
def gjms_events():
    if parser.getboolean("gjms", "database_setup") == False:
        return flask.redirect("../../gjms/config/")
    system = gjms.core.system.get(1)
    return flask.render_template("backend/events.html", time=datetime, system=system, config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
gjms.util.report.output("Setup route /gjms/events/")

@app.route("/gjms/config/", methods=["GET", "POST"])
def gjms_config():
    """ Setup backend config """
    form = gjms.backend.forms.config(flask.request.form)

    if flask.request.method == "POST":
        if form.validate_on_submit():
            parser.set("gjms", "label", form.label.data)
            parser.set("gjms", "manager", form.manager.data)
            parser.set("gjms", "manager_email", form.m_email.data)
            parser.set("gjms", "theme_voting", form.v_theme.data)
            parser.set("gjms", "game_ratings", form.ratings.data)
            parser.set("gjms", "game_comments", form.comments.data)

            parser.set("gjms", "database_engine", form.engine.data)
            parser.set("gjms", "database_host", form.host.data)
            parser.set("gjms", "database_port", form.port.data)
            parser.set("gjms", "database_user", form.user.data)
            parser.set("gjms", "database_password", form.password.data)
            parser.set("gjms", "database", form.db.data)

            if form.engine.data == "sqlite":
                db_url = "sqlite:///%s?check_same_thread=False" % form.host.data
            elif form.engine.data != "sqlite" and form.port.data == "":
                db_url = "%s://%s:%s@%s/%s" % (form.engine.data, form.user.data, form.password.data, form.host.data, form.db.data)
            else:
                db_url = "%s://%s:%s@%s:%s/%s" % (form.engine.data, form.user.data, form.password.data, form.host.data, form.port.data, form.db.data)

            gjms.util.database.setup(db_url)
            elixir.setup_all()
            elixir.create_all()

            parser.set("gjms", "db_url", db_url)
            parser.set("gjms", "database_setup", True)

            cfgfile = open(os.path.abspath(os.path.dirname(__file__)+"/../gjms.cfg"), "w")
            gjms.config.parser.write(cfgfile)

            flask.flash(u"Settings saved!", "success")
        else:
            flask.flash(u"Woops! That didn't work. Check below for details.", "error")
    else:
        form.label.data = parser.get("gjms", "label")
        form.manager.data = parser.get("gjms", "manager")
        form.m_email.data = parser.get("gjms", "manager_email")
        form.v_theme.data = parser.getboolean("gjms", "theme_voting")
        form.ratings.data = parser.getboolean("gjms", "game_ratings")
        form.comments.data = parser.getboolean("gjms", "game_comments")

        form.engine.data = parser.get("gjms", "database_engine")
        form.host.data = parser.get("gjms", "database_host")
        form.port.data = parser.get("gjms", "database_port")
        form.user.data = parser.get("gjms", "database_user")
        form.password.data = parser.get("gjms", "database_password")
        form.db.data = parser.get("gjms", "database")

    system = gjms.core.system.get(1)
    return flask.render_template("backend/config.html", form=form, time=datetime, system=system, config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
gjms.util.report.output("Setup route /gjms/config/")