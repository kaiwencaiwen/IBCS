lines = []
with open("Assets/newfile.txt", "r",encoding='utf-8') as f:
    line=f.read()
    for c in line.split("."):
    	c.strip()
    	lines.append(c)
print(lines)
