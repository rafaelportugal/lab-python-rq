# encoding: utf-8
import os

from flask import request, abort
from functools import wraps


# Login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        token = request.headers.get('APP_TOKEN')
        if token == os.getenv('SECRET_KEY', '123456'):
            return f(*args, **kwargs)
        else:
            return abort(401)

    return wrap
