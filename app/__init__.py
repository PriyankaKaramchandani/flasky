from flask import Flask
from .routes.cat_routes import cats_bp
from .routes.dog_routes import dogs_bp

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.register_blueprint(cats_bp)
    app.register_blueprint(dogs_bp)

    return app