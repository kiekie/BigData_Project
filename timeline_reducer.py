from operator import itemgetter
import linecache
import sys

current_id = None
old_time = None
current_hot = 0
timeline = []
linehot = []

for line in sys.stdin:
    words = line.split(',')
    try:
        id = int(words[0])
    except ValueError:
        continue
    if current_id == id:
        time = int(words[1])
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
            print("-1,%d,"%current_id)
            for e in timeline:
                print("%d"%e,end=',')
            print("")
            for e in linehot:
                print("%d"%e,end=',')
            print("")
            timeline = []
            linehot = []
        current_id = id
        old_time = None
        current_hot = 0