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



s = "print(123)"
#编译 single:变异成单行,exec:变异成python的,eval:变成表达式
r = compile(s,"<string>","exec")

print(r)
#执行
exec(r)
