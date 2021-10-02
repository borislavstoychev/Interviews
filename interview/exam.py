def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False;

    return True


def prime_index(input):
    p = list(input)
    s = ""
    m = input[0]
    for i in range(2, len(p) + 1):
        if is_prime(i):
            s = s + input[i - 1]
        else:
            m += input[i-1]
    return s+m


file = open(f"{input()}.txt", "r")
f = open("bobby.txt", "r")
k, message = f.readline().split(" ")


for i in range(0, int(k)):
    message = prime_index(message)
print(message)
