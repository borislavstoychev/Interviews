class File:
    def __init__(self, name):
        self.name = name

    def __open_for_read(self):
        with open(f"{self.name}.txt", "r+")as f:
            k, message = f.read().split("\n")
            f.close()
        return message, k

    def get_message_k(self):
        try:
            self.__open_for_read()
        except FileNotFoundError:
            print('File name not exist please input message to create')
            with open(f"{self.name}.txt", "a+")as f:
                f.write(input('k=') + "\n")
                f.write(input('message='))
        return self.__open_for_read()
