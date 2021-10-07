def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False;
    return True


def encrypt(mess):
    p = list(mess)
    s = ""
    m = mess[0]
    for i in range(2, len(p) + 1):
        if is_prime(i):
            s = s + mess[i - 1]
        else:
            m += mess[i - 1]
    return s + m


def decrypt(mess):
    p = list(mess)
    s = []
    for i in range(2, len(p) + 1):
        if is_prime(i):
            s.append(i - 1)
    old_mess = list(p[len(s):])
    new_mess = list(p[:len(s)])
    for l in s:
        old_mess.insert(l, new_mess.pop(0))
    return ''.join(e for e in old_mess)


def open_for_read(text):
    with open(f"{text}.txt", "r+")as f:
        k, message = f.read().split("\n")
        f.close()
    return k, message


file_name = input()

try:
    open_for_read(file_name)
except FileNotFoundError:
    print('File name not exist please input message to create')
    with open(f"{file_name}.txt", "a+")as f:
        f.write(input('k=') + '\n')
        f.write(input('message='))

k, message = open_for_read(file_name)
for i in range(0, int(k)):
    message = encrypt(message)
print(message)
