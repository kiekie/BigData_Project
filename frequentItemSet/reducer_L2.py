import sys
itemList = []
buscketList = []

threshold=int(sys.argv[1])

i = 0
j = 1

for line in sys.stdin:
    words = line.replace('\n','').split(",")
    try:
        busketPool = words[1].split(" ")
        buscketList.append(busketPool)
        itemList.append(words[0])
    except:
        continue

while i < len(itemList):
    while j < len(itemList):
        a = set(buscketList[i])
        a.remove('')
        try:
            b = set(buscketList[j])
            b.remove('')
        except:
            continue
        inter = a.intersection(b)
        if(len(inter) >= threshold):
            print("%s %s"%(itemList[i],itemList[j]),end=",")
            for line in inter:
                print("%s "%(line),end="")
            print("")

        j += 1
        inter.clear()
    i += 1
    j = i + 1