# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 15:42:40 2020

@author: Bingo
"""

import csv
import os
import numpy as np

user_click={}

with open('G:/BDT5741/BDTproject/fretest.csv','r',encoding='utf-8') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
      if int(row['user_id']) not in user_click:
          user_click[int(row['user_id'])]=set()
          if row['creative_id'] not in user_click[int(row['user_id'])]:    
              user_click[int(row['user_id'])].add(row['creative_id'])
      else:
          user_click[int(row['user_id'])].add(row['creative_id'])
csvfile.close()


if os.path.exists('gtxt.txt'):
    os.remove(r'gtxt.txt')
for keys,items in user_click.items():
    str1=''
    for item in items:
        str1=str1+item+'\t'
    with open(r'gtxt.txt', 'a') as f:
        f.write(str1)
        f.write('\r')  
f.close()
 

#原用户点击数据
original_list=[]    
   
with open('G:/BDT5741/BDTproject/gtxt.txt', 'r') as file:
    for line in file:
        s = line.strip().split('\t')
        tarray=np.array(s)
        original_list.append(tarray.astype(np.int).tolist())
print("original_list",original_list)


#找到的频繁项集
frequentSet={0:{1,2,4,5,8,11,14},1:{13,15,14,1,12,88,99,120,133}}
def recomByfrq(userclick,frequentSet,threshold):
    for i in frequentSet:
#        在每个频繁项集中找寻其与用户点击数据的交集
        intersectionSet=set(userclick).intersection(frequentSet[i])
#        如果交集的长度/频繁项集的长度 高于阈值，则向用户推荐两个集合的差
        if (len(intersectionSet)/len(frequentSet[i]))>threshold:
            print(frequentSet[i],"recommand for:",userclick ,"==============",frequentSet[i]-intersectionSet)
            

threshold=0.5
#可以改成用户点击的数据作为输入
for i in original_list:
    recomByfrq(i,frequentSet,threshold)











