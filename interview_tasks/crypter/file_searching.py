class File:
    def __init__(self, name):
        self.name = name

    def get_message_k(self):
        try:
            with open(f"{self.name}.txt", "r+")as f:
                k, *message = f.read().split("\n")
                f.close()
            return message, k
        except FileNotFoundError:
            print('File name can not be found please input correct file')
            return File(input()).get_message_k()
