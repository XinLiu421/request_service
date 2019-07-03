# -*- coding: utf-8 -*-
# @Time    : 2019-07-03 15:36
# @Author  : xin.liu
# @File    : request_risk_v2.py


from flask import request
from flask_restful import Resource
import logging
logger = logging.getLogger(__name__)


class RequestRiskV2(Resource):
    def __init__(self):
        self.request_json = request.get_json()

    def test(self):
        return 'success'
