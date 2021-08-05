from flask import Flask, current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    with app.app_context():

        db.init_app(app)
        migrate.init_app(app, db)

        from app.main import bp as main_bp
        app.register_blueprint(main_bp)

        return app


from app import models
