import sys
current_item = ""
current_count = 0
current_busket = []
current_candidate = []

for line in sys.stdin:
    words = line.replace('\r','').replace('\n','').split(",")
    item = ""
    item_set = words[0].split(" ")[0:-1]
    for line in item_set:
        item = item + line + " "
    candidate = words[0].split(" ")[-1]
    busket = set(words[1].split(" ")) # candidate 在哪些 busket内
    busket.remove('	')
    if current_item == item:
        current_candidate.append(candidate)
        current_busket.append(busket)
    else:
        length = len(current_candidate)
        i = 0
        j = 1
        while i < length:
            j = i + 1
            while j < length:
                inter = current_busket[i].intersection(current_busket[j])
                if len(inter) >= 20:
                    print("%s%s %s"%(current_item,current_candidate[i],current_candidate[j]),end=",")
                    for e in inter:
                        print("%s "%(e),end="")
                    print("")
                j += 1
            i += 1
        current_item = item
        current_candidate.clear()
        current_busket.clear()
        current_candidate.append(candidate)
        current_busket.append(busket)
