from operator import itemgetter
import linecache
import sys
import os
old_time = None
old_per = 0.0
count = 0

for line in sys.stdin:
    words = line.split(',')
    time = int(words[0])
    per = float(words[1])
    if old_time == time:
        old_per += per
        count+=1
    else:
        if old_time != None:
            print("%d,%d"%(old_time,old_per/count))
        count = 1
        old_per = per
        old_time = time