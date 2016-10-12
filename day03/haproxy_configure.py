#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import shutil
import json
import os

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



def delete(title,content):
    record_data = check(title)
    content_list = "server %s %s weight %d maxconn %d" \
                   %(content["server"],content["server"],content["weight"],content["maxconn"])
    if len(record_data) == 0:
        shutil.copy(haproxy_file, new_file)
    else:
        if content_list not in record_data:
            shutil.copy(haproxy_file, new_file)
        else:
            flag = False
            record_data.remove(content_list)
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
        usage()
        title = input("please enter title:")
        content = input("please enter content:")
        try:
            content = json.loads(content)
            delete(title,content)
        except:
            print("enter an valid title or content")
    else:
        print("enter an valid number")
