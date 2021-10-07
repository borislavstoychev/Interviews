from interview_tasks.crypter.prime_checker import is_prime


class Decrypt:
    def __init__(self, message, k):
        self.message = message
        self.k = k

    def __decrypt(self):
        p = list(self.message)
        s = []
        for i in range(2, len(p) + 1):
            if is_prime(i):
                s.append(i - 1)
        old_mess = list(p[len(s):])
        new_mess = list(p[:len(s)])
        for l in s:
            old_mess.insert(l, new_mess.pop(0))
        return ''.join(e for e in old_mess)

    def get_decrypt(self):
        for i in range(0, int(self.k)):
            self.message = self.__decrypt()
        return self.message




