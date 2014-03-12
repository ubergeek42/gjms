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
import gjms.core.exceptions
import gjms.backend.forms
import flask.ext.login


sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))


def setup():
    """ Setup the backend routes """

    @gjms.app.route("/", methods=["GET", "POST"])
    @flask.ext.login.login_required
    def root():
        """ Setup root """

        config_form = gjms.backend.forms.gjms_config()

        return flask.render_template("backend-base.html", config=gjms.config, config_form=config_form)
    gjms.util.report.output("Setup route /")

    @gjms.app.route("/login/<name>/<pwd>")
    def login(name, pwd):
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

    @gjms.app.route("/gjms-config/")
    def gjms_config():
        """ Setup config """
        return "Config"
    gjms.util.report.output("Setup route /gjms-config/")
