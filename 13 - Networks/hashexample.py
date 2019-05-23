import hashlib
target="3fafb2f44ee29e1cc0bd3128176945dc"
with open('password_list.txt','r') as f:
	plist=f.readlines()
	for p in plist:
		bytes=str.encode(p.strip('\n'))
		result = hashlib.md5(bytes).hexdigest()
		if result==target:
			print("Password found:", p)
			break

print([i for i in range(0,10)])