class BaseConfig(object):
    DEBUG = False
    TESTING = False
    # DATABASE_URI = 


class DevConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    TESTING = True
