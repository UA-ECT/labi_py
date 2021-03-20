# Run with:
#   python3 Ex01.py [origin file] [end file]
# 

# imports
import sys #for the arguments
import hashlib #for the encryption

print(sys.argv)


# read origin file
# help: https://www.w3schools.com/python/python_file_open.asp
f = open(sys.argv[1], "r")
rawText = f.read()
f.close()

# encriptation
# help: https://www.askpython.com/python-modules/python-hashlib-module
h = hashlib.sha1()
h.update(rawText.encode('utf-8'))
encryptedText = h.hexdigest()

# write end file
#help: https://www.w3schools.com/python/python_file_write.asp
f = open(sys.argv[2], "w")
f.write(encryptedText)
f.close()