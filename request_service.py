# -*- coding: utf-8 -*-
# @Time    : 2019-07-03 14:25
# @Author  : xin.liu
# @File    : request_service.py

from app import create_app
import logging

app = create_app()
gunicorn_logger = logging.getLogger("gunicorn.error")
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

logger = logging.getLogger(__name__)
logger.info("finish init app")


@app.route('/')
def health_check():
    return 'activate'


if __name__ == '__main__':
    app.run(debug=True)
