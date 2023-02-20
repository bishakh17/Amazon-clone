import sqlalchemy.orm as orm
from database import models, database, schemas

def create_db():
    return database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
