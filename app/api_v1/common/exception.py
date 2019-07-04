# -*- coding: utf-8 -*-
# @Time    : 2019-07-04 12:14
# @Author  : xin.liu
# @File    : exception.py


class ApiException(Exception):
    pass


class BadRequestBodyException(ApiException):
    pass


class InvalidParamsException(ApiException):
    pass
