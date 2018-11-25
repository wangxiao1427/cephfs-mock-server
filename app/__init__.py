from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from werkzeug.utils import import_string

moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    db.init_app(app)

    # 注册蓝本
    blueprints = ['app.resources:main_blueprint']
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)

    return app
