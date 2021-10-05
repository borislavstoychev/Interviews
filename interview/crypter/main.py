from crypter.decrypt_message import Decrypt
from crypter.encrypt_message import Encrypt
from crypter.file_searching import File


def main():
    filename = File(input())
    k, msg = filename.get_message_k()
    print(Encrypt(k, msg).get_encrypt())


if __name__ == '__main__':
    main()