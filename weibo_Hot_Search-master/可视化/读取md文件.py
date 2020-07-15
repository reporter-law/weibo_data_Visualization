"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import os,glob
import time
import re
import pprint
import pandas as pd
from datetime import datetime

time_name = time.strftime('%Y{y}%m{m}%d{d}%H{h}',time.localtime()).format(y='年', m='月', d='日',h='点')

path =  r"J:\微博热度\\2020年".strip("\u202a")
for path, file_dir, files in os.walk(path):

    for file_name in files:
        all_path = os.path.join(path, file_name)   # 当前循环打印的是当前目录下的所有文件

        date = re.sub("[\u4e00-\u9fa5]", "/", all_path.split(".")[0].split("\\")[-1])
        date_format = '/'.join(date.split("/")[:-1])
        print(date_format)
        date_time = datetime.strptime(date_format, '%Y/%m/%d/%H')
        #print(date_time)
        #.replace("年","").replace("月","").replace("日","")
        #if "xls" in all_path:
            #os.remove(all_path)
        if not os.path.exists('J:\微博热度\数据集'):
            os.makedirs('J:\微博热度\数据集')
        try:
            with open(all_path, "r",encoding="utf-8",errors="ignore")as f:
                content = f.read()
                #print(content)

            pattern = re.compile("###(.*?)、")
            number = re.findall(pattern, content)
            #pprint.pprint(number)

            pattern = re.compile("、(.*?)\n")
            name = re.findall(pattern, content)
            #pprint.pprint(name)

            pattern = re.compile("热度为：(.*?)\n")
            hot = re.findall(pattern, content)
            #pprint.pprint(hot)
            time = []
            for i in range(50):
                time.append(date_time)

            writer_content = {"number": number, "name": name, "hot": hot, "time": time}

            df = pd.DataFrame(writer_content)

            writer = pd.ExcelWriter('J:\微博热度\数据集\\'+all_path.split(".")[0].split("\\")[-1]+ ".xls")
            df.to_excel(writer, sheet_name='微博热度', index=False)
            writer.save()
        except Exception  as e:
            print(e,all_path)






