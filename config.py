import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    默认配置
    在本地调试时development继承default所有配置，同名覆盖；
    测试环境test + default
    生产环境production + default
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'intellif_AIOS_DMP'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://localhost/fsppgg_test'
    # SQLALCHEMY_ECHO = False
    # DEBUG = True
    # postgresql://scott:tiger@localhost/mydatabase
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'postgresql://postgres:38x92599w.-*,?@localhost/postgres'


class TestingConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
