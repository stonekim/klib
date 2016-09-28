# -*- coding: utf-8 -*-
import os
import sys
import re

import datetime
import time

house_types = ['一房住宅', '二房住宅', '三房住宅', '四房住宅', '四房以上', '复式', '复式住宅', '别墅']
area_types = ['90平方米以下', '90~144平方米', '144平方米以上']
useage_types = ['商业', '办公楼', '住宅']

def get_house_re():
    house_re = r"<.*?>(\d+)<"
    house_re += r".*?>([\d|\.]+).*?<"
    house_re += r".*?\s+(\d+)&nbsp"
    house_re += r".*?>(\d+)<"
    house_re += r".*?>([\d|\.]+).*?<"
    return house_re

def get_area_re():
    area_re = r"<.*?>(\d+)<"
    area_re += r".*?>([\d|\.]+).*?<"
    area_re += r".*?>(\d+).*?<"
    area_re += r".*?>(\d+).*?<"
    return area_re

def get_useage_re():
    useage_re = r"<.*?>(\d+)<"
    useage_re += r".*?>([\d|\.]+).*?<"
    useage_re += r".*?\s+(\d+)&nbsp"
    useage_re += r".*?>(\d+).*?<"
    useage_re += r".*?>([\d|\.]+).*?<"
    return useage_re

def findall_match(content, re_str):
    pattern = re.compile(re_str, re.DOTALL)
    match = pattern.findall(content)
    return match

def trans2str(match, count):
    ret_str = ""
    if len(match) <= 0:
        match = ['0'] * count
    else:
        match = match[0]

    ret_str += ",".join(match) + ","
    return ret_str
    
    
def fetch_data(dist):    
    print 'start to fetch [%s] dist data'  % dist
    with open(dist, 'r') as fb:
        html_content = fb.read()
        house_re = get_house_re()
        area_re = get_area_re()
        useage_re = get_useage_re()
        print house_re, area_re, useage_re
    
        now = datetime.datetime.now()
        date_str = time.strftime("%Y%m%d")
        csv_str = date_str + "," 
        for house_item in house_types:
            re_str = '>' + house_item + house_re 
            match = findall_match(html_content, re_str)
            csv_str += trans2str(match, 5)
            print house_item, match
    
        for area_item in area_types:
            re_str = '>' + area_item + area_re
            match = findall_match(html_content, re_str)
            csv_str += trans2str(match, 4)
            print area_item, match
    
        for useage_item in useage_types:
            re_str = '>' + useage_item + useage_re
            match = findall_match(html_content, re_str)
            csv_str += trans2str(match, 5)
            print useage_item, match

        with open(dist + '.csv', 'a') as csv_fb:
            csv_str = csv_str.strip(',') + "\n"
            csv_fb.writelines(csv_str)

if __name__ == '__main__':
    fetch_data('Ft')
