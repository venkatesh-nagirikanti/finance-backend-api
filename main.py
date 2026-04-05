from fastapi import FastAPI
from models import models
from routes.user_routes import router 
from database.db import engine,Base

app = FastAPI()

app.include_router(router)

Base.metadata.create_all(bind=engine)
@app.get("/")
def read_root():
    return {"message": "Finance Backend is running"}