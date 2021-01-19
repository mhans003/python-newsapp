from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Connect to database using env variable.

# Engine handles connection to database.
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# Session will allow for CRUD operations.
Session = sessionmaker(bind=engine)
# Base will map models to data tables.
Base = declarative_base()