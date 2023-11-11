from sqlalchemy.orm import Session

import models, schemas


def get_goods(db: Session):
    return db.query(models.Goods).all()


def get_category(db: Session):
    return db.query(models.Category).all()


def get_owners(db: Session):
    return db.query(models.Owner).all()


def get_owner_by_email(db: Session, email: str):
    return db.query(models.Owner).filter(models.Owner.email == email).first()


def create_owner(db: Session, owner: schemas.OwnerCreate):
    db_owner = models.Owner(surname=owner.surname, name=owner.name, patronymic=owner.patronymic, email=owner.email)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner
