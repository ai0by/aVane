# coding=utf-8
from aVane import db
from datetime import datetime

# 定义评论
class Comment(db.model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.String(2048))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    image_id = db.Column(db.Integer,db.ForeignKey('image.id'))
    status = db.Column(db.Integer,default=0)# 判断该评论是否被删除,不在数据库中物理删除,默认0不删除


# 定义图片
class Image(db.model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    url = db.Column(db.String(512))
    create_date = db.Column(db.DateTime)
    comment = db.relationship('Comment')

    def __init__(self,Url,User_id):
        self.url = Url
        self.user_id = User_id
        self.create_date = datetime.now()

    def __repr__(self):
        return '<Image %d %d %s %s>' % (self.id,self.user_id,self.url,self.create_date)

# 定义用户
class User(db.Model):
    # 定义它的数据及相关类型
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(80),unique=True)
    password = db.Column(db.String(32))
    head_url = db.Column(db.String(256))
    images = db.relationship('Image')
    comment = db.relationship('Comment')
    # 定义这个类的构造函数,分别赋初始值
    def __init__(self,Username,Password):
        self.username = Username
        self.password = Password
        self.headurl = '/static/default.jpg'
    # 显示用户信息
    def __repr__(self):
        return '<User %d %s>' % (self.id,self.username)