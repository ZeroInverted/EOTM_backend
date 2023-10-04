from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from pathlib import Path
import configparser

# Config parser is used to read db configuration from a .ini file to avoid hardcoding db credentials
config = configparser.ConfigParser()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dbconfig_path = Path(BASE_DIR, "dbconfig.ini")

config.read(dbconfig_path)


DATABASE_URL = f'postgresql://{config["pg-database"]["user"]}:{config["pg-database"]["password"]}@{config["pg-database"]["host"]}:{config["pg-database"]["port"]}/{config["pg-database"]["host"]}'

engine = create_engine(DATABASE_URL)

# Scoped sessions for thread-local sessions and easy session instantiation through db_session()
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


def get_db() -> db_session:
    db = db_session()
    try:
        yield db
    finally:
        db.close()
