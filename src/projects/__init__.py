from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from projects.configs import Config
import marshmallow

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
bcrypt = Bcrypt()


def register_blueprints(app):
    from projects.endpoints.users import blueprint as users
    from projects.endpoints.status import blueprint as status

    app.register_blueprint(users)


def register_error_handler(app):
    @app.errorhandler(marshmallow.exceptions.ValidationError)
    def validation_error_handler(e):
        return jsonify(e.messages), 400


def create_app(enviroment):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(enviroment)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    register_error_handler(app)
    register_blueprints(app)

    return app