from sqlalchemy import Column, Integer, String 
from sqlalchemy import Column, Integer, String, Float
from database.db import Base 

class User(Base): 
    __tablename__ = "users"
    id = Column(Integer,primary_key = True,index= True)
    name = Column(String)
    email = Column(String, unique = True, index = True) 
    role = Column(String,default="viewer") # admin / analyst/viewers 

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    type = Column(String)  # income / expense
    category = Column(String)
    date = Column(String)
    notes = Column(String)

    user_id = Column(Integer)