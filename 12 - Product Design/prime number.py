num = 7


def is_prime(num):
    if type(num) != int:
        return False
    elif num <= 1:
        return False
    else:
        i = 2
        while i < num:
            if (num / i) % 1:
                i += 1
            else:
                return False
    return True


for n in range(1, 20):
    print(n, is_prime(n))
