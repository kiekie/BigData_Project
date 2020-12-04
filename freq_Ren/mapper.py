# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:28:47 2020

@author: Ren Yubin
 SID:1155147507
"""

import sys

for line in sys.stdin:
    line=line.strip()
    items=line.split()
    for item in items:
        print ('%s\t%s' % (item, 1))


    
#with open('G:/BDT5741/asgn-1/assignment-02/gtxt1.txt','r',encoding='utf-8') as file: 
#    for line in file:
#        line=line.strip()
#        items=line.split()
#        for item in items:
#            print ('%s\t%s' % (item, 1))    