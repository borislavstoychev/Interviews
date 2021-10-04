from crypter.crypt_message import Crypt
from crypter.file_searching import File


def main():
    filename = File(input())
    k, msg = filename.get_message_k()
    print(Crypt(k, msg).get_crypt())


if __name__ == '__main__':
    main()