import hashlib
import os

INPUT_FILE = os.environ["PAYLOAD_FILE"]

print(INPUT_FILE)

hasher = hashlib.md5()
with open(INPUT_FILE, 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print("**OUTPUT**")
print(hasher.hexdigest())
