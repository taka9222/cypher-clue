import numpy as np

k = [2, 1, 3, 1, 2, 5, 7, 2]
b = np.array([[0, 1, 1, 0, 0, 0, 1, 0],
              [0, 1, 1, 1, 0, 1, 0, 1],
              [0, 1, 1, 1, 1, 0, 0, 1],
              [0, 1, 1, 0, 0, 0, 1, 1],
              [0, 1, 1, 1, 0, 1, 0, 1],
              [0, 1, 1, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 1, 0, 0, 1]])

for p in range(7):
    binary = ''
    for i in range(8):
        binary += str(b[(k[i] - 1 + p) % 7, i])
    char = chr(int(binary, 2))
    print(char)
