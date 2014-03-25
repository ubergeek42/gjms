"""

    gjms.frontend.routes

    All the frontend routes.

"""

import os
import sys
import flask
import datetime

import gjms.core.system
import gjms.core.users
import gjms.core.events
import gjms.core.games
import gjms.core.platforms
import gjms.core.ratings
import gjms.core.system

import gjms.util.report

from gjms.backend.app import app
from gjms.config import parser

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
system = gjms.core.system.get(1)

@app.route("/")
def gjms_root():
    """ The root route. """
    return flask.render_template("frontend/base.html", time=datetime, system=system, config=parser, users=gjms.core.users, events=gjms.core.events, games=gjms.core.games, platforms=gjms.core.platforms, ratings=gjms.core.ratings)
gjms.util.report.output("Setup route /")
