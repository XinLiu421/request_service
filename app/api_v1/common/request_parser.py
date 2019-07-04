# -*- coding: utf-8 -*-
# @Time    : 2019-07-04 12:11
# @Author  : xin.liu
# @File    : request_parser.py

from marshmallow import Schema, fields, ValidationError
import logging
logger = logging.getLogger(__name__)


class BodySchema(Schema):
    api_type = fields.String(required=True)


def parse_query_request(request_json):
    qrs = BodySchema(strict=True)
    try:
        parsed_data, error = qrs.load(request_json)
        if error == {}:
            return parsed_data
        else:
            logger.exception("parse request body failed")
            return None
    except ValidationError as err:
        logger.exception("not found api name in request")
        return None
