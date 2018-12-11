# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 23:00:00
# @Author  : Wang XiaoLong (xiaolongw123@gmail.com)
# @Link    : https://github.com/xjxj1
# @Version : $Id$
from flask import Flask, jsonify

# 初始化app
app = Flask(__name__)

@app.route('/ping', methods=['get'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
        })
