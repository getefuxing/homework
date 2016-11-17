#!/usr/bin/env python3
# -*- coding:utf-8 -*-



#普通参数
#指定参数
#默认参数
#动态参数
#万能参数

#str.format() 格式化输出


#s1 = "i am {0},age {1}".format("alex",18)
#s2 = "i am {0},age {1}".format(*["alex",18])
#print(s1,s2)

#s3 = "i am {name},age {age}".format(name='alex',age=10)

#print(s3)

#dic = {'name':'alex','age':10}

#s4 = "i am {name},age {age}".format(**dic)

#print(s4)


'''
def f1(a1,a2):
    return a1 + a2

def f1(a1,a2):
    return a1 * a2


ret = f1(8,8)

print(ret)

'''


'''
#特殊：列表，字典 可以修改  无法重新赋值
# 全局变量都是大写

name = 'jack'

def f1():
    global name
    name = 'alex'
    print(name)


def f2():
    print(name)


f1()
f2()


#三元运算 和三目运算

name = 'alex' if 2 == 1 else 'SB'
print(name)


m2 = lambda a1:a1 + 100

print(m2)
'''

#abs()   绝对值
#any()   只有有真就为真
#all()   所有为真 才为真
'''
n = all([1,2,3,0])
print(n)

m = any([0,0,0])

print(m)
'''

#bin()
#oct()
#hex()


# usf-8 一个汉字3个字节
#gbk  一个汉字2个字节
#一个字节是8位
'''
#字符串 转化字节类型 用bytes
s = "李杰"
n = bytes(s,encoding="utf-8")
print(n)

n = bytes(s,encoding="gbk")
print(n)


#字节转化字符串

new_str = str(bytes("李杰",encoding="utf-8"),encoding="utf-8")

print(new_str)


f = open('haproxy.cfg','r')
f.seek(1)

'''

#ascii转化关系
#chr()
#ord()
'''
n = chr(65)

print(n)

m = ord('A')
print(m)
'''

'''
import random
li = []
for i in range(6):
    i = random.randrange(0,5)
    if i == 2 or i == 4:
        num = random.randrange(0,10)
        li.append(str(num))
    else:
        tem = random.randrange(65,91)
        c = chr(tem)
        li.append(c)
result = "".join(li)

print(result)
'''


#compile()
#eval()
#exec()


'''
s = "print(123)"
#编译 single:变异成单行,exec:变异成python的，没有返回值，接收代码或字符串,eval:变成表达式，专门用来处理表达式，有返回值
r = compile(s,"<string>","exec")

print(r)
#执行
exec(r)
'''



#反射:delattr(),getattr(),hasattr()

#print(dir(dict)) 查询对象提供的功能


# print(divmod(97,10)) 求商和余数

# 对象和类
#对象是类的实例


'''
#用于判断是否是某个对象的实例
s = 'str'
r = isinstance(s,list)

print(r)


'''



#filter,map


#filter(函数，可迭代对象)

'''
li = [1,2,3,4,5]
ret = filter(lambda a :a +100,li)

print(list(ret))

'''

'''
li = [1,2,3,4,5]
ret = map(lambda a :a +100,li)

print(list(ret))

zip()

'''

#必须会的  bytes



# 装饰器
#开放封闭原则,函数内部不允许修改
'''
def outer(func):
    def inner():
        print("log")
        return func()
    return inner

#@ + 函数名
#功能
#   1.自动执行outer函数，并且将下面的函数当错参数传递outer
#   2.将outer函数的返回值，重新复制给f1
@outer
def f1():
    print("f1")

@outer
def f2():
    print("f2")


f1()


#定义函数，为调用，函数内部不执行
#函数名 > 代指函数
#函数没写return 返回none
'''



'''
def outer(func):
    def inner(*args,**kwargs):
        print("log")
        r =  func(*args,**kwargs)
        return r
    return inner

@outer
def f1(arg):
    print(arg)
    return "aa"

@outer
def f2(a1,a2):
    print(a1,a2)
    return "aa"

f1(1)
'''


#装饰器可以广泛的运用用户的认证
'''
LOGIN_USER = { "is_login":False}

def outer(func):
    def inner(*args,**kwargs):
        if LOGIN_USER["is_logon"]:
            r =  func(*args,**kwargs)
            return r
        else:
            print("请登陆")
    return inner

@outer
def order(arg):
    print("欢迎登陆")

 '''


'''
#多个装饰器，多装饰器是重下往上使用的

USER_INFO = {}

def check_login(func):
    def inner(*args,**kwargs):
        if USER_INFO.get('is_login',None):
            ret = func(*args,**kwargs)
            return ret
        else:
            print("请登陆")
    return  inner



def check_admin(func):
    def inner(*args,**kwargs):
        if USER_INFO.get('user_type',None) == 2:
            ret = func(*args,**kwargs)
            return ret
        else:
            print("aa")
    return  inner


@check_login
@check_admin
def index():
    print("index")



def home():
    print("home")


def login():
    user = input("请输入:")
    if user == "admin":
        USER_INFO["is"]




def main():
    inp = input("1.登陆:2.查看:3.超级管理员:")

    if inp == "1":
        login()
    elif inp == "2":
        home()
    elif inp == "3":
        index()

'''

'''
s = "-----{0}___{0}-----{1}".format(123,"alex")

print(s)

#填充，居中，% 特殊


tpl = "i am {}, age {}, {}".format("seven", 18, 'alex')

tpl = "i am {}, age {}, {}".format(*["seven", 18, 'alex'])

tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18)

tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})


'''

'''
#生成器，使用函数创造,有yied

def myrange(arg):
    start = 0
    while True:
        if start >= arg:
            return
        yield  start
        start += 1

ret = myrange(3)

print(ret)

for item in ret:
    print(item)


for item in range(10):
    print(item)

'''
'''
def fun(n):
    n += 1
    if n >= 4:
        return "end"
    return fun(n)

r = fun(0)
print(r)

 '''
#序列化和反序列化
'''
import json

dic = '{"k1":"v1"}'

result = json.loads(dic)
print(result)
'''


#json 里面要用双引号
'''
import  requests
import json

response = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=上海")

response.encoding = "utf-8"


ret = json.loads(response.text)

print(ret,type(ret))
'''



#json.loads ,json.load, json.dump,json,dumps

#json.dump 先序列化，在把字符写入文件

#json.load


#json适合跨语音  pickle适合python的复杂类型



#time最常用取时间戳   datetime 最常用取日期
import time
import  datetime


'''
time.time()
time.ctime()
time.gmtime()
time.mktime()
time.strftime("%Y-%m-%d",time.gmtime())

time.strptime("2016-05-06","%Y-%m-%d")
 '''

'''
current_time = datetime.datetime.now()
print(current_time + datetime.timedelta(days=10))
print(current_time)

'''

'''
import logging


logging.basicConfig(filename="example",level=logging.INFO,
                    format="%(asctime)s %(message)s",datefmt="%Y-%m-%d %I:%M:%S %a")
logging.warning("user")
logging.critical("server is down")
 '''

'''

#递归1*2*3..7

def func(num):
    if num == 1:
        return 1
    return num * func(num - 1)

print(func(4))
 '''
#反射

#反射就是利用字符串的形式去对象（默认）中操作（寻找）成员

'''
import  os

os.path.abspath()  #绝对路径
os.path.dirname() #上级目录
'''


'''
print(__file__)

import  sys
print(sys.platform)

def view_bar(num,totle):
    rate = num/totle
    rate_num = int(rate * 100)
    r = "\r%s> %d%%" % ("=" *num,rate_num)
    sys.stdout.write(r)
    sys.stdout.flush()


for i in range(0,101):
    view_bar(i,100)
    time.sleep(0.4)
'''

#去已经提取到的数据中在提取数据

import re
a = "1 + ((2+3) * 5 * (9-4)) / (5 + 5)"

r1 = re.split("\(([^()]*)\)",a)

r2 = re.search("\([^()]*\)", a)

r5 = r2.group().strip("()")

print(r1,r5)


b = " - 1 * 5 + 7 * 8 / 2"

print(eval(r5))

pattern = "\(([\+\*/\-0-9]+)\)"

r3 = re.split(pattern,a)
print(r3)