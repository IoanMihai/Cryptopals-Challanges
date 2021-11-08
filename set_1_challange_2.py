
hex1 = "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"

result1 = bin(int(hex1, 16))[2:]
result2 = bin(int(hex2, 16))[2:]

if len(result1) > len(result2):
    length = len(result1)
else:
    length = len(result2)

result1 = result1.zfill(length)
result2 = result2.zfill(length)

final = [int(bit1) ^ int(bit2) for bit1, bit2 in zip(result1,result2)]

string_final = "".join([str(bits) for bits in final])

hex_final = hex(int(string_final, 2))[2:]
print(hex_final)
