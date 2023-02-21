from ..database import models, schemas
from sqlalchemy.orm import Session
from security import get_hashed_password, verify_password, create_access_token

def create_new_user(user: schemas.UserCreate, db : Session):
    hashed_password = get_hashed_password(user.password)
    new_user = models.User(email=user.email, password=hashed_password, name=user.email.split("@")[0])
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user