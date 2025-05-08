matrizes = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for m in range(0,3):
    for n in range(0,3):
        matrizes[m][n] = int(input('Insira um número: '))
print('-='*20)
for c in range(0,3):
    for l in range(0,3):
        print(f'[{matrizes[c][l]}] ', end = '')
    print()
