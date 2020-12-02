from operator import itemgetter
import linecache
import sys
import os

current_id = None
old_time = None
current_hot = 0
timeline = []
linehot = []


for line in sys.stdin:
    words = line.split(',')
    try:
        id = int(words[0])
        time = int(words[1])
    except ValueError:
        continue
    if current_id == id:
        if old_time == time:
            current_hot+=1
        else:
            if current_hot != 0:
                linehot.append(current_hot)
                timeline.append(old_time)
            current_hot = 1
            old_time = time
    else:
        #output all the result
        if current_id != None:
            linehot.append(current_hot)
            timeline.append(old_time)
            #print("-1,%d,"%current_id)
            tmp = []
            s = sum(linehot)
            for i in range(len(timeline)):
                j = 1.1
                j = float(linehot[i] * 10000)/s
                l = [timeline[i],j]
                tmp.append(l)
            tmp.sort(key=lambda x:x[0])
            for e in tmp:
                print("%d,%f"%((e[0]-tmp[0][0]),e[1]))
            timeline = []
            linehot = []
        current_id = id
        old_time = time
        current_hot = 1