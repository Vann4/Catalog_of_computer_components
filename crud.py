from sqlalchemy.orm import Session

import models, schemas


def get_goods(db: Session):
    return db.query(models.Goods).all()


def create_good(db: Session, good: schemas.GoodsCreate):
    db_good = models.Goods(appellation_good=good.appellation_good, description=good.description, category_id=good.category_id, owner_id=good.owner_id)
    db.add(db_good)
    db.commit()
    db.refresh(db_good)
    return db_good


def get_category(db: Session):
    return db.query(models.Category).all()


# def get_category_by_appellation(db: Session, appellation: str):
#     return db.query(models.Category).filter(models.Category.appellation == appellation).first()


# def create_category(db: Session, category: schemas.CategoryCreate):
#     db_category = models.Category(appellation=category.appellation)
#     db.add(db_category)
#     db.commit()
#     db.refresh(db_category)
#     return db_category


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
