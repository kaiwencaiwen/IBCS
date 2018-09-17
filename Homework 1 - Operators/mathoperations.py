# Question 1
print(9 % 7)
print(8 * 4 - 4)
print(bool(4 / 4))
print(abs(-1) * 4 + 10)
print(pow(3, 4) % 4)
print(20 - int(14.5))
print(bool(10 - (5 * int(2.2))))
print(divmod(19, 4))
print(str(5 * 10 - 13 - 5))
print(float((15 + 4 - int(True)) % 4))

# Question 5
print("\n")
print(4 > 3 and 1 < 2)
print(len("Hi") < 3)
print(6 < 8 or 12 > 10)
print(not(7 > 10))
print(5 < 6 and 7 > 8)
print(not(5 < 6 and 7 > 8))
print("A" != "B" and 5 == 10 / 2)
print("A" != "B" and 10 == 5 / 2)

# Question 7
a = int(input("input a:"))
b = int(input("input b:"))
c = int(input("input c:"))
x = []
discriminant = b**2 - 4 * a * c
if discriminant < 0:
    print("no solution")
else:
    x.append((-b + discriminant**0.5) / 2 * a)
    x.append((-b - discriminant**0.5) / 2 * a)
    x = list(set(x))
    print(x)

# Question 8
a = bool(input("input a:"))
b = bool(input("input b:"))
c = bool(input("input c:"))
print((a and b) or (not(a and c)))
