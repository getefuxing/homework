#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
import  sys

def excess(expression):
    expression = expression.replace("+-","-")
    expression = expression.replace("++", "+")
    expression = expression.replace("-+", "-")
    expression = expression.replace("--", "+")
    return expression

def multiplication_and_division(expression):
    #计算乘除
    number_list = re.split("[*/]",expression)
    symbol_list = re.findall("[*/]", expression)
    result = None
    # if number_list[0].isdigit():
    #     if float(number_list[0]) == 0:
    #         result = 0
    #         return result

    if float(number_list[0]) == 0:
        result = 0
        return result
    else:
        result = None
        for index,i in enumerate(number_list):
            if result:
                if symbol_list[index-1] == "*":
                    if number_list[index] == "0":
                        result = 0
                        return result
                    else:
                        result *= float(i)
                elif symbol_list[index-1] == "/":
                    try:
                        result /= float(i)
                    except:
                        sys.exit("分母不能为0")
            else:
                result = float(i)
    return result



def special(number_list,symbol_list):
    count = 0
    for j in number_list:
        if j.endswith("*") or j.endswith("/"):
            count+=1
    while count:
        for index, i in enumerate(number_list):
            if i.endswith("*") or i.endswith("/"):
                number_list[index] = number_list[index] + symbol_list[index] + number_list[index + 1]
                del number_list[index + 1]
                del symbol_list[index]
        count -= 1
    return number_list,symbol_list


def operation(expression):
    formula = expression.replace(" ", "").strip("()") # 去除括号
    formula = excess(formula)
    number_list = re.split("[+-]",formula)
    symbol_list = re.findall("[-+]", formula)
    if len(number_list[0]) == 0:
        number_list[1] = symbol_list[0] + number_list[1]
        del number_list[0]
        del symbol_list[0]
    number_list,symbol_list = special(number_list,symbol_list)
#    print(number_list,symbol_list)
    for index,i in enumerate(number_list):
        if re.search("[*/]",i):
            res = multiplication_and_division(i)
            number_list[index] = res
    result = float(number_list[0])
    for index,j in enumerate(symbol_list):
        if symbol_list[index] == "+":
            result += float(number_list[index+1])
        elif symbol_list[index] == "-":
            result -= float(number_list[index+1])
    return result



def calculator(expression):
    #运算括号
    flag = True
    while flag:
        bracket = re.search("\([^()]*\)", expression)  # 取第一个括号
        if bracket:
            result = operation(bracket.group())
            expression = expression.replace(bracket.group(),str(result))
        else:
            operation_result = operation(expression)
            flag = False
    return operation_result

if __name__ == "__main__":
    expression = input("please enter your expression:")
    result = calculator(expression)
    print(result)
