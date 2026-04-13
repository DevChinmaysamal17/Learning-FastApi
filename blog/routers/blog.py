from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from blog import schemas, models , hashing, database, oauth2
from blog.database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from blog.repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
    )

get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), curent_user: schemas.UserCreate = Depends(oauth2.get_curent_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.BlogCreate, db: Session = Depends(get_db), curent_user: schemas.UserCreate = Depends(oauth2.get_curent_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), curent_user: schemas.UserCreate = Depends(oauth2.get_curent_user)):
    return blog.destroy(id, db)

    
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), curent_user: schemas.UserCreate = Depends(oauth2.get_curent_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id:int, db: Session = Depends(get_db), curent_user: schemas.UserCreate = Depends(oauth2.get_curent_user)):
    return blog.show(id, db)


