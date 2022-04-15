ZONES = ('com', 'ru', 'net', 'org', 'info', 'cn',
         'es', 'top', 'au', 'pl', 'it', 'uk', 'tk', 'ml',
         'ga', 'cf', 'us', 'xyz', 'top', 'site', 'win', 'bid')

HOMOGLYPHS = {
    'o': ('0',),
    'i': ('1',),


}

import string
import socket
import threading


def method_1(word: str) -> list:
    """
    Insert dot
    :param word:
    :return list:
    """
    pass


def method_2(word: str) -> list:
    """
    Delete char
    :param word:
    :return:
    """
    pass


def method_3(word: str) -> list:
    """
     Homoglyph
    :param word:
    :return:
    """
    pass


def method_4(word: str) -> list:
    """
     Append char
    :param word:
    :return list:
    """
    return [word + ch for ch in string.ascii_lowercase]


def gethost(name, ext):
    try:
        data = socket.gethostbyname_ex(f'{name}.{ext}')
    except Exception:
        data = 'none'
    print(data)


if __name__ == '__main__':
    word = 'anime'
    for name in method_4(word):
        for ext in ZONES:
            thread = threading.Thread(target=gethost, args=(name, ext))
            thread.start()
            thread.join()

