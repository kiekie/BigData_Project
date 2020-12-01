# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:24:22 2020

@author: Bingo
"""

import csv
import os
from numpy import linalg as la
import numpy as np

#key为类目id，value为素材id
product_categroy={}
with open('G:/BDT5741/BDTproject/adtest.csv','r',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row['product_category']) not in product_categroy:
            product_categroy[int(row['product_category'])]=set()
            if row['creative_id'] not in product_categroy[int(row['product_category'])]:  
                product_categroy[int(row['product_category'])].add(row['creative_id'])
        else:
            product_categroy[int(row['product_category'])].add(row['creative_id'])
csvfile.close()  
print(product_categroy)
   
user_click={}
with open('G:/BDT5741/BDTproject/fretest.csv','r',encoding='utf-8') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
      if int(row['user_id']) not in user_click:
          user_click[int(row['user_id'])]={}
          for categroy in product_categroy.keys():
              if row['creative_id'] in product_categroy[categroy]:
                  if categroy not in user_click[int(row['user_id'])]:
                      user_click[int(row['user_id'])][categroy]=1
                  else:
                      user_click[int(row['user_id'])][categroy]+=1
      else:
          for categroy in product_categroy.keys():
              if row['creative_id'] in product_categroy[categroy]:
                  if categroy not in user_click[int(row['user_id'])]:
                      user_click[int(row['user_id'])][categroy]=1
                  else:
                      user_click[int(row['user_id'])][categroy]+=1
csvfile.close()

#字典嵌入字典  key1为用户id，内层字典key为广告类目,value为观看次数
print(user_click)


tryd=[]
testlist1=[0]*5
testlist2=[0]*5
testlist3=[0]*5
testlist1[0]=1
testlist1[4]=25
for key in product_categroy.keys():
    testlist2[key-1]=key+3 
for key in product_categroy.keys():
    testlist3[key-1]=key*2-1 
tryd.append(testlist1)
tryd.append(testlist2)
tryd.append(testlist3)
tryd=np.array(tryd)
print(tryd)
def pca(data_mat, top_n_feat=1):
    """ 
    主成分分析：  
    输入：矩阵data_mat ，其中该矩阵中存储训练数据，每一行为一条训练数据  
         保留前n个特征top_n_feat，默认全保留
    返回：降维后的数据集和原始数据被重构后的矩阵（即降维后反变换回矩阵）
    """  

    # 获取数据条数和每条的维数 
    print("data_mat",type(data_mat),data_mat.dtype)
    num_data,dim = data_mat.shape  
    print("num_data",num_data)  # 100
    print("维数",dim)   # 784
    
    # 数据中心化，即指变量减去它的均值
    mean_vals = data_mat.mean(axis=0)  #shape:(784,)
    mean_removed = data_mat - mean_vals # shape:(100, 784)
    print("去均值化",mean_removed.shape)

    # 计算协方差矩阵（Find covariance matrix）
    cov_mat = np.cov(mean_removed, rowvar=0) # shape：(784, 784)
    print("cov_mat_shape",cov_mat.shape)
    # 计算特征值(Find eigenvalues and eigenvectors)
    eig_vals, eig_vects = la.eig(np.mat(cov_mat)) # 计算特征值和特征向量，shape分别为（784，）和(784, 784)

    eig_val_index = np.argsort(eig_vals)  # 对特征值进行从小到大排序，argsort返回的是索引，即下标
    print("特征值数量",len(eig_vals))
    eig_val_index = eig_val_index[:-(top_n_feat + 1) : -1] # 最大的前top_n_feat个特征的索引
    print("tezhengzhi",eig_vals)
    print("tezhengxiangliang",eig_vects)
    # 取前top_n_feat个特征后重构的特征向量矩阵reorganize eig vects, 
    # shape为(784, top_n_feat)，top_n_feat最大为特征总数
    reg_eig_vects = eig_vects[:, eig_val_index] 

    # 将数据转到新空间
    low_d_data_mat = mean_removed * reg_eig_vects # shape: (100, top_n_feat), top_n_feat最大为特征总数
    recon_mat = ((low_d_data_mat * reg_eig_vects.T) + mean_vals).astype(np.uint8) # 根据前几个特征向量重构回去的矩阵，shape:(100, 784)

#    print("recon_mat",recon_mat.dtype)
#    recon_mat.dtype="float64"
#    print("recon_mat",recon_mat.shape)
    
    return low_d_data_mat, recon_mat




low_d_data_mat, recon_mat=pca(tryd)
print(recon_mat)