from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Goods(Base):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True)
    appellation = Column(String)
    description = Column(String)

    # owners = relationship("Owner", back_populates="owner")
    # category = relationship("ProductCategory", back_populates="goods")


class Owner(Base):
    __tablename__ = "owner"

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    email = Column(String, unique=True)
    # goods_id = Column(Integer, ForeignKey("goods.id"))

    # owner = relationship("Goods", back_populates="owners")


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    appellation = Column(String, unique=True)


# class ProductAndCategory(Base):
#     __tablename__ = "productCategory"
#
#     id = Column(Integer, primary_key=True)
#     appellation = Column(String, unique=True)

