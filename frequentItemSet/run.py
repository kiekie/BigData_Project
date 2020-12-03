import os

support = 20
fdir = "./mid/"

# try:
#     os.system("chmod +x deleteAll.sh")
#     os.system("./deleteAll.sh")
# except:
#     print("Continuing")


First_cmd = "cat mid.txt | python3 mapper_first.py | sort | python3 reducer_first.py "+ str(support) + " > mid1.txt"
print("Stage 0:"+First_cmd)
os.system(First_cmd)
run_cmd = ""
i = 1
cmd = "cat "
input_file = "mid"+str(i)+".txt"
output_file = "mid"+str(i+1)+".txt"
cmd += input_file
cmd += " | python3 mapper_L2.py | sort | python3 reducer_L2.py "+ str(support) + " > "
cmd += output_file
print("Stage" + str(i)+":"+cmd)
os.system(cmd)
i+=1
while 1:
    print("Stage" + str(i))
    cmd = "cat "
    input_file = "mid"+str(i)+".txt"
    output_file = "mid"+str(i+1)+".txt"
    cmd += input_file
    cmd += " | python3 mapper_k.py | sort | python3 reducer_k.py "+ str(support) + " > "
    cmd += output_file
    os.system(cmd)
    f = open(output_file)
    line = f.readline()
    if len(line) < support:
        break
    i+=1




