with open('brothers.txt') as f:
	lines = [line for line in f.readlines()]
	chars = [char for line in lines for char in line]
	words = [word for line in lines for word in line.split()]

repldict={"Chapter":"$$","the":"#","Th":"$","er":"@","and":"&","to":"%","as":"=","in":"{","on":"}","it":"~","st":"\\","is":"`"}
for n in range(len(lines)):
	for key,val in repldict.items():
		lines[n]=lines[n].replace(key, val)

with open('comped.txt', 'w') as f:
    f.write("".join(lines))