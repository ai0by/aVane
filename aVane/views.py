# coding=utf-8
from aVane import app

@app.route('/')
def index():
    return 'hello'