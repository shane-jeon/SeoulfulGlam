"""SeoulfulGlam Server"""

import os
from flask import(
    Flask,
    session,
    render_template,
    request,
    jsonify,
    flash,
    redirect,
    url_for,
    Blueprint
)
from flask_debugtoolbar import DebugToolbarExtension 
from flask_login import (
    login_user,
    LoginManager,
    login_required,
    logout_user,
    current_user,
    UserMixin
)
from flask_bcrypt import Bcrypt
from model import BusinessUser, connect_to_db 
from sqlalchemy.sql import text
import crud
from jinja2 import StrictUndefined
# from square.client import Client
# from dotenv import load_dotenv
import os
import urllib.request, json




app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = '*xZJ_0d7c#+ii0C'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

APPLICATION_ID = os.environ['APPLICATION_ID']

@app.route('/')
def sample():
    return "<p>Hello</p>"

if __name__ == '__main__':
    app.run(debug=True)
