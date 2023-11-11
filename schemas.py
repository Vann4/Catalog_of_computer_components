from pydantic import BaseModel


class ProductCategoryBase(BaseModel):
    appellation: str
    goods_id: int


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategory(ProductCategoryBase):
    id: int

    class Config:
        from_attributes = True


class GoodsBase(BaseModel):
    appellation: str


class GoodsCreate(GoodsBase):
    description: str


class Goods(GoodsBase):
    id: int
    category: list[ProductCategory] = []

    class Config:
        from_attributes = True
