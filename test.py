# coding=utf-8
import requests
import random
import re
from bs4 import BeautifulSoup


def getQiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print "start:", div.text.strip()


# string常用方法
def string_build():
    aStr = "hello mr.tang";
    print aStr.capitalize();
    print aStr.replace('hello', 'hero');
    bStr = "   go go go   \n\r";
    print bStr;
    print bStr.lstrip();
    print bStr.rstrip();
    print bStr.startswith(' ');
    print bStr.endswith(' ');
    print len(bStr);
    print '-'.join([aStr, bStr]);
    print aStr.split(' ');


# 控制结构
def testFor():
    for i in range(0, 10, 1):
        if i > 4:
            continue;
        print i + 1, '0o0';
        if i > 2:
            pass;


# list
def testList():
    aList = [1, 2, 3];
    print aList;
    bList = ['a', 1, 'b', '1.1', 2.2];
    print bList;
    aList.extend(bList);
    print aList;
    print len(aList);
    print 'a' in bList;
    bList.insert(0, 'ai0by');
    print bList;
    bList.pop(0);
    print bList;
    bList.reverse()
    print bList;
    for i in range(0, 5, 1):
        print bList[i];
    bList.sort();
    print bList;
    # 倒序排序,值为真(1)
    bList.sort(reverse=1);
    print bList;
    print bList * 2;
    print [0] * 10;
    bList.append(1);
    print bList;
    # 带中括号的集合 tuplea
    atuplea = (1, 2, '3');
    print atuplea;


# dict测试开始

def aTestDict(a, b):
    return a - b;


def bTestDict(a, b):
    return a + b;


def testDict():
    aDict = {5: "默认排序", 1: 1, 2: '2', 3: "ai0by"};
    print aDict;
    # print aDict.keys(1); 不能这样写
    print aDict.keys(), aDict.values();
    # print aDict.values(2); 不能这样写
    print aDict.has_key(1), aDict.has_key(4);
    for i, j in aDict.items():
        print "key , value", i, j;
    bDict = {1: aTestDict, 2: bTestDict};
    print bDict[1](2, 3);
    # 字典 1 调用 1 所指向的函数 aTestDict 作减法运算
    print bDict[2](10, 2);
    print bDict;
    # 测试添加一个字典
    bDict['3'] = "ai0by";
    print bDict;
    # 删除一个字典
    bDict.pop('3');
    print bDict;
    # 还可以这样写
    del bDict[2];
    print bDict;


# set测试
def testSet():
    # set构造tuplea
    aSet = set((1, 2, '3'));
    print aSet;
    bSet = set(['1', '2', "ai0by", '4']);
    # print aSet + bSet; 不可以相加
    aSet.add('4');
    print aSet;
    # 他们的交集
    print aSet.intersection(bSet);
    # 并集
    print aSet.union(bSet);
    # 相减
    print aSet - bSet;


# 测试一个对象
class User:
    type = "user";
    def __init__(self,name,uid):
        self.name = name;
        self.uid = uid;

    def __repr__(self):
        return "i'm" + " " + self.name+" "+str(self.uid);
# 继承一个对象
class Admin(User):
    type = "Admin";
    def __init__(self,name,uid,group):
        User.__init__(self,name,uid)
        self.group = group;
    def __repr__(self):
        return "i'm" + " " + self.name + " "+str(self.uid) + " " + self.group;

# 多态的实践
def testCreatUser(type):
    if type == "User":
        return User("ai0by",1);
    elif type == "Admin":
        return Admin("ai0by",1,"AdminGroup");
    else:raise ValueError("error!");

# 异常处理程序
def testCatch():
    try:
        # print 2/0;
        raise Exception("raise error","ai0by");
    except Exception as e:
        print "error",e;
    finally:
        print "start program";

# 随机数库测试
def testRandom():
    # 死随机,种子固定
    # random.seed(1);
    # 正常随机数
    print int(random.random()*100);
    print random.random();
    print random.randint(0,1000);
    print random.choice([1,2,3,4,5,0,0,0,0,0,0,0,0]);
    print random.sample(range(0,100),4);
    testA = [1,2,5,3,4];
    random.shuffle(testA);
    print testA;

# 正则表达式
def testRe():
    aStr = "1ab376vasd9a89dw";
    # 测试数字
    aTest = re.compile("[\d]+");    # 使用「+」号多次匹配
    bTest = re.compile("\d");
    print aTest.findall(aStr);
    print bTest.findall(aStr);
    bStr = "a@163.com;b@163.com;c@qq.com;4@biyeai.com;e@hkzn.cn";
    cTest = re.compile("[\w]+@[163|qq|hkzn]+\.[com|cn]+");
    print cTest.findall(bStr);
    cStr = "ldkajkga2017-03-27kjgahksjdha";
    dTest = re.compile("\d{4}-\d{2}-\d{2}")
    print dTest.findall(cStr);


# 主函数开始
if __name__ == '__main__':
    print("hello world");
    # getQiushibaike();
    # string_build();
    # testFor();
    # testList();
    # testDict();
    # testSet();
    # User1 = User("ai0by",01);
    # print User1;
    # Admin1 = Admin("ai0by",01,"AdminGroup");
    # print Admin1;
    # print testCreatUser("Guest");
    # testCatch();
    # testRandom();
    # testRe();
