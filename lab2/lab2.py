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
        first_way = rotor3[rotor2.index(rotor1[ord(curind)])]
        reflect = reflector[-reflector.index(first_way)+1]
        back_way = rotor1.index(rotor2[rotor3.index(reflect)])
        res += chr(back_way)
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

# шифруем/расшифровываем файл
def encrypt_file(in_file, out_file, rotor1, rotor2, rotor3):
    try:
        input_file = open(in_file, 'rb')
    except FileNotFoundError:
        print("No such file! Try again!")
        return

    output_file = open(out_file, 'wb')
    read_byte = input_file.read(1000)
    file_text = ''

    while read_byte:
        byte_encrypt = b""
        for s in read_byte:
            file_text += chr(s)
        file_text = encrypt(file_text, rotor1, rotor2, rotor3)
        for ch in file_text:
            byte_encrypt += bytes([ord(ch)])
        output_file.write(byte_encrypt)
        read_byte = input_file.read(1000)

    input_file.close()
    output_file.close()
    return file_text

symbols = [chr(i) for i in range(0, 255)]

rotor1_copy = rotor1 = symbols[:]
rotor2_copy = rotor2 = symbols[:]
rotor3_copy = rotor3 = symbols[:]
random.shuffle(rotor1)
random.shuffle(rotor2)
random.shuffle(rotor3)


reflector = symbols[:]
random.shuffle(reflector)


print("Enter file_name in: ")
f_in = input()
print("Enter file_name encrypt: ")
f_out = input()
print("Enter file_name result: ")
f_res = input()
text = encrypt_file(f_in, f_out, rotor1, rotor2, rotor3)
print("\nЗашифрованный текст:\n")
print(text)
textEncrypt = encrypt_file(f_out, f_res, rotor1_copy, rotor2_copy, rotor3_copy)

print("\nРасшифрованный текст:\n")
print(textEncrypt)
