import math


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


prime_less_than_100 = {num for num in range(2, 100) if is_prime(num)}
print(prime_less_than_100)