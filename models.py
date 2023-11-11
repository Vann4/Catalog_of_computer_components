from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Goods(Base):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True)
    appellation = Column(String)
    description = Column(String)

    category = relationship("ProductCategory", back_populates="goods")


class ProductCategory(Base):
    __tablename__ = "productCategory"

    id = Column(Integer, primary_key=True)
    appellation = Column(String, unique=True)
    goods_id = Column(Integer, ForeignKey("goods.id"))

    goods = relationship("Goods", back_populates="category")
