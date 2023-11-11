from pydantic import BaseModel


class CategoryBase(BaseModel):
    appellation: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    appellation: str

    class Config:
        from_attributes = True


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
    appellation: str


class GoodsCreate(GoodsBase):
    description: str


class Goods(GoodsBase):
    id: int

    class Config:
        from_attributes = True
