# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:26:10 2020

@author: Bingo
"""

#((ax+b)modc)modN
#N=18
#随意给一个数，来找哈希函数中的ac
number=672

import random
import os
from numpy import linalg as la
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
#print(bulidhash(prime_pair))
    
    
    
user_click=[0]*18
user_click[0]=1
user_click[3]=1
user_click[7]=1
user_click[8]=1
user_click[12]=1
user_click[17]=1 


def hashf(a,b,c,x):
    return (a*x+b)%c


listd=[]    
for i in range(len(prime_pair)):
    tmp=[]
    a=prime_pair[i][0]
    b=prime_pair[i][1]
    c=prime_pair[i][2]
    for x in range(len(user_click)):
        tmp.append(hashf(a,b,c,x))
    listd.append(tmp)
    
print(listd)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
