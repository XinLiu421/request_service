# -*- coding: utf-8 -*-
# @Time    : 2019-07-03 14:25
# @Author  : xin.liu
# @File    : __init__.py.py

from flask import Flask


def create_app():
    app = Flask(__name__)
    from .api_v1 import api_bp as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint, url_prefix='request_data/v1')