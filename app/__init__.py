
from pip import main
from .config import config
from flask import Flask
from authlib.integrations.flask_client import OAuth

# initializations goes here
oauth = OAuth()

def create_app(conf = 'default'):
    app = Flask(__name__)
    app.config.from_object(config[conf])
    config[conf].init_app(app)

    # app instance initializations
    oauth.init_app(app)
    
    # register blueprint
    from .blueprint import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

