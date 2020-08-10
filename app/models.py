#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/8/10 14:42
# @Author  : MQS
# @File    : models.py

import json
from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(255))

    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return 'User{id=%d,name=%s,age=%d,phone=%s}' % (self.id, self.name, self.age, self.phone)