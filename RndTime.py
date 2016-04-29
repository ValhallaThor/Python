import time
from random import randint
import sys

if len(sys.argv) != 3:
    print ("syntax: RndTime.py <number of seconds to wait> <random seconds to wait>")
else:
    waittime = int(sys.argv[1])
    rnddelay = int(sys.argv[2])
    realdelay = randint(0,rnddelay)
    print ("Waiting %d seconds with a random delay of %d seconds" % (waittime,realdelay))

time.sleep(waittime)
time.sleep(realdelay)

