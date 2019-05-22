import hashlib
bytes=b'password'
result = hashlib.md5(bytes).hexdigest()
print(result)