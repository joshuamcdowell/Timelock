


import sys
from datetime import datetime
import datetime
from pytz import timezone # pip install pytz
import pytz
import hashlib

epoch = sys.stdin.read()
i = 0
nextNum = ""
for ch in epoch:
    if ch == ' ':
        if i == 0:
            epochYear = nextNum
        elif i == 1:
            epochMonth = nextNum
        elif i == 2:
            epochDay = nextNum
        elif i == 3:
            epochHour = nextNum
        elif i == 4:
            epochMin = nextNum
        elif i == 5:
            epochSec = nextNum
        nextNum = ""
        i += 1
    else:
        nextNum += ch

if i == 5:
    if nextNum[-1] == '\n':
        nextNum = nextNum[:-1]
    epochSec = nextNum

if i < 5:
    print("Not enough given. Exiting...")
    exit()

localTZ = pytz.timezone('America/Chicago')
targetTZ = pytz.timezone('UTC')

dt = datetime.datetime(int(epochYear), int(epochMonth), int(epochDay), int(epochHour), int(epochMin), int(epochSec))
dt = localTZ.localize(dt)
dt = targetTZ.normalize(dt)

ct = datetime.datetime.now()
ct = localTZ.localize(ct)
ct = targetTZ.normalize(ct)

finalTime = ct - dt
ft = int(finalTime.total_seconds())
ft -= (ft % 30)


h = str(hashlib.md5(str(hashlib.md5(str(ft)).hexdigest())).hexdigest())
numcount = 0
letcount = 0

for c in h:
    if(numcount >= 2 and letcount >= 2):
        break

    if(ord(c) >= 48 and ord(c) <= 57):
        numcount += 1
    elif(ord(c) >= 97 and ord(c) <= 122):
        letcount += 1

if(numcount < 2):
    letcount = 4 - numcount
elif(letcount < 2):
    numcount = 4 - letcount
else:
    numcount = 2
    letcount = 2

code = ""
k = letcount
for c in h:
    if(k <= 0):
        break

    if(ord(c) >= 97 and ord(c) <= 122):
        code += c
        k -= 1

i = len(h) - 1
k = numcount

while(i >= 0):
    if(k <= 0):
        break

    char = h[i]
    if(ord(char) >= 48 and ord(char) <= 57):
        code += char
        k -= 1

    i -= 1

print(code)
