# 此文件负责注册路由
from flask import Blueprint
from flask_restful import Api

main_blueprint = Blueprint('main', __name__, url_prefix='/api')
api = Api(main_blueprint)
# views中还会导入蓝本main，所以需要末尾导入
from . import views
