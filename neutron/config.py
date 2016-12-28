import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('NEUTRON_SECRET_KEY') or 'Neutron is neutron'

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'ProductionConfig': ProductionConfig,
    'default': DevelopmentConfig
}
