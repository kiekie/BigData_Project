# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:26:10 2020

@author: Bingo
"""

#((ax+b)modc)modN
#N=18
#随意给一个数，来找哈希函数中的ac
number=19

import random
import os
import numpy as np


def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def acprime(a,c):
    if c%a==0:
        return False
    return True
    
#找a c
#def find_prime_pair(num):
#    primelist=[]
#    pairlist=[]
#    for i in range(1,num):
#        if isprime(i) and i>=4*num/5:
#            primelist.append(i)
#    for i in primelist:
#        pairlist.append([num-i,i])
#    return pairlist

def find_prime_pair(num):

    pairlist=[]
    for i in range(int(4*num/5),num):
        if acprime(num-i,i):
            pairlist.append([num-i,i])
    return pairlist

prime_pair=find_prime_pair(number)
print("互质个数",len(find_prime_pair(number)))



def bulidhash(prime_pair):
    for i in range(len(prime_pair)):
        tmp=prime_pair[i][1]-prime_pair[i][0]
        b=random.randint(int(tmp/2),tmp)
        prime_pair[i].insert(1,b)
    return prime_pair

prime_pair=bulidhash(prime_pair)
print("hash 函数 abc",prime_pair)
    


def hashf(a,b,c,x):
    return (a*x+b)%c

    
    
#用户id对应其点击的广告类目id或者industry id 或者广告id
#    这是优化的结构，可以不需要矩阵，这里为用户id为5，看过014，用户id为1，看过013
users={5:{0,1,4},1:{0,1,3}}
#users=[user_click]   
sig_matrix=list()
hashfunclist=[[2,2,5]]

#在所有用户中遍历，第二层遍历为在所有哈希函数中遍历，并得到其对应的permutation，
#然后寻找用户中最小signature（对应的第一个1）
def minHash(users,hashfunclist,numElement=5):
    similar_mat={}
    unsimilar_count=0
    for userkey in users.keys():
        user=users[userkey]
        tmpresult=[]
        print("用户数据",user)
        for hashfunc in hashfunclist:
            tmppermutation=[]
            a=hashfunc[0]
            b=hashfunc[1]
            c=hashfunc[2]
            for x in range(numElement):
                tmppermutation.append(hashf(a,b,c,x)) 
#            每一次hash完的结果
            print("tmppermutation",tmppermutation)
            countflag=0
            for sig in tmppermutation:
                if tmppermutation.index(sig) in user:
                    if countflag==0:
                        tmpsig=sig
                        countflag+=1
                    elif sig<tmpsig:
                        tmpsig=sig
            tmpresult.append(tmpsig)
            
#        将初步相似的加入到同一key值下面，不相似的会新开一个key，放入新的signature列表
        if len(similar_mat)==0:
            similar_mat[unsimilar_count]=[tmpresult]
        else:
            similar_count=0
            for key in similar_mat.keys():
                for item in similar_mat[key][0]:
#                    计算相似sig的数量，之和其中一个比就行，因为初步判断相似，不需要全部比较之后取均值
                    if tmpresult[similar_mat[key][0].index(item)]==item:
                        similar_count+=1
#                0.5作为初步相似的阈值
                if similar_count/len(similar_mat[key][0])>0.5:
                    similar_mat[key].append(tmpresult)
                    break
                else:
                    unsimilar_count+=1
                    similar_mat[unsimilar_count]=[tmpresult]
                    break
    
                
            
    return similar_mat

sig_matrix=(minHash(users,prime_pair))


        
#sig_matrix=(minHash(users,hashfunclist))
            
print(sig_matrix)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
