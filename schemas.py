from pydantic import BaseModel


class OwnerBase(BaseModel):
    surname: str
    name: str


class OwnerCreate(OwnerBase):
    surname: str
    name: str
    patronymic: str
    email: str


class Owner(OwnerBase):
    patronymic: str
    email: str
    id: int

    class Config:
        from_attributes = True


class GoodsBase(BaseModel):
    appellation_good: str


class GoodsCreate(GoodsBase):
    appellation_good: str
    description: str
    category_id: int
    owner_id: int


class Goods(GoodsBase):
    id: int
    category_id: int
    owner_id: int

    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    appellation_category: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    appellation_category: str
    good: list[Goods] = []

    class Config:
        from_attributes = True
