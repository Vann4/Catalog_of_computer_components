from sqlalchemy.orm import Session

import models


def get_goods(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Goods).offset(skip).limit(limit).all()
