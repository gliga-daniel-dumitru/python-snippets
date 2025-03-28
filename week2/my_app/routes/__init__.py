from flask import Flask
from routes.post_routes import posts_routes
from config import Config
from models import db

def create_app(config_name=None):
    app = Flask(__name__)
    app.register_blueprint(posts_routes)

    if config_name:
        app.config.from_object(config_name)
    else:
        app.config.from_object(Config)
    db.init_app(app)

    return app
