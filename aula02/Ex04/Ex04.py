import os
import sys
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA

if len(sys.argv)<3:
    print("Need Valid Arguments!")
    exit(1)

fileName = sys.argv[1]
chave = sys.argv[2]

if len(chave)<5:
    h = SHA.new()
    h.update(chave.encode('utf-8'))
    chave = h.hexdigest()
elif len(chave)>256:
    chave = chave[0:256]

f = open(fileName, 'rb')
text = f.read()

cipher = ARC4.new(chave)
cryptogram = cipher.encrypt(text)
os.write(1, cryptogram )

decipher = ARC4.new(chave)
decrypted = decipher.decrypt( cryptogram )
print(decrypted.decode('utf-8'))