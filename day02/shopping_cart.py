#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import sys
import time

with open('shopping_history.txt') as h:
    shopping_history  = json.load(h)


with open('commodity.txt') as c:
    commodity_info  = json.load(c)

commodity_list=[]
for commodity in commodity_info:
    commodity_list.append(commodity)

with open('account.txt') as u:
    user_info = json.load(u)

user_list = []
for user in user_info:
    user_list.append(user)


infomation_list = ["商品信息","用户信息","充值","历史信息","退出"]
shopping_cart = []


#用户登陆
count = 3
while count > 0:
    username = input("name:")
    lock_check = open('lock.txt','r')
    for line in lock_check:
        line = line.strip('\n')
        if username == line:
            print("your name is loacked")
            sys.exit(0)
    lock_check.close()
    password = input("password:")
    match_flag = False
    if username in user_list and password == user_info[username][0]:
        print("Welcom %s  to the shopping mall ！" %username)
        match_flag = True
        break
    if match_flag == False:
        print ('username or password is wrong')
        count =count - 1
else:
    print ('your name is locked!')
    f = open('lock.txt','a')
    f.write("".join(username)+"\n")
    f.close()
    sys.exit()


balance = user_info[username][1]
flag = False
#购物
while not flag:
    for index in enumerate(infomation_list):
        number = index[0]
        info = index[1]
        print(number,info)
    user_choice = input("[q] is quit,please enter your choice:")
    if user_choice == '0':
        while not flag:
            print("list".center(50, '-'))
            for item in enumerate(commodity_list):
                index = item[0]
                type_name = item[1]
                print(index, type_name)
            type_chioce = input("[q] is quit,[b] is back,what do you want to buy:")
            if type_chioce.isdigit():
                type_chioce = int(type_chioce)
                if type_chioce < len(commodity_list) and type_chioce >= 0:
                    while not flag:
                        print("list".center(50, '*'))

                        for x in enumerate(commodity_info[commodity_list[type_chioce]]):
                            number = x[0]
                            goods = x[1][0]
                            price = x[1][1]
                            total = x[1][2]
                            print(number,goods,price,total)
                        commodity_choice = input("[q] is quit,[b] is back,please enter you choice:")
                        if commodity_choice.isdigit():
                            commodity_choice = int(commodity_choice)
                            if commodity_choice < len(commodity_info[commodity_list[type_chioce]]) and commodity_choice >= 0:
                                value = commodity_info[commodity_list[type_chioce]][commodity_choice][2]
                                shop = commodity_info[commodity_list[type_chioce]][commodity_choice]
                                amount = input("how many want to buy:")
                                if amount.isdigit():
                                    amount = int(amount)
                                    if amount < value:
                                        commodity_amount = shop[1] * amount
                                        shopping_list = [shop[0],amount,commodity_amount]
                                        if commodity_amount <= balance:
                                            shopping_cart.append(shopping_list)
                                            balance = balance - commodity_amount
                                            value = value - amount
                                            shop[2] = value

                                            print(" ".center(50, '*'))
                                            print(" Add %s into shop car,you current balance  is %s " %(shop,balance))
                                        else:
                                            print("Your balance is %s,can not afford this..." %(balance,))
                                    else:
                                        print("quantity is not enough，please choice other or buy litter")
                                        continue
                                else:
                                    print("enter an vaild number")
                                    continue
                        else:
                            if commodity_choice == "b":
                                break

                            elif type_chioce == "c":
                                for item in shopping_cart:
                                    print("commodity:%s,number:%s,amount:%s" %(item[0],item[1],item[2]))

                            elif commodity_choice == "q":

                                for item in shopping_cart:
                                    print("commodity:%s,number:%s,amount:%s" %(item[0],item[1],item[2]))
                                user_info[username][1] = balance
                                with open('account.txt', 'w') as u:
                                    json.dump(user_info, u,ensure_ascii=False)

                                with open('commodity.txt','w') as c:
                                    json.dump(commodity_info,c,ensure_ascii=False)

                                shopping_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

                                history_list = shopping_history[username]
                                history = {shopping_time: shopping_cart}
                                history_list.append(history)
                                shopping_history[username] = history_list
                                with open('shopping_history.txt', 'w') as s:
                                    json.dump(shopping_history,s,ensure_ascii=False)

                                flag = True
                                print("Look forward to seeing you next time")
                            else:
                                print("enter an vaild number!")
                                continue
            else:
                if type_chioce == "b":
                    break
                elif type_chioce == "c":
                    for item in shopping_cart:
                        print("commodity:%s,number:%s,amount:%s" %(item[0],item[1],item[2]))
                elif type_chioce == "q":
                    for item in shopping_cart:
                        print("commodity:%s,number:%s,amount:%s" %(item[0],item[1],item[2]))
                    user_info[username][1] = balance
                    with open('account.txt','w') as u:
                        json.dump(user_info,u,ensure_ascii=False)


                    with open('commodity.txt', 'w') as c:
                        json.dump(commodity_info, c,ensure_ascii=False)

                    shopping_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    history_list = shopping_history[username]
                    history = {shopping_time: shopping_cart}
                    history_list.append(history)
                    shopping_history[username] = history_list
                    with open('shopping_history.txt', 'w') as s:
                        json.dump(shopping_history, s, ensure_ascii=False)

                    flag = True
                    print("Look forward to seeing you next time")
                else:
                    print("enter an vaild number!")
                    continue

    elif user_choice == '1':
        print("username=%s,password=%s,balance=%s" %(username,password,balance))

    elif user_choice == '2':
        while True:
            recharge = input("[b] is back,please enter the amount of recharge:")
            if recharge.isdigit():
                balance = balance + int(recharge)
                print("充值成功！")
            else:
                if recharge == 'b':
                    break
                else:
                    print("enter an vaild number!")

    elif user_choice == '3':
        for item in shopping_history[username]:
            print(item)

    elif user_choice == 'q' or user_choice == '4':
        user_info[username][1] = balance
        with open('account.txt', 'w') as u:
            json.dump(user_info, u, ensure_ascii=False)
        with open('commodity.txt', 'w') as c:
            json.dump(commodity_info, c, ensure_ascii=False)

        shopping_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        history_list = shopping_history[username]
        history = {shopping_time: shopping_cart}
        history_list.append(history)
        shopping_history[username] = history_list
        with open('shopping_history.txt', 'w') as s:
            json.dump(shopping_history, s, ensure_ascii=False)
        print("Look forward to seeing you next time")

        flag = True
    else:
        print("enter an vaild number!")
        continue
