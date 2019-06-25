import os


# default config
class BaseConfig(object):
    DEBUG = False
    # shortened for readability
    PROCESSES = os.environ.get('PROCESSES', 1)
    APP_NAME = "lab-rq"


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    DEBUG = True
    REDISTOGO_URL = "redis://localhost:6379/0"

    SECRET_KEY = "123456"
    QUEUE_NAME = "test"
    PAGE_SIZE = 100000

    IS_TEST = 1


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    REDISTOGO_URL = "redis://localhost:6379/0"

    SECRET_KEY = "123456"
    QUEUE_NAME = "development"
    PAGE_SIZE = 100000


class ProductionConfig(BaseConfig):
    DEBUG = False
