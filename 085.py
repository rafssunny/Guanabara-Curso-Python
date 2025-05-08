valores = [[], []]
for c in range(0,7):
    n = int(input('Insira um valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print(f'Pares em ordem crescente {sorted(valores[0])}')
print(F'Impares em ordem crescente {sorted(valores[1])}')