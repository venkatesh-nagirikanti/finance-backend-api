from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.models import User, Record

def check_admin(user_role: str):
    if user_role != "admin":
        return {"error": "Only admin allowed"}

router = APIRouter()

# Dependency (DB connection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create User API
@router.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get("/users")

def get_users(db:Session= Depends(get_db)):
    users=db.query(User).all()

    return users  



@router.post("/records")
def create_record(
    amount: float,
    type: str,
    category: str,
    date: str,
    notes: str,
    user_id: int,
    role:str,
    db: Session = Depends(get_db)
):
    if role != "admin":
        return{"error":"Only admin can create records"}

    new_record = Record(
        amount=amount,
        type=type,
        category=category,
        date=date,

        notes=notes,
        user_id=user_id
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return new_record 

@router.get("/records")
def get_records(
    type: str = None,
    category: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Record)

    if type:
        query = query.filter(Record.type == type)

    if category:
        query = query.filter(Record.category == category)

    records = query.all()
    return records 


@router.get("/dashboard")
def get_dashboard(
    role:str,
    db: Session = Depends(get_db)
): 
    if role not in["admin","analyst"]:
        return {"error":"Not allowed"}

    records = db.query(Record).all()

    total_income = 0
    total_expense = 0

    for record in records:
        if record.type == "income":
            total_income += record.amount
        elif record.type == "expense":
            total_expense += record.amount

    balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }