#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import re

def find_brackets(arg):
    content = re.search("\([^()]*\)", arg)
    if not content:
        result = eval(arg)
    else:
        content = content.strip("()")
        result = eval(content)
        new_arg = arg.replace(content,str(result))

    return result

a = "1 + 3 * (-3 + 2) + 2 * ( 3 + 2 ) "

print(eval(a))


