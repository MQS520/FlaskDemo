#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/8/9 17:34
# @Author  : MQS
# @File    : config.py


# 配置环境的基类
class Config(object):

    # 每次请求结束后，自动提交数据库中的变动，该字段在flask-sqlalchemy 2.0之后已经被删除了（有bug）
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 2.0之后新加字段，flask-sqlalchemy 将会追踪对象的修改并且发送信号。
    # 这需要额外的内存，如果不必要的可以禁用它。
    # 注意，如果不手动赋值，可能在服务器控制台出现警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 数据库操作时是否显示原始SQL语句，一般都是打开的，因为后台要日志
    SQLALCHEMY_ECHO = True


# 开发环境的配置
class DevelopmentConfig(Config):
    DEBUG = True
    # 数据库URI
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xxx@xxxx/xxx'

    # 也可如下来写，比较清晰
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}/{databasename}".format(username="xxxx", password="xxxx", hostname="xxxx", databasename="xxxx")


# 测试环境的配置
class TestingConfig(Config):

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@172.17.180.3:3306/cleven_test'

    """
    测试环境也可以使用sqlite，默认指定为一个内存中的数据库，因为测试运行结束后无需保留任何数据
    也可使用  'sqlite://' + os.path.join(basedir, 'data.sqlite') ，指定完整默认数据库路径
    """
    # import os
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'


# 生产环境的配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xxx@xxxx:3306/xxxx'


# 初始化app实例时对应的开发环境声明
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}