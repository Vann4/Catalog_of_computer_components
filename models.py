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

    category = relationship("Category", back_populates="good")
    owner = relationship("Owner", back_populates="owners")
    characteristic = relationship("ProductCharacteristic", back_populates="characteristics")


class Owner(Base):
    __tablename__ = "owner"

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    email = Column(String, unique=True)
    # goods_id = Column(Integer, ForeignKey("goods.id"))

    owners = relationship("Goods", back_populates="owner")


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    appellation_category = Column(String, unique=True)

    good = relationship("Goods", back_populates="category")


class ProductCharacteristic(Base):
    __tablename__ = "product_characteristics"

    id = Column(Integer, primary_key=True)
    goods_id = Column(Integer, ForeignKey("goods.id"))
    characteristic_name = Column(String)
    characteristic = Column(String)

    characteristics = relationship("Goods", back_populates="characteristic")
