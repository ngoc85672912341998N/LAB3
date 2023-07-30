from sqlalchemy.orm import Session
from sqlalchemy import update

from . import models, schemas

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.ho_ten_nhan_su == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.User):
    ho_ten_nhan_su = user.ho_ten_nhan_su
    db_user = models.User(ho_ten_nhan_su=ho_ten_nhan_su, don_vi=user.don_vi,so_the=user.so_the,link_fb_nhan_vien=user.link_fb_nhan_vien,luot_thich=user.luot_thich)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_mutiple_user(db: Session, user: schemas.User):
    ho_ten_nhan_su = user.ho_ten_nhan_su.split(",")
    don_vi=user.don_vi.split(",")
    so_the=user.so_the.split(",")
    link_fb_nhan_vien=user.link_fb_nhan_vien.split(",")
    luot_thich=user.luot_thich.split(",")
    i=0
    for ho_ten_nhan_su in ho_ten_nhan_su:
        db_user = models.User(ho_ten_nhan_su=ho_ten_nhan_su, don_vi=don_vi[i],so_the=so_the[i],
                              link_fb_nhan_vien=link_fb_nhan_vien[i],luot_thich=luot_thich[i])
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        i=i+1
    return db_user


def get_update_user11(db: Session, user: schemas.UpdatePost):
    print("update")
    update_query = {models.User.luot_thich: user.luot_thich_thay}
    print(user.luot_thich_thay)
    db.query(models.User).filter_by(ho_ten_nhan_su=user.ho_ten_nhan_su).update(update_query)
    db.commit()
    return "success"


def get_update_time_user11(db: Session, user: schemas.UpdateTime):
    print("update")
    update_query = {models.updateUser.thoi_gian: user.thoi_gian}
    print(user.thoi_gian_thay)
    db.query(models.updateUser).filter_by(thoi_gian=user.thoi_gian).update(update_query)
    db.commit()
    return "success"


def get_delete_time_user11(db: Session, user: schemas.DeleteTime):
    print("update")
    post = db.query(models.updateUser).filter_by(thoi_gian=user.thoi_gian).all()
    db.query(models.updateUser).filter_by(thoi_gian=user.thoi_gian).delete()
    db.commit()
    return "success"






#########################################################################
# def get_update_user(db: Session, user_id: int):
#     return db.query(models.updateUser).filter(models.updateUser.id == user_id).first()


def get_update_user_by_email(db: Session, thoi_gian: str):
    return db.query(models.updateUser).filter(models.updateUser.thoi_gian == thoi_gian).first()


def get_update_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.updateUser).offset(skip).limit(limit).all()


def create_update_user(db: Session, user: schemas.updateUser):
    thoi_gian = user.thoi_gian
    print(thoi_gian)
    db_user = models.updateUser(thoi_gian=thoi_gian, status=user.status)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


