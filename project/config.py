# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 23:00:00
# @Author  : Wang XiaoLong (xiaolongw123@gmail.com)
# @Link    : https://github.com/xjxj1
# @Version : 1.0
class BaseConfig:
    """ 基础配置 """
    DEBUG = False
    TESTING = False

class DevelopmentConfig:
    """ 开发环境配置 """
    DEBUG = True

class TestingConfig:
    """ 测试环境配置 """
    DEBUG = True
    TESTING = True

class ProductionConfig:
    """ 生产环境配置 """
    DEBUG = False





