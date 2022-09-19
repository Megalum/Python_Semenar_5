# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(data):
    encode = '' 
    prev_char = '' 
    count = 1
    for char in data: 
        if char != prev_char:  
            encode += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else: 
        encode += str(count) + prev_char 
        return encode

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

file = open('encode.txt', 'r')
data = ''
for i in file:
    data += i
file.close
file = open('decode.txt', 'w')
file.write(rle_encode(data))
file.close

print(rle_encode(data))
print(rle_decode(rle_encode(data)))