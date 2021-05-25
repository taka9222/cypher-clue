import copy

Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Plugboard = Alphabet.copy()

Scrambler1 = ['u', 'w', 'y', 'g', 'a', 'd', 'f', 'p', 'v', 'z', 'b', 'e',
              'c', 'k', 'm', 't', 'h', 'x', 's', 'l', 'r', 'i', 'n', 'q', 'o', 'j']

Scrambler2 = ['a', 'j', 'p', 'c', 'z', 'w', 'r', 'l', 'f', 'b', 'd', 'k',
              'o', 't', 'y', 'u', 'q', 'g', 'e', 'n', 'h', 'x', 'm', 'i', 'v', 's']

Scrambler3 = ['t', 'a', 'g', 'b', 'p', 'c', 's', 'd', 'q', 'e', 'u', 'f',
              'v', 'n', 'z', 'h', 'y', 'i', 'x', 'j', 'w', 'l', 'r', 'k', 'o', 'm']

Reflector = ['y', 'r', 'u', 'h', 'q', 's', 'l', 'd', 'p', 'x', 'n', 'g',
             'o', 'k', 'm', 'i', 'e', 'b', 'f', 'z', 'c', 'w', 'v', 'j', 'a', 't']

word = "gyhrvflrxy"
plug_swap = ['ab', 'sz', 'uy', 'gh', 'lq', 'en']

sc1_init = Alphabet.index('a')
sc2_init = Alphabet.index('e')
sc3_init = Alphabet.index('b')

Scrambler1, Scrambler2 = Scrambler2, Scrambler1
encrypted = ""

def rel(num):
    return num % len(Alphabet)


for wire in plug_swap:
    nums = list(wire)
    idx1 = Plugboard.index(nums[0])
    idx2 = Plugboard.index(nums[1])
    Plugboard[idx1], Plugboard[idx2] = Plugboard[idx2], Plugboard[idx1]

turn = 0
for ch in word:
    sc1_init += 1
    if turn % len(Alphabet) == len(Alphabet) - 1:
        sc2_init += 1
        if turn % len(Alphabet) % len(Alphabet) == len(Alphabet) - 1:
            sc3_init += 1
    idx = rel(Plugboard.index(ch) + sc1_init)
    idx = rel(Scrambler1.index(Alphabet[idx]) - sc1_init + sc2_init)
    idx = rel(Scrambler2.index(Alphabet[idx]) - sc2_init + sc3_init)
    idx = rel(Scrambler3.index(Alphabet[idx]) - sc3_init)
    idx = Reflector.index(Alphabet[idx])
    idx = rel(Alphabet.index(Scrambler3[rel(idx + sc3_init)]) - sc3_init)
    idx = rel(Alphabet.index(Scrambler2[rel(idx + sc2_init)]) - sc2_init)
    idx = rel(Alphabet.index(Scrambler1[rel(idx + sc1_init)]) - sc1_init)
    encrypted += Plugboard[idx]
    turn += 1

print(encrypted)
