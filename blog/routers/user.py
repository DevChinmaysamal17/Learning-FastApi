from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from blog import schemas, models , hashing, database
from blog.database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from blog.repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)
 
get_db = database.get_db

@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)): 
    
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)

@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
def destroy_user (id, db: Session = Depends(get_db)):
    return user.destroy_user(id, db)