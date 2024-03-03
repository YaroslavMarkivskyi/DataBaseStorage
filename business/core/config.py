import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class Config:
    """
    Configuration class to store all the configuration variables.
    """
    DB_TYPE = config['database']['db_type']
    DB_HOST = config['database']['db_host']
    DB_NAME = config['database']['db_name']
    DB_USER = config['database']['db_user']
    DB_PASS = config['database']['db_pass']
    DB_PORT = config['database']['db_port']
