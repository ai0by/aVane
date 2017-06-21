# coding=utf-8

from flask import Flask
# 初始化Flask
from flask_sqlalchemy import SQLAlchemy
# 导入SQLAlchemy


app = Flask(__name__)
# 配置文件在这里
app.config.from_pyfile('app.conf')
db = SQLAlchemy(app)

from aVane import views,models