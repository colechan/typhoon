#!/usr/bin/env python
#
# encoding: utf-8
'''
# Time    : 13/02/2020 16:12
# Author  : Cole Chan chensqi@gdou.edu.cn
# Usage   :
# File    : plot_track.py
# Aim     :
# Software: PyCharm
'''
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import pandas as pd
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

#读入数据
df_best =  pd.read_csv('E:/data/tracks.csv')

#读取边界文件
with open('E:\data1\CN-border-La.dat') as src:
    context = src.read()
    blocks = [cnt for cnt in context.split('>') if len(cnt) > 0]
    borders = [np.fromstring(block, dtype=float, sep=' ') for block in blocks]

#设置投影
mapcrs = ccrs.Mercator()
datacrs = ccrs.PlateCarree()

#画图设置
fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='gray', alpha=0.5, linestyle='--')
for line in borders:
        ax.plot(line[0::2], line[1::2], '-', lw=1, color='k',
                transform=ccrs.Geodetic())
gl.xformatter = LONGITUDE_FORMATTER #设置x轴为经度格式
gl.yformatter = LATITUDE_FORMATTER #设置y轴为纬度格式
gl.xlines = False
gl.ylines = False
gl.xlabels_top = False  #关闭顶部标签
gl.ylabels_right = False #关闭右边标签
gl.ylabel_style = {'size': 20} #y轴的size
gl.xlabel_style = {'size': 20} #x轴的size
ax.set_extent([110, 170, 5, 45], ccrs.PlateCarree())  #添加海洋、陆地、河流、湖泊
# ax.set_extent([100, 145, 12, 45], ccrs.PlateCarree())
#添加海洋、陆地、河流、湖泊
ax.add_feature(cfeature.OCEAN.with_scale('50m'))
ax.add_feature(cfeature.LAND.with_scale('50m'))
ax.add_feature(cfeature.RIVERS.with_scale('50m'))
ax.add_feature(cfeature.LAKES.with_scale('50m'))
#画图以及设置
ax.plot(df_best['lon']*1,df_best['lat']*1,color='red',marker='o',linestyle = '-',linewidth=3.0,markersize=6, transform=ccrs.Geodetic(),label='track')

plt.legend()
plt.show()
