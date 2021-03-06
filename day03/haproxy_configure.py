#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import shutil
import json
import os

import sys

haproxy_file = 'haproxy.cfg'
new_file = 'ha.cfg'



def check(data):
    with open(haproxy_file,'r') as f:
        backend_title = 'backend %s' % data
        record_list = []
        flag = False
        for line in f:
            line = line.strip()
            if line == backend_title:
                flag = True
                continue
            if flag and line.startswith('backend'):
                flag = False
                break
            if flag and line:
                record_list.append(line)
    return record_list

def add(title,content):
    record_data = check(title)
    backend_title = 'backend %s' %title
    content_list = "server %s %s weight %d maxconn %d" \
                   %(content["server"],content["server"],content["weight"],content["maxconn"])
    if len(record_data) == 0:
        record_data.append(content_list)
        with open(haproxy_file,'r') as old ,open(new_file,'w') as new:
            for line in old:
                new.write(line)
            new.write( "\n"+ backend_title + "\n")
            for i in record_data:
                new.write(" " * 8+ i + "\n")
    else:
        if content_list in record_data:
            shutil.copy(haproxy_file,new_file)

        else:
            exist = False
            for i in record_data:
                if content["server"] in i:
                    record_data.remove(i)
                    record_data.append(content_list)
                    exist = True
            if not exist:
                record_data.append(content_list)

            flag = False
            with open(haproxy_file, 'r') as old, open(new_file, 'w') as new:
                backend_title = 'backend %s' % title
                for line in old:
                    if line.strip().startswith("backend") and line.strip() == backend_title:
                        flag = True
                        new.write(line)
                        for j in record_data:
                            new.write(" " * 8 + j + "\n")
                        continue
                    if flag and line.strip().startswith("backend"):
                        flag = False
                        new.write(line)
                        continue
                    if not flag and line.strip():
                        new.write(line)
    os.rename(haproxy_file,'haproxy.cfg.bak')
    os.rename(new_file, 'haproxy.cfg')



def write_file(title,content):
    flag = False
    with open(haproxy_file, 'r') as old, open(new_file, 'w') as new:
        backend_title = 'backend %s' % title
        for line in old:
            if line.strip().startswith("backend") and line.strip() == backend_title:
                flag = True
                if len(content) == 0:
                    continue
                else:
                    new.write(line)
                    for j in content:
                        new.write(" " * 8 + j + "\n")
                    continue
            if flag and line.strip().startswith("backend"):
                flag = False
                new.write(line)
                continue
            if not flag and line.strip():
                new.write(line)



def backend_data():
    content_dict = {}
    key_list = []
    with open(haproxy_file, 'r') as f:
        for line in f:
            if line.strip().startswith("backend"):
                key = line.strip().split()[1]
                key_list.append(key)
    for i in key_list:
        record_list = check(i)
        content_dict[i] = record_list
    return content_dict


def delete_data():
    key_list = []
    content_list = []
    content_dict = backend_data()
    for key in content_dict.keys():
        key_list.append(key)
    print("this config has %d backend" %len(key_list))
    flag = False
    while not flag:
        for j in enumerate(key_list):
            print(j[0],j[1])
        title_choice = input("[q] is  quit,please input your choice:")
        if title_choice.isdigit():
            title_choice = int(title_choice)
            if title_choice < len(key_list) and title_choice >= 0:
                record_title = key_list[title_choice]
                record_content = content_dict[record_title]
                while not flag:
                    for k in enumerate(record_content):
                        print(k[0], k[1])
                    content_choice = input("[q] is quit,which one do you delete:")
                    if content_choice.isdigit():
                        content_choice = int(content_choice)
                        if content_choice < len(record_content) and content_choice >= 0:
                            content_choice = int(content_choice)
                            content_delete = record_content[content_choice]
                            content_list.append(content_delete)
                            record_content.remove(content_delete)
                    else:
                        if content_choice == 'q':
                            write_file(record_title, record_content)
                            flag = True
                            print("you are exit")

                        #elif content_choice == "b":
                        #    break
                        else:
                            print("enter an valid number")
                            continue
        else:
            if title_choice == 'q':
                shutil.copy(haproxy_file, new_file)
                flag =True

                print("you are exit")
            else:
                print("enter an valid number")
                continue

    os.rename(haproxy_file, 'haproxy.cfg.bak')
    os.rename(new_file, 'haproxy.cfg')


def usage():
    print('''\033[1;31;40mplease enter date like :
title:"www.oldboy.org"
content:{"server":"192.168.0.1","weight":200,"maxconn":30}\033[0m'''
)


if __name__ == '__main__':
    print("""1:查询
2:添加
3:删除""")
    choice = input("[1,2,3]please enter your choice:")
    if choice == "1":
        title = input("please enter title:")
        check_list = check(title)
        print(check_list)
    elif choice == "2":
        usage()
        title = input("please enter title:")
        content = input("please enter content:")
        try:
            content = json.loads(content)
            add(title,content)
        except:
            print("enter an valid title or content")

    elif choice == "3":
        delete_data()
    else:
        print("enter an valid number")
