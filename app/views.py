from crypt import methods
from flask import render_template, redirect, url_for, flash
from .blueprint import main
import time
from . import oauth
import os

# root
@main.route('/')
def index():
    now = time.time()
    return render_template('index.html', time = time.ctime(now), email = None, name = None, img = None)

# resorce owner authorization
@main.route('/google/')
def google():
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    CONF_URI = "https://accounts.google.com/.well-known/openid-configuration"
    oauth.register(
        name='google',
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        server_metadata_url=CONF_URI,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    redirect_uri = url_for('main.auth', _external = True)
    return oauth.google.authorize_redirect(redirect_uri)

# redirectiion URI
@main.route('/auth/')
def auth():
    token = oauth.google.authorize_access_token()
    _token = str(token)
    email = str(token['userinfo']['email'])
    name = str(token['userinfo']['name'])
    img = str(token['userinfo']['picture'])
    print("#"*30)
    print(token)
    return render_template('index.html', name = name, email = email, img = img)


# twitter login interface
# facebook login interface

