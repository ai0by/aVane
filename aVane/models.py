# coding=utf-8
from aVane import db

# 定义用户
class User(db.Model):
    # 定义它的数据及相关类型
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(80),unique=True)
    password = db.Column(db.String(32))
    head_url = db.Column(db.String(256))
    # 定义这个类的构造函数,分别赋初始值
    def __init__(self,Username,Password):
        self.username = Username
        self.password = Password
        self.headurl = '/static/default.jpg'
    # 显示用户信息
    def __repr__(self):
        return '<User %d %s>' % (self.id,self.username)