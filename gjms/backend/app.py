"""

    gjms.backend.app

    The app container for GJMS.

"""

import os
import sys
import flask

from werkzeug.contrib.fixers import ProxyFix

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

app = flask.Flask(__name__, static_folder="../media", template_folder="../templates")
app.secret_key = os.urandom(24)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.debug = True