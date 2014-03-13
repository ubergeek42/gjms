#coding: utf8

"""

    gjms.backend.forms

    The all around loved forms for various purposes.
    Includes registration, login, game submission and such.

"""

import os
import sys

from flask_wtf import Form

import wtforms
import wtforms.validators

import gjms.util.report


sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

gjms.util.report.output("Generating forms..")

class login(Form):
    """ Login form. """
    def __init__(self):
        pass
gjms.util.report.output("Login form..")

class registration(Form):
    """ Registration form """
    def __init__(self):
        pass
gjms.util.report.output("Registration form..")


class game_submission(Form):
    """ Game submission form """
    def __init__(self):
        pass
gjms.util.report.output("Game submission form..")


class event_creation(Form):
    """ Event creation """
    def __init__(self):
        pass
gjms.util.report.output("Event creation form..")

class config(Form):
    """ The config menu """

    label = wtforms.TextField(u"Label:", [wtforms.validators.required()])

    manager = wtforms.TextField(u"Manager:", [wtforms.validators.required()])
    m_email = wtforms.TextField(u"E-Mail:", [wtforms.validators.optional(), wtforms.validators.email()])

    v_theme = wtforms.BooleanField(u"Allow theme voting:", [wtforms.validators.optional()])
    ratings = wtforms.BooleanField(u"Allow game ratings:", [wtforms.validators.optional()])

gjms.util.report.output("GJMS configuration form..")

gjms.util.report.output("Forms generated!")

