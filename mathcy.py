# encrypter for math cryptgraphy

Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

nums = ["50", "20", "37", "95", "74", "00", "25", "51", "05", "78", "34", "32", "72"]
x, y, z = 4, 19, 3
encrypted = ""

for i in range(len(nums)):
    num = int(nums[i]) **x 
    # num = int(nums[i] + nums[i+1])#str(x))
    num %= y
    num += z
    encrypted += Alphabet[num]
    print(encrypted)