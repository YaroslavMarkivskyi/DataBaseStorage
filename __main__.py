from database import Database
from config import Config


if __name__ == "__main__":
    db_host = Config.DB_HOST
    db_name = Config.DB_NAME
    db_user = Config.DB_USER
    db_password = Config.DB_PASS

    db = Database(db_host, db_name, db_user, db_password)
