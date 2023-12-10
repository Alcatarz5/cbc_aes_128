WORD_LENGTH = 4

ROUND = 10

S_BOX = (
    (0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76),
    (0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0),
    (0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15),
    (0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75),
    (0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84),
    (0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF),
    (0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8),
    (0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2),
    (0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73),
    (0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB),
    (0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79),
    (0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08),
    (0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A),
    (0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E),
    (0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF),
    (0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16),
)

INV_S_BOX = (
    (0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB),
    (0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB),
    (0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E),
    (0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25),
    (0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92),
    (0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84),
    (0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06),
    (0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B),
    (0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73),
    (0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E),
    (0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B),
    (0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4),
    (0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F),
    (0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF),
    (0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61),
    (0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D),
)

R_CON = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)

MIX_MATRIX = (
    (0x02, 0x03, 0x01, 0x01),
    (0x01, 0x02, 0x03, 0x01),
    (0x01, 0x01, 0x02, 0x03),
    (0x03, 0x01, 0x01, 0x02)
)

INV_MIX_MATRIX = (
    (0x0e, 0x0b, 0x0d, 0x09),
    (0x09, 0x0e, 0x0b, 0x0d),
    (0x0d, 0x09, 0x0e, 0x0b),
    (0x0b, 0x0d, 0x09, 0x0e)
)


def left_shift(arr):
    first_bit = arr[0]
    for i in range(WORD_LENGTH - 1):
        arr[i] = arr[i + 1]
    arr[WORD_LENGTH - 1] = first_bit
    return arr

# print(left_shift(['2', 'a', '6', 'f']))
# output ['a', '6', 'f', '2']


def right_shift(arr):
    last_bit = arr[-1]
    for i in range(WORD_LENGTH - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_bit
    return arr

# print(right_shift(['2', 'a', '6', 'f']))
# output ['f', '2', 'a', '6']


# Galois multiplication
def galois_mult(a, b):
    mult = 0
    for i in range(8):
        if b & 1 == 1:
            mult ^= a
        if a & 0x80:
            a = a << 1 ^ 0x11b
        else:
            a <<= 1
        b >>= 1
    return mult


# Generate 4x4 matrix from hex string array
def generate_4x4_matrix(hex_string):
    hex_string_arr = [hex_string[i:i + WORD_LENGTH] for i in range(0, len(hex_string), WORD_LENGTH)]
    matrix_4x4 = [['' for x in range(WORD_LENGTH)] for y in range(WORD_LENGTH)]
    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            matrix_4x4[i][j] = hex_string_arr[i][j]
    return matrix_4x4

# print(generate_4x4_matrix("0123456789abcdef"))
# Output    [['0', '4', '8', 'c'],
#           ['1', '5', '9', 'd'],
#           ['2', '6', 'a', 'e'],
#           ['3', '7', 'b', 'f']]


# Convert int array to hex array
def convert_int_arr_to_hex(int_arr):
    hex_arr = ['' for x in range(len(int_arr))]
    for i in range(len(int_arr)):
        hex_arr[i] = "{:02x}".format(int_arr[i])
    return hex_arr

# arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(convert_int_arr_to_hex(arr))
# Output ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f']


# Convert hex array to int array
def convert_matrix_to_int(matrix):
    int_matrix = [[0 for x in range(WORD_LENGTH)] for y in range(WORD_LENGTH)]
    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            int_matrix[i][j] = int(matrix[i][j], 16)
    return int_matrix

# arr_1 = [['00', '04', '08', '0c'], ['01', '05', '09', '0d'], ['02', '06', '0a', '0e'], ['03', '07', '0b', '0f']]
# print(convert_matrix_to_int(arr_1))
# Output [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]]


# XOR with round key
def add_round_key(m1_hex, m2_hex):
    matrix_4x4 = [['' for x in range(WORD_LENGTH)] for y in range(WORD_LENGTH)]
    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            val_1 = int(m1_hex[j][i], 16)
            val_2 = int(m2_hex[j][i], 16)
            res = val_1 ^ val_2
            matrix_4x4[j][i] = "{:02x}".format(res)
    return matrix_4x4

# arr_1 = [['0', '4', '8', 'c'], ['1', '5', '9', 'd'], ['2', '6', 'a', 'e'], ['3', '7', 'b', 'f']]
# arr_2 = [['1', '1', '8', 'c'], ['1', '5', '9', 'd'], ['2', '6', 'a', 'e'], ['3', '7', 'b', 'f']]
# print(add_round_key(arr_1, arr_2))
# Output    [['01', '05', '00', '00'],
#           ['00', '00', '00', '00'],
#           ['00', '00', '00', '00'],
#           ['00', '00', '00', '00']]


# Substitution bytes in matrix 4x4 with s_box(if flag=TRUE) and inv_s_box otherwise
def substitute_bytes(matrix, flag):
    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            int_val = matrix[j][i]
            if flag:
                s_box_val_int = S_BOX[int(int_val[0], 16)][int(int_val[1], 16)]
            else:
                s_box_val_int = INV_S_BOX[int(int_val[0], 16)][int(int_val[1], 16)]
            s_box_val_hex = "{:02x}".format(s_box_val_int)
            matrix[j][i] = s_box_val_hex
    return matrix

# arr_1 = [['00', '04', '08', '0c'], ['01', '05', '09', '0d'], ['02', '06', '0a', '0e'], ['03', '07', '0b', '0f']]
# print(substitute_bytes(arr_1, True))
# Output [['63', 'f2', '30', 'fe'],
#        ['7c', '6b', '01', 'd7'],
#        ['77', '6f', '67', 'ab'],
#        ['7b', 'c5', '2b', '76']]


# Shift rows in matrix (using for encrypt)
# In 1 row left shift for 1 pos
# In 2 row left shift for 2 pos
# In 3 row left shift for 3 pos
def shift_row(matrix):
    res_matrix = [['' for x in range(WORD_LENGTH)] for y in range(WORD_LENGTH)]

    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            res_matrix[i][j] = matrix[j][i]

    res_matrix[1] = left_shift(res_matrix[1])

    res_matrix[2] = left_shift(res_matrix[2])
    res_matrix[2] = left_shift(res_matrix[2])

    res_matrix[3] = left_shift(res_matrix[3])
    res_matrix[3] = left_shift(res_matrix[3])
    res_matrix[3] = left_shift(res_matrix[3])

    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            matrix[i][j] = res_matrix[j][i]

    return matrix


# arr_1 = [['00', '04', '08', '0c'], ['01', '05', '09', '0d'], ['02', '06', '0a', '0e'], ['03', '07', '0b', '0f']]
# print(shift_row(arr_1))
# Output [['0', '4', '8', 'c'],
#       ['5', '9', 'd', '1'],
#       ['a', 'e', '2', '6'],
#       ['f', '3', '7', 'b']]


# Shift rows in matrix (using for decrypt)
# In 1 row right shift for 1 pos
# In 2 row right shift for 2 pos
# In 3 row right shift for 3 pos
def shift_row_inv(matrix):
    res_matrix = [['' for x in range(WORD_LENGTH)] for y in range(WORD_LENGTH)]

    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            res_matrix[i][j] = matrix[j][i]

    # print(res_matrix)

    res_matrix[1] = right_shift(res_matrix[1])

    # print(res_matrix[1])

    res_matrix[2] = right_shift(res_matrix[2])
    res_matrix[2] = right_shift(res_matrix[2])

    # print(res_matrix[2])

    res_matrix[3] = right_shift(res_matrix[3])
    res_matrix[3] = right_shift(res_matrix[3])
    res_matrix[3] = right_shift(res_matrix[3])

    # print(res_matrix[3])

    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            matrix[i][j] = res_matrix[j][i]

    return matrix


# Mix given column using MIX_MATRIX (using for encrypt)
def mix_column(column):
    temp_column = [0, 0, 0, 0]
    res_iter = 0
    for i in MIX_MATRIX:
        for j in range(WORD_LENGTH):
            temp_column[res_iter] ^= galois_mult(i[j], column[j])
        res_iter += 1
    return temp_column

# column_1 = [0, 4, 8, 12]
# print(mix_column(column_1))
# Output [8, 28, 0, 20]


#  Mix given column using INV_MIX_MATRIX (using for decrypt)
def inv_mix_column(column):
    temp_column = [0, 0, 0, 0]
    res_iter = 0
    for i in INV_MIX_MATRIX:
        for j in range(WORD_LENGTH):
            temp_column[res_iter] ^= galois_mult(i[j], column[j])
        res_iter += 1
    return temp_column

# column_1 = [0, 4, 8, 12]
# print(inv_mix_column(column_1))
# Output [40, 60, 32, 52]


# Mix columns (if flag=TRUE using for encrypt else for decrypt)
def mix_columns(matrix, flag):
    int_matrix = convert_matrix_to_int(matrix)
    col_based = [[0 for x in range(WORD_LENGTH)] for y in range(WORD_LENGTH)]
    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            col_based[i][j] = int_matrix[i][j]
    # print(col_based)
    if flag:
        for i in range(WORD_LENGTH):
            col_based[i] = mix_column(col_based[i])
    else:
        for i in range(WORD_LENGTH):
            col_based[i] = inv_mix_column(col_based[i])
    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            matrix[i][j] = '{:02x}'.format(col_based[i][j])
            int_matrix[i][j] = col_based[i][j]
    return matrix

# arr_1 = [['00', '04', '08', '0c'], ['01', '05', '09', '0d'], ['02', '06', '0a', '0e'], ['03', '07', '0b', '0f']]
# print(mix_columns(arr_1, True))
# Output [[2, 6, 10, 14],
#       [7, 3, 15, 11],
#       [0, 4, 8, 12],
#       [5, 1, 13, 9]]


# Generate round key
def find_all_round_keys(main_key_val):
    # Create array from 44 of [0,0,0,0]
    w = [['' for x in range(WORD_LENGTH)] for y in range(44)]

    temp_arr = []

    # Adding in temporary array main key 2 values each ['00', '01' ...
    for l in range(0, len(main_key_val), 2):
        temp_arr.append(main_key_val[l:l + 2])

    # Filling 4 rows each w matrix from temp array
    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            w[i][j] = temp_arr[(i * WORD_LENGTH) + j]

    temp_arr = []

    round_num = 0
    for word_num in range(WORD_LENGTH, WORD_LENGTH * (ROUND + 1)):

        if word_num % WORD_LENGTH == 0:
            round_num += 1
            temp_w = [0, 0, 0, 0]
            for i in range(4):
                temp_w[i] = w[word_num - 1][i]
            temp_w = left_shift(temp_w)

            s_box_arr = []

            for i in range(WORD_LENGTH):
                if len(temp_w[i]) == 1:
                    temp_w[i] = '0' + temp_w[i]
                s_box_index = [temp_w[i][0], temp_w[i][1]]
                s_box_arr.append(hex(S_BOX[int(s_box_index[0], 16)][int(s_box_index[1], 16)]))

            round_cont_arr = [0, 0, 0, 0]
            round_cont_arr[0] = round_cont_arr[0] + R_CON[round_num]
            for i in range(WORD_LENGTH):
                s_box_arr[i] = int(s_box_arr[i], 16) ^ round_cont_arr[i]

            for i in range(WORD_LENGTH):
                int_val = int(w[word_num - 4][i], 16)
                w[word_num][i] = hex(int_val ^ s_box_arr[i])[2:]

        else:
            for i in range(WORD_LENGTH):
                int_val_minus_1 = int(w[word_num - 1][i], 16)
                int_val_minus_4 = int(w[word_num - 4][i], 16)
                w[word_num][i] = hex(int_val_minus_1 ^ int_val_minus_4)[2:]

    temp_round_keys_hex = []

    for i in range(WORD_LENGTH * (ROUND + 1)):
        for j in range(WORD_LENGTH):
            temp_round_keys_hex.append("{:02x}".format(int(w[i][j], 16)))

    round_keys_in_hex = [temp_round_keys_hex[i * (WORD_LENGTH * WORD_LENGTH):(i + 1) * (WORD_LENGTH * WORD_LENGTH)]
                         for i in range(
            (len(temp_round_keys_hex) + (WORD_LENGTH * WORD_LENGTH) - 1) // (WORD_LENGTH * WORD_LENGTH))]

    return round_keys_in_hex

# for i in find_all_round_keys("000102030405060708090a0b0c0d0e0f"):
#     print(i)
# Output:
#     ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f']
#     ['d6', 'aa', '74', 'fd', 'd2', 'af', '72', 'fa', 'da', 'a6', '78', 'f1', 'd6', 'ab', '76', 'fe']
#     ['b6', '92', 'cf', '0b', '64', '3d', 'bd', 'f1', 'be', '9b', 'c5', '00', '68', '30', 'b3', 'fe']
#     ['b6', 'ff', '74', '4e', 'd2', 'c2', 'c9', 'bf', '6c', '59', '0c', 'bf', '04', '69', 'bf', '41']
#     ['47', 'f7', 'f7', 'bc', '95', '35', '3e', '03', 'f9', '6c', '32', 'bc', 'fd', '05', '8d', 'fd']
#     ['3c', 'aa', 'a3', 'e8', 'a9', '9f', '9d', 'eb', '50', 'f3', 'af', '57', 'ad', 'f6', '22', 'aa']
#     ['5e', '39', '0f', '7d', 'f7', 'a6', '92', '96', 'a7', '55', '3d', 'c1', '0a', 'a3', '1f', '6b']
#     ['14', 'f9', '70', '1a', 'e3', '5f', 'e2', '8c', '44', '0a', 'df', '4d', '4e', 'a9', 'c0', '26']
#     ['47', '43', '87', '35', 'a4', '1c', '65', 'b9', 'e0', '16', 'ba', 'f4', 'ae', 'bf', '7a', 'd2']
#     ['54', '99', '32', 'd1', 'f0', '85', '57', '68', '10', '93', 'ed', '9c', 'be', '2c', '97', '4e']
#     ['13', '11', '1d', '7f', 'e3', '94', '4a', '17', 'f3', '07', 'a7', '8b', '4d', '2b', '30', 'c5']


def encrypt(text_hex, all_round_keys):
    state_matrix = generate_4x4_matrix(text_hex)
    # print(f'Round[{0}].input: {state_matrix}')
    round_n_matrix = generate_4x4_matrix(all_round_keys[0])
    # print(f'Round[0].k_sch: {round_n_matrix}')
    current_matrix = add_round_key(state_matrix, round_n_matrix)
    # print(f'Round[1].start: {current_matrix}')

    for i in range(1, ROUND):
        current_matrix = substitute_bytes(current_matrix, True)
        # print(f'Round[{i}].s_box: {current_matrix}')
        current_matrix = shift_row(current_matrix)
        # print(f'Round[{i}].s_row: {current_matrix}')
        current_matrix = mix_columns(current_matrix, True)
        # print(f'Round[{i}].m_col: {current_matrix}')
        round_n_keys = generate_4x4_matrix(all_round_keys[i])
        # print(f'Round[{i}].k_sch: {round_n_keys}')
        current_matrix = add_round_key(current_matrix, round_n_keys)
        # print(f'Round[{i + 1}].start: {current_matrix}')

    current_matrix = substitute_bytes(current_matrix, True)
    # print(f'Round[10].s_box: {current_matrix}')
    current_matrix = shift_row(current_matrix)
    # print(f'Round[10].s_row: {current_matrix}')
    round_n_keys = generate_4x4_matrix(all_round_keys[10])
    # print(f'Round[10].k_sch: {round_n_keys}')
    cipher_text_matrix = add_round_key(current_matrix, round_n_keys)
    # print(f'Round[10].output: {cipher_text_matrix}')

    cipher_text = []
    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            cipher_text.append(cipher_text_matrix[i][j])
            # print(cipher_text)

    return cipher_text

# Example from page 36
# text_1 = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99", "aa", "bb", "cc", "dd", "ee", "ff"]
# key = "000102030405060708090a0b0c0d0e0f"
# all_keys = find_all_round_keys(key)
# print(encrypt(text_1, all_keys))


def decrypt(cipher_text, all_round_keys):
    current_matrix = generate_4x4_matrix(cipher_text)
    # print(f'Round[0].iinput: {cipher_text}')
    round_n_matrix = generate_4x4_matrix(all_round_keys[10])
    # print(f'Round[0].ik_sch: {round_n_matrix}')

    current_matrix = add_round_key(current_matrix, round_n_matrix)
    # print(f'Round[1].istart: {current_matrix}')
    current_matrix = shift_row_inv(current_matrix)
    # print(f'Round[1].is_row: {current_matrix}')
    current_matrix = substitute_bytes(current_matrix, False)
    # print(f'Round[1].is_box: {current_matrix}')

    i = 9
    while i > 0:
        round_n_matrix = generate_4x4_matrix(all_round_keys[i])
        # print(f'Round[{10 - i}].ik_sch: {round_n_matrix}')
        current_matrix = add_round_key(current_matrix, round_n_matrix)
        # print(f'Round[{10 - i}].istart: {current_matrix}')
        current_matrix = mix_columns(current_matrix, False)
        # print(f'Round[{11 - i}].m_col: {current_matrix}')
        current_matrix = shift_row_inv(current_matrix)
        # print(f'Round[{11 - i}].is_row: {current_matrix}')
        current_matrix = substitute_bytes(current_matrix, False)
        # print(f'Round[{11 - i}].is_box: {current_matrix}')
        i -= 1

    round_n_matrix = generate_4x4_matrix(all_round_keys[0])
    # print(f'Round[10].ik_sch: {round_n_matrix}')
    plain_text_matrix = add_round_key(current_matrix, round_n_matrix)
    # print(f'Round[10].ioutput: {plain_text_matrix}')

    plain_text = []
    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            plain_text.append(plain_text_matrix[i][j])
            # print(plain_text)

    return plain_text


# if __name__ == '__main__':

    # text_2 = encrypt(text_1, all_keys)
    # print(text_2)
    # print(decrypt(text_2, all_keys))
    # [[99, 83, 224, 140], [9, 96, 225, 4], [205, 112, 183, 81], [186, 202, 208, 231]]
    # arr = [['63', '53', 'e0', '8c'], ['09', '60', 'e1', '04'], ['cd', '70', 'b7', '51'], ['ba', 'ca', 'd0', 'e7']]
    # print(mix_columns(arr, True))
    # arr = [['63', 'ca', 'b7', '04'], ['09', '53', 'd0', '51'], ['cd', '60', 'e0', 'e7'], ['ba', '70', 'e1', '8c']]
    # print(shift_row(arr))

    # print(arr)
    # arr_2 = [['' for x in range(WORD_LENGTH)] for y in range(WORD_LENGTH)]
    # print(arr_2)
    # for i in range(WORD_LENGTH):
    #     for j in range(WORD_LENGTH):
    #         arr_2[j][i] = arr[i][j]
    # print(arr_2)
    # print(shift_row(arr_2))
    # for i in range(WORD_LENGTH):
    #     for j in range(WORD_LENGTH):
    #         arr[j][i] = arr_2[i][j]
    # print(arr)

    # val_1 = galois_mult(2, 99)
    # print(val_1)
    # val_2 = galois_mult(3, 9)
    # print(val_2)
    # val_3 = galois_mult(1, 205)
    # print(val_3)
    # val_4 = galois_mult(1, 186)
    # print(val_4)
    #
    # print(f'{hex(val_1)} + {hex(val_2)} ^ {hex(val_3)} ^ {hex(val_4)}')
    # 5f 72 64 15 57 f5 bc 92 f7 be 3b 29 1d b9 f9 1a
    # print(galois_mult(2,86))
    # print(mix_column(column_1))
    # print(convert_matrix_to_int(arr))

    # arr = [['bd', 'b5', '21', '89'], ['f2', '61', 'b6', '3d'], ['0b', '10', '7c', '9e'], ['8b', '6e', '77', '6e']]
    # current_matrix = shift_row_inv(arr)
    # print(current_matrix)


# ['69', '6a', 'd8', '70', 'c4', '7b', 'cd', 'b4', 'e0', '04', 'b7', 'c5', 'd8', '30', '80', '5a']
# 69 c4 e0 d8 6a 7b 04 30 d8 cd b7 80 70 b4 c5 5a
