from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
# Use application context (g object) to provide global variables.
from flask import g

load_dotenv()

# Connect to database using env variable.

# Engine handles connection to database.
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# Session will allow for CRUD operations.
Session = sessionmaker(bind=engine)
# Base will map models to data tables.
Base = declarative_base()

def init_db(app):
    Base.metadata.create_all(engine)
    app.teardown_appcontext(close_db)

# Return a new session connection object on the g object (or the existing one).
def get_db():
    if 'db' not in g:
        # Store db connection in app context, if not already.
        g.db = Session()

    return g.db

# Close the connection if not already closed.
def close_db(e=None):
    # If we don't find db in the g object, we know there is no connection to close.
    db = g.pop('db', None)

    if db is not None:
        db.close()