from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    ho_ten_nhan_su = Column(String, unique=True, index=True)
    don_vi = Column(String)
    so_the= Column(String)
    link_fb_nhan_vien= Column(String)
    luot_thich=Column(String)
    is_active = Column(Boolean, default=True)




class updateUser(Base):
    __tablename__ = "update"

    id = Column(Integer, primary_key=True, index=True)
    thoi_gian = Column(String, unique=True, index=True)
    status = Column(String)
    is_active = Column(Boolean, default=True)




