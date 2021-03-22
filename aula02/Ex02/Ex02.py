import sys
import Crypto
import hashlib

if len(sys.argv)<3:
    print("Need Valid Arguments!")

h = hashlib.sha1()

f = open(sys.argv[1], 'rb')
buffer = f.read(512)
while len(buffer)>0:
    h.update(buffer)
    buffer = f.read(512)

f = open(sys.argv[2], "w")
f.write(h.hexdigest())
f.close()