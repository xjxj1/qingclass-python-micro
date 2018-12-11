# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 23:00:00
# @Author  : Wang XiaoLong (xiaolongw123@gmail.com)
# @Link    : https://github.com/xjxj1
# @Version : $Id$
from flask_script import Manager
from project import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()