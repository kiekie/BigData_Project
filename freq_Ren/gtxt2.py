# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:26:10 2020

@author: Bingo
"""

import csv
import os
import sys
import numpy as np

user_click={}
#ad.csv
csv_path1=sys.argv[1]
#click_log.csv
csv_path2=sys.argv[2]

#只输入txt文件名即可，不用增加后缀
txtpath=sys.argv[3]

#输入category，creative_id，industry其中之一，选择需要读取得到的数据。
#针对kmeans 不要写入txt后再使用数据，会遗失点击次数的数据
readtype=sys.argv[4]

#csv_path1='adtest.csv'
#csv_path2='click_log.csv'
#txtpath='gtxt'
#readtype='\ufeffcreative_id'
#readtype='categroy'
#readtype='industry'

    
def data_creative(csv_path,txtpath):
#    每一行为用户点击的广告素材id，针对频繁项集，每一行第一列为用户id
    with open(csv_path,'r',encoding='utf-8') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          if int(row['user_id']) not in user_click:
              user_click[int(row['user_id'])]=set()
              if row['\ufeffcreative_id'] not in user_click[int(row['user_id'])]:    
                  user_click[int(row['user_id'])].add(row['\ufeffcreative_id'])
          else:
              user_click[int(row['user_id'])].add(row['\ufeffcreative_id'])
    csvfile.close()
    print(user_click)
    if os.path.exists(txtpath+"_creative.txt"):
        os.remove(txtpath+"_creative.txt")
    with open(txtpath+"_creative.txt", 'a') as f:
        for keys,items in user_click.items():
            str1=str(keys)+" "
            for item in items:
                str1=str1+str(item)+' '
            f.write(str1)
            f.write('\n')  
    f.close()

def data_categroy(csv_path1,csv_path2,txtpath):
    #key为类目id，value为素材id
    product_categroy={}
    with open(csv_path1,'r',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['product_category']) not in product_categroy:
                product_categroy[int(row['product_category'])]=set()
                if row['\ufeffcreative_id'] not in product_categroy[int(row['product_category'])]:  
                    product_categroy[int(row['product_category'])].add(row['\ufeffcreative_id'])
            else:
                product_categroy[int(row['product_category'])].add(row['\ufeffcreative_id'])
    csvfile.close()  
    print(product_categroy)
    user_click={}
    #行user，列类目id，交点为这个用户点击这个类目的次数
    with open(csv_path2,'r',encoding='utf-8') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          if int(row['user_id']) not in user_click:
              user_click[int(row['user_id'])]={}
              for categroy in product_categroy.keys():
                  if row['creative_id'] in product_categroy[categroy]:
                      if categroy not in user_click[int(row['user_id'])]:
                          user_click[int(row['user_id'])][categroy]=int(row['click_times'])
                      else:
                          user_click[int(row['user_id'])][categroy]+=int(row['click_times'])
          else:
              for categroy in product_categroy.keys():
                  if row['creative_id'] in product_categroy[categroy]:
                      if categroy not in user_click[int(row['user_id'])]:
                          user_click[int(row['user_id'])][categroy]=int(row['click_times'])
                      else:
                          user_click[int(row['user_id'])][categroy]+=int(row['click_times'])
    csvfile.close()
#    print(user_click)
    #    写入文件未保存点击次数数据
    if os.path.exists(txtpath+'_categroy.txt'):
        os.remove(txtpath+'_categroy.txt')
    with open(txtpath+'_categroy.txt','a') as f:
        for keys,items in user_click.items():
            str1=str(keys)+" "
            for item in items:
                str1=str1+str(item)+" "
            f.write(str1)
            f.write('\n')
        f.close()
        
        
def data_industryid(csv_path1,csv_path2,txtpath):
    #key为industry_id，value为素材id
    product_categroy={}
    with open(csv_path1,'r',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['industry']) not in product_categroy:
                product_categroy[int(row['industry'])]=set()
                if row['\ufeffcreative_id'] not in product_categroy[int(row['industry'])]:  
                    product_categroy[int(row['industry'])].add(row['\ufeffcreative_id'])
            else:
                product_categroy[int(row['industry'])].add(row['\ufeffcreative_id'])
    csvfile.close()  

       
    user_click={}
    #行user，列industry_id，交点为这个用户点击这个industry的次数
    with open(csv_path2,'r',encoding='utf-8') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          if int(row['user_id']) not in user_click:
              user_click[int(row['user_id'])]={}
              for categroy in product_categroy.keys():
                  if row['\ufeffcreative_id'] in product_categroy[categroy]:
                      if categroy not in user_click[int(row['user_id'])]:
                          user_click[int(row['user_id'])][categroy]=int(row['click_times'])
                      else:
                          user_click[int(row['user_id'])][categroy]+=int(row['click_times'])
          else:
              for categroy in product_categroy.keys():
                  if row['\ufeffcreative_id'] in product_categroy[categroy]:
                      if categroy not in user_click[int(row['user_id'])]:
                          user_click[int(row['user_id'])][categroy]=int(row['click_times'])
                      else:
                          user_click[int(row['user_id'])][categroy]+=int(row['click_times'])
    csvfile.close()
    
#    print(user_click)
#    写入文件未保存点击次数数据
    if os.path.exists(txtpath+'_industry.txt'):
        os.remove(txtpath+'_industry.txt')
    with open(txtpath+'_industry.txt','a') as f:
        for keys,items in user_click.items():
            str1=str(keys)+" "
            for item in items:
                str1=str1+str(item)+" "
            f.write(str1)
            f.write('\n')
        f.close()
        
        
if readtype=="category":
    data_categroy(csv_path1,csv_path2,txtpath)
elif readtype=="creative_id":
    data_creative(csv_path2,txtpath) 
elif readtype=="industry":
    data_industryid(csv_path1,csv_path2,txtpath)

#原用户点击数据
#original_list=[]    
#with open(txtpath+"_creative.txt", 'r') as file:
#    for line in file:
#        s = line.strip().split(' ')
#        tarray=np.array(s)
#        original_list.append(tarray.astype(np.int).tolist())
#print("original_list",original_list)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
