# -*- coding: utf-8 -*-
# @Time    : 2019-07-03 15:30
# @Author  : xin.liu
# @File    : __init__.py.py


from flask import Blueprint
from flask_restful import Api
from .resources.request_risk_v2 import RequestRiskV2

api_bp = Blueprint('api', __name__)

api = Api(api_bp)
api.add_resource(RequestRiskV2, '/risk_v2')
