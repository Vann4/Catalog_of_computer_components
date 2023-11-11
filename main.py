from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/goods/", response_model=list[schemas.Goods])
def get_goods(db: Session = Depends(get_db)):
    goods = crud.get_goods(db)
    return goods


@app.get("/category/", response_model=list[schemas.Category])
def get_category(db: Session = Depends(get_db)):
    category = crud.get_category(db)
    return category


@app.get("/owners/", response_model=list[schemas.Owner])
def get_owners(db: Session = Depends(get_db)):
    owners = crud.get_owners(db)
    return owners


@app.post("/owner/", response_model=schemas.Owner)
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    db_user = crud.get_owner_by_email(db, email=owner.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Человек с такой почтой уже зарегистрирован")
    return crud.create_owner(db=db, owner=owner)
