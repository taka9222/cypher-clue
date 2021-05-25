# ASCII文字列をバイナリリストに変換
def char2bin(char):
    text = []
    for ch in char:
        text += '0'
        text += list(bin(ord(ch)))[2:]
    return text

#リスト内の列入れ替え
def swapcols(text, col1, col2):
    for row in range(4):
        idx1 = 4 * row + col1
        idx2 = 4 * row + col2
        text[idx1], text[idx2] = text[idx2], text[idx1]
    return text

# shift の数だけ左にシフト
def shiftrows(text, shift=[0, 0, 0, 0]):
    for row in range(4):
        idx = range(4 * row, 4 * (row + 1))
        tmp = text[4 * row:4 * (row + 1)]
        text[idx[0]] = tmp[(0 + shift[row]) % 4]
        text[idx[1]] = tmp[(1 + shift[row]) % 4]
        text[idx[2]] = tmp[(2 + shift[row]) % 4]
        text[idx[3]] = tmp[(3 + shift[row]) % 4]
    return text

def xor(text, key):
    result = [0] * 16
    for idx in range(16):
        result[idx] = int(text[idx]) ^ int(key[idx])
    return result

def encrypt(text, char):
    key = char2bin(char)
    text = swapcols(text, 0, 1)
    text = swapcols(text, 2, 3)
    key = swapcols(key, 0, 1)
    key = swapcols(key, 2, 3)
    text = xor(text, key)
    text = shiftrows(text, [0, 3, 2, 1])
    return text

def decrypt(text, char):
    key = char2bin(char)
    text = shiftrows(text, [0, 1, 2, 3])
    text = xor(text, key)
    text = swapcols(text, 0, 1)
    text = swapcols(text, 2, 3)
    key = swapcols(key, 0, 1)
    key = swapcols(key, 2, 3)
    return text

txt = list('1001011110110101')
keys = ['YS', 'BX']
txt = encrypt(txt, keys[0])
txt = encrypt(txt, keys[1])
print(txt)