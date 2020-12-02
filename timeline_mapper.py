import sys
import getopt
import os
import time

import sys

for line in sys.stdin:
    words = line.split(",")
    try:
        print("%s,%s"%(words[2],words[0]))
    except:
        continue