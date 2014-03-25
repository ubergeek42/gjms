#coding: utf8

"""

    gjms.backend

    Contains everything regarding the backend.
    This includes the forms for management as well as templates.

"""

import os
import sys
import flask
import flask.ext.login

import gjms.core.users
import gjms.backend.routes
import gjms.frontend.routes

from gjms.backend.app import app
from flask.ext.login import login_required

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

lm = flask.ext.login.LoginManager()
lm.init_app(app)

@lm.user_loader
def load_user(userid):
    """ Grab the user for the login manager. """
    return gjms.core.users.User.get(userid)
