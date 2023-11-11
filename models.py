from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Goods(Base):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True)
    appellation_good = Column(String)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))
    owner_id = Column(Integer, ForeignKey("owner.id"))

    # owners = relationship("Owner", back_populates="owner")
    category = relationship("Category", back_populates="good")
    owner = relationship("Owner", back_populates="good")


class Owner(Base):
    __tablename__ = "owner"

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    email = Column(String, unique=True)
    # goods_id = Column(Integer, ForeignKey("goods.id"))

    good = relationship("Goods", back_populates="owner")


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    appellation_category = Column(String, unique=True)

    good = relationship("Goods", back_populates="category")
