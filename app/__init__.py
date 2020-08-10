#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/8/9 17:34
# @Author  : MQS
# @File    : __init__.py.py

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    # 初始化
    app = Flask(__name__)

    # 导致指定的配置对象:创建app时，传入环境的名称
    app.config.from_object(config[config_name])

    # 初始化db
    db.init_app(app)

    # 注册所有蓝图
    regist_blueprints(app)

    return app


def regist_blueprints(app):
    # 导入蓝图对象
    # 方式一
    from app.api import api

    # 方式二：这样，就不用在app/api/__init__.py（创建蓝本时）里面的最下方单独引入各个视图模块了
    # from app.api.views import api
    # from app.api.errors import api

    # 注册api蓝图,url_prefix为所有路由默认加上的前缀
    app.register_blueprint(api, url_prefix='/api')