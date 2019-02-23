#!/usr/bin/env python
#-*- coding:utf8 -*-
# Author:Taoke
# @Time:2019/2/23 23:28
'''
功能说明:将猫眼榜单top100的电影数据爬取下来保存到csv文件中
'''
import urllib.request
import re
import csv
# 创建maoyan_data.csv文件
with open('maoyan_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # 写入csv文件第一行的头
    writer.writerow(('id', '电影名称', '明星', '上映时间', '评分'))
    # 构造url
    for url in ('https://maoyan.com/board/4?offset=%d'%(i*10,) for i in range(10)):
        # 访问url获取数据
        text = urllib.request.urlopen(url).read().decode('utf-8')
        # 通过正则表达式匹配出数据
        res = re.findall('<dd>[\s\S]*?</dd>',text)
        for i in res:
            _id = re.findall('<i class="board-index board-index-\d*?">(.*?)</i>',i)[0]
            title = re.findall('title="([\s\S]*?)" c',i)[0]
            stars = re.findall('<p class="star">[\s\S]*?主演：([\s\S]*?)</p>',i)[0].strip()
            time = re.findall('<p class="releasetime">上映时间：([\s\S]*?)</p>',i)[0].strip()
            score = ''.join(re.findall('<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>',i)[0])
            # 将匹配完成的数据写入maoyan_data.csv文件
            writer.writerow((_id,title,stars,time,score))
            # 打印数据
            print(_id,title,stars,time,score)




