def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

numbers = [10, 15, 17, 19, 21, 23, 29, 30]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)
