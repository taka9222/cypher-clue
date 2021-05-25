# alphabet frequency analyzer
from itertools import product

word = "AJLPNYRJZJFLZYASGSKQGSMMEJKEJPFSVLPJLKKEJELNNSPZKYNNYGNSGASGYZJGAKEYZYGASVW\
NJKSWSKECNLUJZKEJZEYCYZWSVOEKLGAHYKKJAZEJNYJZLKLGUESPPJLAFHSPZJLFSVGJRJPYTL\
OYGJALZMJJKJPZUESSGJPLUEYNATYOEKZLYNEJPKMSEVGAPJAKSGZGLTJEYZCLGYSNL"

word = "LAFLUIWOYWPADUFHSNBVSWVNDZQDUFRBPLUYQPLWLPHZRLUEDUBSYMIPRDIJ\
HTYQUCUZYLKERSKHZBUHULUEKPQFOYLYSSAMWOCWHZOLGDTDDPPOFDDTGOPY\
UDGWOYOSDRYKVVDVLAULRZYGWPLJZYQKYPTWVLJIAFHHSWOMUVDDAPLMJLUE\
PVLRNPDWFXWMQAFHZSEQCFAGQDFLJFLHLDSWCLMQLFXUBULBDUBVPVWFQHWY\
UHRHJGSOCUZZXAGFVLILQVAFDARKPQLZCQAGULJBUCZAMPL"

Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Alphabet_d = ['{}{}'.format(x, y) for x, y in product(Alphabet, Alphabet)]
Alphabet_t = ['{}{}'.format(x, y) for x, y in product(Alphabet, Alphabet_d)]
frequency = {}
frequency_d = {}
frequency_t = {}

display_num = 8

for i in range(len(Alphabet)):
    count = word.lower().count(Alphabet[i])
    if count != 0:
        frequency[Alphabet[i]] = count

for i in range(len(Alphabet_d)):
    count = word.lower().count(Alphabet_d[i])
    if count != 0:
        frequency_d[Alphabet_d[i]] = count

for i in range(len(Alphabet_t)):
    count = word.lower().count(Alphabet_t[i])
    if count != 0:
        frequency_t[Alphabet_t[i]] = count

frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=1)
frequency_d = sorted(frequency_d.items(), key=lambda x: x[1], reverse=1)
frequency_t = sorted(frequency_t.items(), key=lambda x: x[1], reverse=1)
print(frequency[0:display_num])
print(frequency_d[0:20])
print(frequency_t[0:display_num])