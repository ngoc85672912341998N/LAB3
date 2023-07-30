from typing import List
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from . import crud, models, schemas
from .database import SessionLocal, engine
import httpx
import requests
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

app = FastAPI()
limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
timeout = httpx.Timeout(timeout=5.0, read=15.0)
client = httpx.AsyncClient(limits=limits, timeout=timeout)




# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("shutdown")
async def shutdown_event():
    print("shutting down...")
    await client.aclose()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    
    return templates.TemplateResponse("2.html", context={"request": request})

###################################################################################

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.ho_ten_nhan_su)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/create_mutiple_users/", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_mutiple_user(db=db, user=user)

@app.post("/get_update_luot_thich/")
def get_update_luot_thich(user: schemas.UpdatePost, db: Session = Depends(get_db)):
    print(user)
    return crud.get_update_user11(db=db, user=user)

@app.post("/get_update_time_users/")
def get_update1_user(user: schemas.UpdateTime, db: Session = Depends(get_db)):
    print(user)
    return crud.get_update_time_user11(db=db, user=user)


@app.post("/get_Delete_time_users/")
def get_Delete_time_users(user: schemas.DeleteTime, db: Session = Depends(get_db)):
    print(user)
    return crud.get_delete_time_user11(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

##################################################################################

@app.post("/create_update__time/", response_model=schemas.updateUser)
def create_update__time(user: schemas.updateUser, db: Session = Depends(get_db)):
    db_user = crud.get_update_user_by_email(db, thoi_gian=user.thoi_gian)
    if db_user:
        raise HTTPException(status_code=400, detail="time already registered")
    return crud.create_update_user(db=db, user=user)


@app.get("/read_update_time/", response_model=List[schemas.updateUser])
def read_update_time(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_update_users(db, skip=skip, limit=limit)
    return users





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
