#-*- encoding=UTF-8 -*-

from flask import Flask,render_template,request
# 引入Flask框架

# 装饰器
def log(leavel,*args,**kvargs):
    def inner(fun):
        # 装饰器的定义
        def wrapper(*args,**kvargs):
            # 打印装饰器等级
            print leavel,"Start:",fun.__name__
            fun(*args,**kvargs)
            # 使用*args和**kvargs代表引用的函数的参数,可变参数
            print "args",args,"kvargs",kvargs
            # *args代表无名子的参数,**kvargs代表有名字的参数,可以一起使用
            print "End:",fun.__name__
        return wrapper
    return inner

# 装饰器的引用,分等级的log,装饰器参数
@log(leavel="INFO")
def hello(myName,myCode,myUid):
    print "hello",myName,myCode,myUid
    print "nmb"


# 初始化Flask
app = Flask(__name__)
# 使用jinja的模板语法,让#号之后的语句变更为Jinja语法
app.jinja_env.line_statement_prefix="#"
# 如果访问的地址为"/",那么就用index函数来处理,映射功能
@app.route('/')
def index():
    return "hello world"

# 路径中带入参数,并将变量参数强制转换类型为int,在后面加入/可以自动补齐,且更加保守,推荐
@app.route('/profile/<int:uid>/',methods=["get","post"])
def profile(uid):
    # 必须强制转换为str在输出,因为默认的uid是int类型的
    # 定义了一个tuplea,名为colors
    colors = ("red","green")
    me = {"name":"tang","num":91}
    return render_template("profile.html",uid=uid,colors=colors,me=me)

# 测试一个request的简单调用
@app.route('/request')
def testRequest():
    # 将res设置为,get传参,当不传递任何参数时,默认是defaultkey
    res = request.args.get("key","defaultkey") + "<br>"
    # 将res增加,地址显示和path
    res = request.url + " <br>" + request.path + "<br>"
    for i in dir(request):
        # 将res增加,request的内容和属性
        res = res + str(i) + "<br>"+str(eval("request."+i)) + "<br>"
    return res


if __name__ =='__main__':
    # hello("ai0by",12345,myUid=001);
    app.run(debug=True)
