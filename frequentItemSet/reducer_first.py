import sys
threshold = 20

threshold=int(sys.argv[1])

threshold_itemset = []
current_item = 0
current_count = 0
item = 0

for line in sys.stdin:
    words = line.split('\t')
    try:
        item = int(words[0])
        words[1] = words[1].replace('\n', '').replace('\r', '')
    except:
        continue
    if item == current_item and current_count < threshold - 1:
        current_count+=1
        threshold_itemset.append(words[1])
    elif item == current_item and current_count == threshold-1:
        current_count+=1
        print("%d,"%current_item,end='')
        for itembucket in threshold_itemset:
            print("%s "%itembucket,end = '')
        threshold_itemset.clear()
        print("%s "%words[1],end = '')
    elif item == current_item:
        print("%s "%words[1],end = '')
    
    if item != current_item:
        print("",end="\n")
        current_count = 1
        current_item = item


