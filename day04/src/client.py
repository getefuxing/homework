#!/usr/bin/env python3
# -*- coding:utf-8 -*-



import os
from conf import baseconf
import sys
import json

USER_AUTH = {"auth":False,"userinfo":None}
def login_required(func):
    def wrapper(*args,**kwargs):
        if USER_AUTH.get('auth'):
            return func(*args,**kwargs)
        else:
            exit("User is not authenticated.")
    return wrapper


@login_required
def inquire(user_data):
    print("aa")


def withdrawcash():
    pass

def repayment():
    pass

def deposit():
    pass

def Record():
    pass

def quit():
    pass


def login():
    count = 3
    flag = False
    cardnumber = input("please enter your cardnumber:")
    user_dir = os.path.join(baseconf.DB_PATH,"client",cardnumber)
    user_file = os.path.join(user_dir,"userinfo")
    if not os.path.exists(user_dir):
        sys.exit("user is not exist")
    else:
        with open(user_file, 'r') as f:
            user_info = json.load(f)
        while count > 0:
            passwd = input("please enter your password:")
            if user_info["status"] == "1":
                sys.exit("please contact administrator")
            elif user_info["status"] == "2":
                if cardnumber == user_info["cardnumber"] and passwd == user_info["password"]:
                    USER_AUTH["userinfo"] = user_info
                    USER_AUTH["auth"] =True
                    flag = True
                    break
                if flag == False:
                    count -= 1
                    print("please check your cardnumber or password! you have %s chance",count)
        else:
            user_info["status"] = "1"
            with open(user_file,"w") as f :
                json.dump(user_info,f)
    return USER_AUTH


@login_required
def main(user_data):
    print('''
1.查询
2.取款
3.还款
4.存款
6.账单
7.退出''')
    primary_menu_dict = {"1":inquire}
    flag = False
    while not flag:
        user_option = input(">>:").strip()
        if user_option in primary_menu_dict:
            primary_menu_dict[user_option](user_data)
        else:
            print("Option does not exist!")

def run():
    ret = login()
    if ret["auth"]:
        user_data= USER_AUTH["userinfo"]
        main(user_data)


run()