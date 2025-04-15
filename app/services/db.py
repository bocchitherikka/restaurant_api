from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import logging
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("sqlalchemy.engine")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("db.log")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
