from interview_tasks.crypter.prime_checker import get_prime_indexes


class Crypt:
    def __init__(self, message, k):
        self.message = message
        self.k = int(k)

    def __encrypt(self):
        new_message = []
        for m in self.message:
            p = list(m)
            for i, l in enumerate(get_prime_indexes(len(m))):
                p.insert(i, p.pop(l-1))
            new_message.append("".join(e for e in p))
        return new_message

    def get_encrypt(self):
        for i in range(0, self.k):
            self.message = self.__encrypt()
        return "\n".join(self.message)

    def __decrypt(self):
        old_message = []
        for m in self.message:
            prime_indexes_d = get_prime_indexes(len(m))
            p = list(m[len(prime_indexes_d):])
            for i, l in enumerate(prime_indexes_d):
                p.insert(l-1, m[i])
            old_message.append(''.join(e for e in p))
        return old_message

    def get_decrypt(self):
        for i in range(0, self.k):
            self.message = self.__decrypt()
        return "\n".join(self.message)
