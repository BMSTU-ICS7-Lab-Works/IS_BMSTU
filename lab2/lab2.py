from collections import deque
import random

def rotate(l, n):
    return l[n:] + l[:n]

def encrypt(word, rotor1, rotor2, rotor3):
    res = ''
    count1 = 0
    count2 = 0
    for el in word:
        curind = el
        first_way = rotor3[rotor2.index(rotor1[ord(curind) - 65])]
        reflect = reflector[-reflector.index(first_way)+1]
        back_way = rotor1.index(rotor2[rotor3.index(reflect)])
        res += chr(back_way + 65)
        rotor1 = rotate(rotor1, 1)
        count1 += 1
        if count1 % 26 == 0:
            count1 = 0
            count2 += 1
            rotor2 = rotate(rotor2, 1)
        if count2 % 26 == 0:
            count2 = 0
            rotor3 = rotate(rotor3, 1)
    return res

symbols = [chr(i) for i in range(65, 91)]

#for el in symbols:
 #   print(el, ord(el), sep='/')
rotor1_copy = rotor1 = symbols[:]
rotor2 = symbols[:]
rotor3 = symbols[:]
random.shuffle(rotor1)
random.shuffle(rotor2)
random.shuffle(rotor3)


reflector = symbols[:]
random.shuffle(reflector)

word = input('Введите слово: ')
res = encrypt(word, rotor1, rotor2, rotor3)
print(res)
print(encrypt(res, rotor1_copy, rotor2, rotor3))

    




