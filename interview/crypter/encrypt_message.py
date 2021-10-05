from crypter.prime_checker import is_prime


class Encrypt:
    def __init__(self, message, k):
        self.message = message
        self.k = k

    def __encrypt(self):
        p = list(self.message)
        s = ""
        m = self.message[0]
        for i in range(2, len(p) + 1):
            if is_prime(i):
                s = s + self.message[i - 1]
            else:
                m += self.message[i - 1]
        return s + m

    def get_encrypt(self):
        for i in range(0, int(self.k)):
            self.message = self.__encrypt()
        return self.message