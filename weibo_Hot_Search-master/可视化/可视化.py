"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py
df = pd.read_excel(r"J:\微博热度\数据集\合并数据\合并数据表——1.xls".strip('\u202a'))

#年份与类型一致才可以，否则就会出问题
fig =px.bar(df[-2000:], x="hot",y='number', animation_frame="time",animation_group="number",
            orientation = 'h',range_y=[df.name.max(),0],color = 'name',
           )
fig.show()
py.plot(fig,filename='J:\微博热度\数据集\合并数据\合并数据表.html')