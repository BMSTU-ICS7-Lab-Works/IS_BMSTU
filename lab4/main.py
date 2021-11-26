from random import choices, choice, randint
from math import sqrt
from base64 import b32encode, b32decode

_end = 100


def getListSimpleNumbers(n):
    listNumber = [num for num in range(2, n + 1)]

    for num in range(2, int(sqrt(n + 1)) + 1):
        for j in range(len(listNumber)):
            if j >= len(listNumber):
                break
            if num != listNumber[j] and listNumber[j] % num == 0:
                listNumber.pop(j)

    return listNumber

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a or b


def find_e(a):
    b = randint(0, _end)
    while (gcd(a, b) != 1):
        b = randint(0, _end)
    return b


def find_d(e, phi_n):
    k = 0
    while ((k * phi_n + 1) % e != 0):
        k += 1
    return (k * phi_n + 1) // e


def RSA_params():
    p, q = choices(getListSimpleNumbers(_end), k = 2)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = find_e(phi_n)  # открытый
    d = find_d(e, phi_n)  # закрытый

    return n, e, d


def RSA(sym, n, e, d, enc=True):
    if (enc):
        return pow(sym, e, n)
    else:
        return pow(sym, d, n)


def RSA_string(string, n, e, d, enc=True):
    res = ""
    for char in string:
        ch = RSA(ord(char), n, e, d, enc)
        res += chr(ch)
    return res


def main():
    filename = input("Введите имя файла: ")
    file_read = open(filename, 'rb')

    n, e, d = RSA_params()

    data = b32encode(file_read.read())
    str = data.decode("ascii")

    str_enc = RSA_string(str, n, e, d)
    with open(filename.split('.')[0] + ".encrypted", 'w', encoding="utf-8") as file:
        file.write(str_enc)

    str_dec = RSA_string(str_enc, n, e, d, False)
    with open(filename.split('.')[0] + "_decrypted.rar", 'wb') as file:
        file.write(b32decode(str_dec))


if __name__ == "__main__":
    main()