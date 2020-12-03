import sys
busket = 1

for line in sys.stdin:
    words = line.split(" ")
    for word in words:
        print("%s\t%d"%(word,busket))
    busket+=1