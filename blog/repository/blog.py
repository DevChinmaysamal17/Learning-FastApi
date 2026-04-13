from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from blog import schemas, models , hashing, database
from blog.database import engine, SessionLocal
from typing import List
from sqlalchemy.orm import Session

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.BlogCreate, db: Session):
    user = db.query(models.User).filter(models.User.id == request.user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        user_id=request.user_id
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

def destroy(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=404, detail="Blog not found")

    blog.delete(synchronize_session=False)
    db.commit()

    return {"message": "Blog deleted successfully"}

def update(id:int, request: schemas.Blog,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=404, detail="Blog not found")

    blog.update({
    "title": request.title,
    "body": request.body
    })
    db.commit()
    return 'updated successfully'

def show(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first() 
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id:{id} is not available')
    return blog