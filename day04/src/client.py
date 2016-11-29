#!/usr/bin/env python3
# -*- coding:utf-8 -*-



import os
from conf import baseconf
import sys
import json

USER_AUTH = {"auth":False,"userinfo":None}
PRIMARY_MENU = ["查询","提现","还款","存款","消费记录","账单","退出"]


def inquire():
    pass

def withdrawcash():
    pass

def repayment():
    pass

def deposit():
    pass

def Record():
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


def main():
    for index,item in enumerate(PRIMARY_MENU,1):
        print(index,item)

def run():
    ret = login()
    if ret["auth"]:
        main()
