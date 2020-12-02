from operator import itemgetter
import linecache
import sys
import os
old_line = None
count = 0

for line in sys.stdin:
    line = line[0:-1]
    if line == old_line:
        count+=1
    else:
        if old_line != None:
            print("%s,%d"%(old_line,count))
        count = 1
        old_line = line
