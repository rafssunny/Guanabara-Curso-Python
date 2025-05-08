soma_pares = soma_terceira = 0
matrizes = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for m in range(0,3):
    for n in range(0,3):
        matrizes[m][n] = int(input('Insira um número: '))
        if matrizes[m][n] % 2 == 0:
            soma_pares+=matrizes[m][n]
print('-='*20)
for c in range(0,3):
    for l in range(0,3):
        print(f'[{matrizes[c][l]}] ', end = '')
    print()
print('-='*40)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {matrizes[0][2]+matrizes[1][2]+matrizes[2][2]}')
print(f'O maior valor da segunda linha é {max(matrizes[1])}')