#-*- encoding=UTF-8 -*-
# 装饰器
def log(fun):
    def wrapper(*args,**kvargs):
        print "Start:",fun.__name__;
        fun(*args,**kvargs);
        print "End:",fun.__name__;
    return wrapper;

@log
def hello(myName,myCode,myUid):
    print "hello",myName,myCode,myUid;
    print "nmb";

if __name__ =='__main__':
    hello("ai0by",12345,myUid=001);

