"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import pandas as pd
import os,glob
from datetime import datetime


def cancat_excel(input_files,outputfiles):
    #print(input_files)
    all_workbook = glob.glob(os.path.join(input_files, '*.xls'))
    data_frames = []
    '''重点来了，遍历工作簿、工作表，簿为列表，表为字典'''
    for workbook in all_workbook:
        all_sheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
        for worksheet_name, data in all_sheets.items():
            data_frames.append(data)
    all_data = pd.concat(data_frames, axis=0, ignore_index=True)
    #axis为列合并，而axis为1则为横向合并
    #print(all_data)
    writer = pd.ExcelWriter(outputfiles)
    all_data.to_excel(writer, sheet_name='微博数据', index=False)
    writer.save()
input_files = r"J:\微博热度\数据集\\".strip('\u202a')
path = "J:\微博热度\数据集\\合并数据"
if not os.path.exists(path):
    os.makedirs(path)
outputfiles = r"J:\微博热度\数据集\合并数据\合并数据表.xls".strip('\u202a')
#cancat_excel(input_files,outputfiles)
def make_data():
    df = pd.read_excel(outputfiles)
    df["time"] = df["time"].map(lambda x:int(x.strftime('%m%d%H')))
    print(df["time"])
    writer = pd.ExcelWriter(r"J:\微博热度\数据集\合并数据\合并数据表——1.xls".strip('\u202a'))
    df.to_excel(writer, sheet_name='微博数据', index=False)
    writer.save()
make_data()