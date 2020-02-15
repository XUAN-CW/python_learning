#coding=utf-8
#测试os.walk()递归遍历所有的子目录和子文件
'''
os.walk()方法：
    返回一个 3个元素的元组，(dirpath, dirnames, filenames),
    dirpath：要列出指定目录的路径
    dirnames：目录下的所有文件夹
    filenames：目录下的所有文件
'''

import os

all_files = []
path = os.getcwd()
list_files = os.walk(path)

for dirpath,dirnames,filenames in list_files:
    for dir in dirnames:
        all_files.append(os.path.join(dirpath,dir))
    for file in filenames:
        all_files.append(os.path.join(dirpath,file))

#打印所有的子目录和子文件
for file in all_files:
    print(file)