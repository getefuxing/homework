#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import commons

def run():
    inp = input("please enter:")
#    if inp == "loggin":
#        commons.loggin()
#    elif inp == "loggout":
#        commons.loggout()
#    elif inp == "home":
#        commons.home()
#    else:
#        print("404")
#delattr()
#setattr()
    if hasattr(commons,inp):
        func = getattr(commons,inp)
        func()


run()

obj = __import__("xxx",fromlist=True)

