def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


def get_prime_indexes(index_range):
    prime_indexes = []
    for i in range(2, index_range + 1):
        if is_prime(i):
            prime_indexes.append(i)
    return prime_indexes
