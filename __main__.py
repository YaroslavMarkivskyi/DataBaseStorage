from database import Database
from config import Config

if __name__ == "__main__":
    db_type = Config.DB_TYPE
    db_host = Config.DB_HOST
    db_name = Config.DB_NAME
    db_user = Config.DB_USER
    db_pass = Config.DB_PASS

    db = Database(db_type, db_host, db_name, db_user, db_pass)
