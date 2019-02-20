lines = []
with open("Assets/newfile.txt", "r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        line = line.split(".")
        if line!="":
            lines+=line
print(lines)
