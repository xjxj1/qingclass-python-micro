# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 23:00:00
# @Author  : Wang XiaoLong (xiaolongw123@gmail.com)
# @Link    : https://github.com/xjxj1
# @Version : $Id$
import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# 初始化app
app = Flask(__name__)
# 环境配置
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# 初始化数据库
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    create_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.create_at = datetime.datetime.utcnow()

@app.route('/ping', methods=['get'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
        })
