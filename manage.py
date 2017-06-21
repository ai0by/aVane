# coding=utf-8

from aVane import app,db
from flask_script import Manager
from aVane.models import User

manager = Manager(app)

@manager.command
def init_database():
    # 删除所有数据库内容
    db.drop_all()
    # 根据数据库内的定义创建数据
    db.create_all()
    # 生成100个随机用户
    for i in range(0,100):
        db.session.add(User('User'+str(i),'a'+str(i)))
    # 提交操作
    db.session.commit()

if __name__ == '__main__':
    manager.run()