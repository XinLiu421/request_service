# -*- coding: utf-8 -*-
# @Time    : 2019-07-03 15:36
# @Author  : xin.liu
# @File    : request_data.py


from flask import request
from flask_restful import Resource
from app.api_v1.common.request_parser import parse_query_request
from app.api_v1.common.exception import BadRequestBodyException, InvalidParamsException
from app.api_v1.Request.get_data import GetData
import logging
logger = logging.getLogger(__name__)


class RequestData(Resource):
    def __init__(self):
        self.request_json = request.get_json()
        self.parsed_data = parse_query_request(self.request_json)
        super(RequestData, self).__init__()

    def post(self):
        try:
            if self.parsed_data is None:
                raise BadRequestBodyException
            else:
                GetData(self.parsed_data).sent_request()
                return "success"
        except InvalidParamsException:
            return "fail"
