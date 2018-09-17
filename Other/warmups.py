# 0914
import math
print(str(52) + bin(52) + hex(52))

print('*' * 1)
print('*' * 2)
print('*' * 3)
print('*' * 4)
print('*' * 5)

for n in range(5):
    print('*' * (n + 1))

print(2**11)

a = 5
for n in range(4):
    a *= 2
print(a)

#...or
print(round(5**math.log(80, 5)))
# no because 36/3=12 which is a 3*2*2

# 0917
my_str = "hello"
my_int = 3
my_float = 3.14159
my_bool = False

print(type(my_str))
print(type(my_int))
print(type(my_float))
print(type(my_bool))

print(bool(my_int))
print(bool(my_float))

print(int(my_bool) + int(my_float))

print(bin(my_int))
print(hex(my_int))

# ASCII Order
print(ord("A"))
print(chr(65))

print(my_int << 1)
print(my_int & 0)
