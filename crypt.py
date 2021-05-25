# encrypter for polyalphabetic substitution

Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# word = "ztvglkdbglruhabtuoz"
# word = "jcwsvlivlvgsjjfjcwcvl"

word = "lafluiwoywpadufhsnbvswvndzqdufrbpluyqplwlphzrluedubsymiprdij\
htyqucuzylkerskhzbuhuluekpqfoylyssamwocwhzolgdtddppofddtgopy\
udgwoyosdrykvvdvlaulrzygwpljzyqkyptwvljiafhhswomuvddaplmjlue\
pvlrnpdwfxwmqafhzseqcfagqdfljflhldswclmqlfxubulbdubvpvwfqhwy\
uhrhjgsocuzzxagfvlilqvafdarkpqlzcqaguljbuczampl"

# key = "flash"
# key = "pur"
key = "cgx"
encrypted = ""

word = list(word)
key = list(key)

for i in range(len(word)):
    key_idx = i % len(key)
    if key[key_idx] == '*':
        encrypted += '*'
    else:
        idx = (Alphabet.index(word[i]) - Alphabet.index(key[key_idx]) - 1) % len(Alphabet)
        encrypted += Alphabet[idx]

print(encrypted)