from file_searching import File
from crypter import Crypt
import datetime


def main():
    filename = File(input())
    start_time = datetime.datetime.now().microsecond
    msg, k = filename.get_message_k()
    print(Crypt(msg, k).get_encrypt())
    end_time = datetime.datetime.now().microsecond
    print(f'Microseconds: {end_time - start_time}')
    filename1 = File(input())
    start_time = datetime.datetime.now().microsecond
    msg, k = filename1.get_message_k()
    print(Crypt(msg, k).get_decrypt())
    end_time = datetime.datetime.now().microsecond
    print(f'Microseconds: {end_time - start_time}')


if __name__ == '__main__':
    main()
