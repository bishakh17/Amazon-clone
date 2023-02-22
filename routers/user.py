from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from utils.user import create_new_user
from utils.user import authenticate_user
from utils.db import get_db
from database import schemas

router = APIRouter(prefix="/user", tags=["user"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Token)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    access_token = create_new_user(user,db)
    if not access_token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return access_token
    

@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    access_token = authenticate_user(email=form_data.username, password=form_data.password, db=db)
    if not access_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    return access_token