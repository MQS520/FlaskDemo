#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/8/10 15:00
# @Author  : MQS
# @File    : user.py

from flask import jsonify
from app.api import api
from ..models import User
from .. import db

@api.route('/insert', methods=['POST', 'GET'])
def insert():
    '''
    单表插入
    :return:
    '''
    user1 = User(name='MQS', age=24, phone='110')
    db.session.add_all([user1])
    res = {'code': 200, 'msg': '插入成功'}
    return jsonify(res)

@api.route('/select', methods=['POST', 'GET'])
def select():
    '''
    查询所有
    :return:
    '''
    ulist = User.query.all()
    for user in ulist:
        print(user)
    res = {'code': 200, 'msg': '查询成功'}
    return jsonify(res)

