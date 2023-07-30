from typing import List, Union

from pydantic import BaseModel

class UserBase(BaseModel):
    ho_ten_nhan_su: str
    don_vi: str
    so_the: str
    link_fb_nhan_vien: str
    luot_thich:str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True




class updateUserBase(BaseModel):
    thoi_gian: str
    status: str


class updateUser(updateUserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True



class UpdatePost(BaseModel):
    ho_ten_nhan_su: str
    luot_thich_thay: str

    class Config:
        orm_mode = True


class UpdateTime(BaseModel):
    thoi_gian: str
    thoi_gian_thay: str

    class Config:
        orm_mode = True

class DeleteTime(BaseModel):
    thoi_gian: str

    class Config:
        orm_mode = True











