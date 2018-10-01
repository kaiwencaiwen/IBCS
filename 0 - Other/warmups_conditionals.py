# 1001
# a) there are random generators but they are still not truly random
# b) yes?
# c) yes, but it's very complicated and hard to measure

# is it a number?
numb = "2"
if numb.isdigit():
    print("yeah is number")
else:
    print("no is not number")

# does it contain all vowels?
stri = "papepipuo"
stri = stri.lower()
if "a" in stri and "e" in stri and "i" in stri and "o" in stri and"u" in stri:
    print("yeah has vowels")
else:
    print("no has vowels")

# ternary statement
a = 10
b = 2
print("yes") if a < b else print("no")

# compound conditional
import math
numa = 20
if math.sqrt(numa) < 5 or math.sqrt(numa) > 10:
    print("yeah whatever that says")
elif math.sqrt(numa) == 10:
    print("it's ten")

namestr="Kevin"
if namestr.isalpha() and len(namestr)<30:
	print("nice name!")
else:
	namestr=input("Write a real name!")
