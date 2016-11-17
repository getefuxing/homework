#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
a = "- 1 * 4 / 2 + 3 * 4"
b = " -0 * 4 / 2"
c = "((1+2) *3 + 4) * ( 3 + 4 )"
d = "- 0.1 * 4 / 2 + 3 * -4"


b = b.replace(" ","")


r1 = re.split("[*/+-]",b)
r2 = re.findall("[*/]",b)
print(r1,r2)
print("0" in r1)



def multiplication_and_division(expression):
    #计算乘除

    number_list = re.split("[*/]",expression)
    symbol_list = re.findall("[*/]", expression)

    list = re.split("[*/+-]",expression)
    if "0" in list:
        return  0

    else:
        result = None
        for index,i in enumerate(number_list):
            if result:
                if symbol_list[index-1] == "*":
                    result *= float(i)
                elif symbol_list[index-1] == "/":
                    result /= float(i)
            else:
                result = float(i)
    return result

def operation(expression):
    b = b.replace(" ", "")
    number_list = re.split("[+-]",expression)
    symbol_list = re.findall("[-+]", expression)
    print(number_list,symbol_list)


#print(operation(c))

print(multiplication_and_division(b))

def calc(expression):
    pass


