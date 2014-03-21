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

    # General jam options.
    label = wtforms.TextField(label=u"Label:", description="The general name of your events (i.e. Ludum Dare)", validators=[wtforms.validators.required()])
    manager = wtforms.TextField(label=u"Manager:", description="Who runs these events? (i.e. Mike Kasprzak)", validators=[wtforms.validators.required()])
    m_email = wtforms.TextField(label=u"E-Mail:", description="Where can the manager be contacted? (i.e. mikek@example.com)", validators=[wtforms.validators.optional(), wtforms.validators.email()])
    v_theme = wtforms.BooleanField(label=u"Theme voting:", description="Allow a theme voting process?", validators=[wtforms.validators.optional()])
    ratings = wtforms.BooleanField(label=u"Game ratings:", description="Allow game ratings?", validators=[wtforms.validators.optional()])
    comments = wtforms.BooleanField(label=u"Game comments:", description="Allow comments?", validators=[wtforms.validators.optional()])

    # Database stuff.
    engine = wtforms.SelectField(u"Engine:", description="Which database backend to use.", validators=[wtforms.validators.required()], choices=[('sqlite', 'SQLite'), ('mysql', 'MySQL'), ('postgre', 'PostgreSQL')])
    host = wtforms.TextField(label=u"Host:", description="Database host. Usually localhost", validators=[wtforms.validators.required()])
    port = wtforms.TextField(label=u"Port:", description="Database port. Usually 3306", validators=[wtforms.validators.optional()])
    user = wtforms.TextField(label=u"User:", description="Database user. Depends on host.", validators=[wtforms.validators.optional()])
    password = wtforms.PasswordField(label=u"Password:", description="Database password.", validators=[wtforms.validators.optional()])
    db = wtforms.TextField(label=u"Database:", description="Which database to use. Make sure it exists!", validators=[wtforms.validators.optional()])


gjms.util.report.output("GJMS configuration form..")
gjms.util.report.output("Forms generated!")

