#-*-coding:utf-8-*-
from app import db

class Basemodel():
    is_delete = db.Column(db.BOOLEAN())



class Contactor(db.Model,Basemodel):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20))
    middlename = db.Column(db.String(20),nullable=True)
    lastname = db.Column(db.String(20))
    nickname = db.Column(db.String(20),nullable=True)
    otherphone = db.Column(db.String(12))
    email = db.Column(db.String(40))
    contact_id =  db.Column(db.String(200),nullable=True)

