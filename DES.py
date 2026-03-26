#IP置换
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
#IP反置换
IP_INV = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]
E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]
P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]
#S盒
S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]
SHIFT_TABLE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def permute(block, table):#按字典置换
    return [block[x - 1] for x in table]
def left_shift(key, n):#左移
    return key[n:] + key[:n]
def xor(a, b):#异或
    return [x ^ y for x, y in zip(a, b)]
def s_box(block):#S盒操作
    result = []
    tmp=[0,0,0,0]
    for i in range(8):
        s_box = S_BOXES[i]
        row = block[i * 6] *2 + block[i * 6 + 5]#行
        col = block[i * 6 + 1] * 8 + block[i * 6 + 2] * 4 + block[i * 6 + 3] * 2 + block[i * 6 + 4]#列
        val = s_box[row][col]
        for k in range(4):
            tmp[3-k]=val%2
            val//=2
        result.extend(tmp)
    return result
def subkey(key):#密钥生成
    key = permute(key, PC1)#PC1置换
    left, right = key[:28], key[28:]#分成28位
    subkeys = []
    for i in range(16):
        left = left_shift(left, SHIFT_TABLE[i])#左移置换
        right = left_shift(right, SHIFT_TABLE[i])
        combined = left + right
        subkey = permute(combined, PC2)#PC2置换
        subkeys.append(subkey)
    return subkeys
def pkcs7pad(data, block_size):#PKCS7填充
    padding_len = block_size - len(data) % block_size
    padding = bytes([padding_len] * padding_len)
    return data + padding
def pkcs7unpad(data):#PKCS7去除填充
    padding_len = data[-1]
    return data[:-padding_len]
def descrypt(block, subkeys,mode):#加解密
    if mode=='1':
        ED=1
        ADD=0
    elif mode=='2':
        ED=-1
        ADD=-1
    block = permute(block, IP)#初始IP置换
    for i in range(16):
        left, right = block[:32], block[32:]
        expanded = permute(right, E)#扩展
        xored = xor(expanded, subkeys[i*ED+ADD])#与生成密钥异或
        s_boxed = s_box(xored)#S盒置换
        permuted = permute(s_boxed, P)#P盒置换
        new_right = xor(left, permuted)#与左半边异或
        block = right + new_right
    block = block[32:] + block[:32]
    block = permute(block, IP_INV)#逆IP置换
    return block
def encryptstring(plaintext, key):#加密+编码
    key=pkcs7pad(bytes(key,"utf-8"),8)#密钥填充
    key = bytes.fromhex(key.hex())
    key = [int(b) for b in ''.join(format(x, '08b') for x in key)]
    subkeys = subkey(key)
    plaintext = plaintext.encode('utf-8')
    plaintext = pkcs7pad(plaintext, 8)
    blocks = [plaintext[i:i+8] for i in range(0, len(plaintext), 8)]
    ciphertext = b''
    for block in blocks:#分成块处理
        block = [int(b) for b in ''.join(format(x, '08b') for x in block)]
        encrypted_block = descrypt(block, subkeys,'1')
        ciphertext += bytes(int(''.join(map(str, encrypted_block[i:i+8])), 2) for i in range(0, 64, 8))
    #return bytes.fromhex(ciphertext.hex())
    return ciphertext.hex()
def decryptstring(ciphertext, key):#解密+编码
    key=pkcs7pad(bytes(key,"utf-8"),8)
    key = bytes.fromhex(key.hex())
    key = [int(b) for b in ''.join(format(x, '08b') for x in key)]
    subkeys = subkey(key)
    ciphertext = bytes.fromhex(ciphertext)
    blocks = [ciphertext[i:i+8] for i in range(0, len(ciphertext), 8)]
    plaintext = b''
    for block in blocks:
        block = [int(b) for b in ''.join(format(x, '08b') for x in block)]
        decrypted_block = descrypt(block, subkeys,'2')
        plaintext += bytes(int(''.join(map(str, decrypted_block[i:i+8])), 2) for i in range(0, 64, 8))
    plaintext = pkcs7unpad(plaintext)
    return plaintext.decode('utf-8')

#plaintext = input('密文:')
#key = input('密钥:')

key="feistel"
plaintext="Hi,this is DES!"

encrypted = encryptstring(plaintext, key)
print(encrypted)

plaintext="4d77d60db619f9e850330c5b60052dcd"
decrypted = decryptstring(plaintext, key)
print(decrypted)