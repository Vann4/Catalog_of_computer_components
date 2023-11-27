from pydantic import BaseModel


class ProductCharacteristicBase(BaseModel):
    characteristic_name: str
    characteristic: str


class ProductCharacteristicCreate(ProductCharacteristicBase):
    goods_id: int
    characteristic_name: str
    characteristic: str


class ProductCharacteristic(ProductCharacteristicBase):
    id: int
    goods_id: int
    characteristic_name: str
    characteristic: str

    class Config:
        from_attributes = True


class GoodsBase(BaseModel):
    appellation_good: str
    description: str


class GoodsCreate(GoodsBase):
    appellation_good: str
    description: str
    category_id: int
    owner_id: int


class Goods(GoodsBase):
    id: int
    category_id: int
    owner_id: int
    characteristic: list[ProductCharacteristic] = []

    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    appellation_category: str


class CategoryCreate(CategoryBase):
    appellation_category: str


class Category(CategoryBase):
    id: int
    appellation_category: str
    good: list[Goods] = []

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
    owners: list[Goods]

    class Config:
        from_attributes = True
