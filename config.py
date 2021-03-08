import os
class Config:
    '''
    General configuration parent class
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://qyunky:Lewis860@localhost/blog'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTES_API_BASE_URL = ' http://quotes.stormconsultancy.co.uk/popular.json'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class prodConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_options = {
'development':DevConfig,
'production':prodConfig
}