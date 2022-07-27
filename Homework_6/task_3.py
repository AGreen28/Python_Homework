'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''

with open('sourse_file.txt') as sf:
    print(*sf)
with open('sourse_file.txt') as sf:
    sf = sf.read()

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1 
    else:
        encoding += str(count) + prev_char
        return encoding

encoded_val = rle_encode(sf)
print(encoded_val)
encoded_file = open('RLE_encode.txt', 'w')
encoded_file.write(encoded_val)
encoded_file.close()

with open('RLE_encode.txt') as en:
    en = en.read()

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

decoded_val = rle_decode(en)
print(decoded_val)
decoded_file = open('RLE_decode.txt', 'w')
decoded_file.write(decoded_val)
decoded_file.close()