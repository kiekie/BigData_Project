# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:51:27 2020

@author: Ren Yubin
 SID:1155147507
"""

import operator
from operator import itemgetter
import sys
import numpy as np
from collections import OrderedDict

 
tmp_dict=OrderedDict()
item_list=[]
original_list=[]
path=sys.argv[1]
support=sys.argv[2]

print("load data 1")

with open(path,'r',encoding='utf-8') as file:
    for line in file:
        s = line.strip().split('\t')
        tarray=np.array(s[0].split(" "))
        original_list.append(tarray.astype(np.int).tolist())

print("load data 2")

for line in sys.stdin:
    line = line.strip()
    item, count = line.split('\t', 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if item not in tmp_dict:
        tmp_dict[item]=count
        
    else:
        count=tmp_dict[item]+1
        tmp_dict[item]=count
#Select items that appear more than the threshold 20    
print("load finish, sorting")

for i in tmp_dict:
    if tmp_dict[i]>support:
        item_list.append(int(i))
item_list.sort()

print("sort finish")

#make the original data into {key:set(the index that an item exist)}
def prune(item_list):
    result=OrderedDict()
    for freq_item in item_list:
        tmp_set=set()
        for index in range(len(original_list)):
            items=original_list[index]
            if freq_item in items:
                if freq_item not in result:
                    tmp_set.add(index)
                    result[freq_item]=tmp_set
                else:
                    result[freq_item].add(index)
    return result
#product frequent items set with k=2
def product_two(dict):
    result=OrderedDict()
    items=list(dict.items())
    len_dict=len(dict)
    for key1 in range(len_dict):
        for key2 in range(key1+1,len_dict):
            key_set=set()
            val_set=set()
            key_set.add(items[key1][0])
            key_set.add(items[key2][0])
#            Take the intersection of the location of the item
            val_set=items[key1][1]&items[key2][1]
            dkey=tuple(sorted(tuple(key_set)))
            if len(val_set)<support:
                continue
            if dkey not in result:
                result[dkey]=val_set
    return result

#product frequent items set with k
def product_kk(dictk,k):
    kitem_dict=OrderedDict()
    items1=list(dictk.items())
    len_dict1=len(dictk)
    if len_dict1==1:
        return kitem_dict
    for key1 in range(len_dict1):
        for key2 in range(key1+1,len_dict1):
#            if If the first K-2 keys are not same ,then they can not merge
            keytp1=items1[key1][0][:k-2]
            keytp2=items1[key2][0][:k-2]
            
            if keytp1==keytp2:
                keyset1=set(items1[key1][0])
                keyset2=set(items1[key2][0])
                valset=set()
#                Merge key 
                keyset=keyset1|keyset2
#            Take the intersection of the location of the item
                valset=items1[key1][1]&items1[key2][1]
                if len(valset)<support:
                    continue
                dkey=tuple(sorted(tuple(keyset)))
                if len(dkey)==k:
                    if dkey not in kitem_dict:
                        kitem_dict[dkey]=valset 
                    else:
#                        if key is same ,then merge the location of the item
                        kitem_dict[dkey]=kitem_dict[dkey]|valset             
            else:
                break      
    return kitem_dict

                   
prune_dict=prune(item_list)  

original_list=[]
twoItems=product_two(prune_dict)   


flag=True
k=3
tmp_result={}
resultk=product_kk(twoItems,3)
while flag:
#    if the length of result is 0,we take the k-1 items set as result
    if len(resultk)==0:
        print('The size of maximal frequent item set is %s' % (k-1))
        print('the items are : %s'%(tmp_result.keys()))
        flag=False
    else:
        tmp_result=resultk
        k+=1
        if k>10:
            print('Numbers of frequent item with size %s===%s' %((k-1),len(tmp_result)))
            print("Frequent set of size  %s  == %s"%(k-1,tmp_result.keys()))
        resultk=product_kk(tmp_result,k)

        
        
        
        
