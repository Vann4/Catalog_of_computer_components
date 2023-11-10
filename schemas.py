# from pydantic import BaseModel
#
#
# class TypesOfGoodsBase(BaseModel):
#     title: str
#     description: str | None = None
#
#
# class TypesOfGoodsCreate(TypesOfGoodsBase):
#     pass
#
#
# class TypesOfGoods(TypesOfGoodsBase):
#     id: int
#     appellation: str
#
#     class Config:
#         from_attributes = True
#
#
# class GoodsBase(BaseModel):
#     appellation: str
#
#
# class GoodsCreate(GoodsBase):
#     appellation: str
#
#
# class Goods(GoodsBase):
#     id: int
#     items: list[TypesOfGoods] = []
#
#     class Config:
#         from_attributes = True


from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        from_attributes = True
