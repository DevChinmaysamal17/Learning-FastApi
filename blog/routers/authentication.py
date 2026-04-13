from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from blog import schemas, database, models, jwt_token
from sqlalchemy.orm import Session
from typing import List
from blog.hashing import Hash
from blog.routers import blog, user, authentication

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Invalid Credentials' )

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials" )
    
    access_token = jwt_token.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}