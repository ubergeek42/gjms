#coding: utf8

"""

    gjms.backend

    Contains everything regarding the backend.
    This includes the forms for management as well as templates.

"""

import os
import sys

import gjms.util.report
import gjms
import gjms.config
import gjms.core.users
import flask.ext.login


sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))


def setup():
    """ Setup the backend roots """

    @gjms.app.route("/login/<name>/<pwd>")
    def login(name, pwd):
        if gjms.core.users.login(name, pwd):
            user = gjms.core.users.get(name)
            flask.ext.login.login_user(user)
            return "YEP."
        else:
            return "NOPE."

    @gjms.app.route("/")
    @flask.ext.login.login_required
    def root():
        """ Setup root """
        return flask.render_template("backend-base.html", config=gjms.config)

    gjms.util.report.output("Setup route /")

    @gjms.app.route("/gjms-config/")
    def gjms_config():
        """ Setup config """
        return "Config"

    gjms.util.report.output("Setup route /gjms-config/")
