import sys
import Crypto
from Crypto.Hash import SHA256

if len(sys.argv)<3:
    print("Need Valid Arguments!")
    exit(1)

h = SHA256.new()

f = open(sys.argv[1], 'rb')
buffer = f.read(512)
while len(buffer)>0:
    h.update(buffer)
    buffer = f.read(512)

f = open(sys.argv[2], "w")
f.write(h.hexdigest())
f.close()