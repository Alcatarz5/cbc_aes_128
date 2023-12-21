from secrets import token_hex
import aes

plain_text = ["6BC1BEE22E409F96E93D7E117393172A", "AE2D8A571E03AC9C9EB76FAC45AF8E51",
              "30C81C46A35CE411E5FBC1191A0A52EF", "F69F2445DF4F9B17AD2B417BE66C3710",]

key = "2B7E151628AED2A6ABF7158809CF4F3C"

all_round_keys = aes.find_all_round_keys(key)

def convert_str_to_arr_hex(input_str):
    arr = []
    for i in range(0, len(input_str), 2):
        arr.append(input_str[i:i + 2])
    return arr

# XOR 2 strings
def xor_strs(str1, str2):
    ret = []
    for i in range(16):
        y = int(str1[i], 16) ^ int(str2[i], 16)
        if len(hex(y)) == 3:
            ret.append('0' + hex(y)[2:])
        else:
            ret.append(hex(y)[2:])
    return ret

def generate_random():
    result = convert_str_to_arr_hex(token_hex(16))
    return result

def pbr_encrypt(plaintext_block, all_keys, r):
    return r + xor_strs(convert_str_to_arr_hex(plaintext_block), aes.encrypt(r, all_keys))

def pbr_decrypt(chiphertext_block, all_keys):
    return xor_strs(aes.encrypt(chiphertext_block[:16], all_keys), chiphertext_block[16:])


chipher_text = []
result = []


print('PBR encryption:')
for i, plaintext_block in enumerate(plain_text):
    random_string = generate_random()
    chipher_text.append(pbr_encrypt(plaintext_block, all_round_keys, random_string))
    print(chipher_text[i])

print('PBR decryption:')
for i, chiphertext_block in enumerate(chipher_text):
    result.append(xor_strs(aes.encrypt(chiphertext_block[:16], all_round_keys), chiphertext_block[16:]))
    print(result[i])
