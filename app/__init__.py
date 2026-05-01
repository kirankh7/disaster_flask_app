import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.main import main_bp
    from .routes.health import health_bp
    from .routes.ai import ai_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(ai_bp)

    from .errors import register_error_handlers
    register_error_handlers(app)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s %(message)s',
    )
    return app
