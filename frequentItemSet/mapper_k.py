import sys

# f = open("result2.dat")
# candidatList = []
# busketList = []
# busketList1 = []
# current_item = ""

# line = f.readline()
# while line:
#     try:
#         words = line.split(",")
#         busketList.append(words[1])
#         idList.append(words[0])
#         line = f.readline()
#     except:
#         line = f.readline()

# length = len(idList)

for line in sys.stdin:
    print(line.replace("\n",""))

    # if current_item == item:
    #     candidatList.append(keys[-1])
    #     busketList1.append(words[1])
    # else:
    #     i = 0
    #     j = 1
    #     while i < len(candidatList):
    #         j = i + 1
    #         while j < len(candidatList):
    #             str = candidatList[i] + " " +candidatList[j]
    #             try:
    #                 id = idList.index(str)
    #                
    #             except:
    #                 j += 1
    #                 continue
    #