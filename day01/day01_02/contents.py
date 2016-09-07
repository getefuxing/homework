#!/usr/bin/env python
#-*-coding:utf-8 -*-

import json
import sys

with open('contents.json') as f:
    data = json.load(f)

flag = True
while flag:
    province = []
    for key in data.keys():
        province.append(key)
    for i in range(1,len(province)+1):
        print '''%s:%s''' %(i,province[i-1])
    province_choice = raw_input('please enter number:')
    if province_choice == 'q' or province_choice == 'b':
        flag = False
        break
    if province_choice > str(0) and province_choice < str(len(province)+1):
        while flag:
            city = []
            for y in data[province[int(province_choice)-1]]:
                city.append(y)
            for i in  range(1,len(city)+1):
                print '''%s:%s''' %(i,city[i-1])
            city_choice = raw_input('please enter number:')
            if city_choice == 'b':
                break
            if city_choice == 'q':
                flag = False
                break
            if city_choice > str(0) and city_choice < str(len(city)+1):
                while flag:
                    county = []
                    for z in data[province[int(province_choice)-1]][city[int(city_choice)-1]]:
                        county.append(z)
                    for i in range(1,len(county)+1):
                        print '''%s:%s''' %(i,county[i-1])
                    county_choice = raw_input('please enter number:')
                    if county_choice == 'b':
                        break
                    if county_choice == 'q':
                        flag = False
                        break
                    if county_choice > str(0) and county_choice < str(len(county)+1):
                        print "you are win"
                        sys.exit(0)
                    else:
                        print "enter an vaild number!"
                        continue
            else:
                print "enter an vaild number"
                continue
    else:
        print "enter an vaild number"
        continue
