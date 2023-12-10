import aes


# convert string to hex array
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


# Input plaint text
plain_text = ["6BC1BEE22E409F96E93D7E117393172A", "AE2D8A571E03AC9C9EB76FAC45AF8E51",
              "30C81C46A35CE411E5FBC1191A0A52EF", "F69F2445DF4F9B17AD2B417BE66C3710",]

# Key
key = "2B7E151628AED2A6ABF7158809CF4F3C"

# Array of round keys
all_round_keys = aes.find_all_round_keys(key)

# Initialization vector
IV = "000102030405060708090a0b0c0d0e0f"


# CBC mode for AES-128 (encryption)
def cbc_encrypt(plain_text, all_round_keys):
    input_block = ''
    output_block = ''
    cipher_blocks = []
    i = 0
    while i < len(plain_text):
        if i == 0:
            input_block = xor_strs(convert_str_to_arr_hex(plain_text[i]), convert_str_to_arr_hex(IV))
            output_block = aes.encrypt(input_block, all_round_keys)
            cipher_blocks.append(output_block)

            print(f'Plain text block {i}: {plain_text[i]}')
            print(f'Input block {i}: {input_block}')
            print(f'Output block {i}: {output_block}')
            print(f'Cipher text block {i}: {cipher_blocks[i]}')
        else:
            input_block = xor_strs(convert_str_to_arr_hex(plain_text[i]), cipher_blocks[i-1])
            output_block = aes.encrypt(input_block, all_round_keys)
            cipher_blocks.append(output_block)

            print(f'Plain text block {i}: {plain_text[i]}')
            print(f'Input block {i}: {input_block}')
            print(f'Output block {i}: {output_block}')
            print(f'Cipher text block {i}: {cipher_blocks[i]}')
        i += 1
    return cipher_blocks


def cbc_decrypt(cipher_text, all_round_keys):
    input_block = ''
    output_block = ''
    plain_blocks = []
    i = 0
    while i < len(cipher_text):
        if i == 0:
            input_block = cipher_text[i]
            output_block = aes.decrypt(input_block, all_round_keys)
            plain_blocks.append(xor_strs(convert_str_to_arr_hex(IV), output_block))

            print(f'Cipher text block {i}: {cipher_text[i]}')
            print(f'Input block {i}: {input_block}')
            print(f'Output block {i}: {output_block}')
            print(f'Plain text block {i}: {plain_blocks[i]}')

        else:
            input_block = cipher_text[i]
            output_block = aes.decrypt(input_block, all_round_keys)
            plain_blocks.append(xor_strs(cipher_text[i - 1], output_block))

            print(f'Cipher text block {i}: {cipher_text[i]}')
            print(f'Input block {i}: {input_block}')
            print(f'Output block {i}: {output_block}')
            print(f'Plain text block {i}: {plain_blocks[i]}')
        i += 1
    return plain_blocks



result_cbc_encrypt = cbc_encrypt(plain_text, all_round_keys)
for i in result_cbc_encrypt:
    print(i)

result_cbc_decrypt = cbc_decrypt(result_cbc_encrypt, all_round_keys)
for i in result_cbc_decrypt:
    print(i)
