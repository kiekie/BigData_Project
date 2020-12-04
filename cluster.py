# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:26:10 2020

@author: Bingo
"""

#((ax+b)modc)modN
#N=18
#随意给一个数，来找哈希函数中的ac
number=784
import random
import os
import numpy as np
import sys
#user_data_path=sys.argv[1]

def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
lshf=[]

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
#print("hash 函数 abc",prime_pair)
    


def hashf_minhash(a,b,c,x):
    return (a*x+b)%c


    
#用户id对应其点击的广告类目id或者industry id 或者广告id
#    这是优化的结构，可以不需要矩阵，这里为用户id为5，看过014，用户id为1，看过013
users={5:{0,1,4},1:{0,1,3}}
#users=[user_click]   
sig_matrix=list()
hashfunclist=[[2,2,5],[2,3,5],[2,1,5],[2,4,5]]

#在所有用户中遍历，第二层遍历为在所有哈希函数中遍历，并得到其对应的permutation，
#然后寻找用户中最小signature（对应的第一个1）
def minHash(users,hashfunclist):
    lshf=[]
#    chose_f=random.randint(1,len(hashfunclist))
#    for i in range(5):
#        lshf.append(chose_f+i)
#    任选5个sig的位置，理论上只有完全一样的会hash到同一个bucket中
    for i in range(100):
        if len(lshf)<20:
            chose_f=random.randint(1,len(hashfunclist))
            if chose_f not in lshf:
                lshf.append(chose_f)
            else:
                chose_f=random.randint(0,len(hashfunclist))
    for i in range(1000000,1,-1):
        if isprime(i):
            lshf.append(i)
            break

    print(lshf)
    similar_mat={}
#    unsimilar_count=0
    for userkey in users.keys():
        user=users[userkey]
        tmpresult=[userkey]
        for hashfunc in hashfunclist:
            tmppermutation=[]
            a=hashfunc[0]
            b=hashfunc[1]
            c=hashfunc[2]
            for x in user:
                tmppermutation.append(hashf_minhash(a,b,c,x)) 
#            每一次hash完的结果
#            print("tmppermutation",tmppermutation)
            countflag=0
            for sig in tmppermutation:
#                if tmppermutation.index(sig) in user:
                if countflag==0:
                    tmpsig=sig
                    countflag+=1
                elif sig<tmpsig:
                    tmpsig=sig
            tmpresult.append(tmpsig)


#        将sig矩阵hash到不同的bucket中，只有完全一样的有很大几率hash到一个bucket中
#        bucket=dictionary key为bucket id value为用户id
        bucketid=LSH(tmpresult,lshf)
        if bucketid not in similar_mat:
            similar_mat[bucketid]=[]
            similar_mat[bucketid].append(tmpresult[0])
        else:
            similar_mat[bucketid].append(tmpresult[0])             
            
    return similar_mat



def LSH(user_sig,lshf):
    bucketid=0
    for i in range(0,len(lshf)-1):
        bucketid+=((user_sig[lshf[i]])*((i+1))+i**5+i**4+i**3+i**2+i)%lshf[len(lshf)-1]
    return bucketid


original_list={}    
   
with open('gtxt1.txt', 'r') as file:
    for line in file:
        s = line.strip().split(' ')
        tarray=np.array(s).astype(np.int).tolist()
        tmpset=set()
        for data in tarray[1:]:
            tmpset.add(data)
        original_list[tarray[0]]=tmpset
#print("original_list",original_list)
        

sig_matrix=(minHash(original_list,prime_pair))  
print(sig_matrix)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
