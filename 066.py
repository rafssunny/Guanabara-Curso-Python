n = q = s = 0
while True:
    n = int(input('Insira um número: '))
    if n == 999:
        break
    q += 1
    s+=n
print(f'A soma entre esses valores foi de {s} e a quantidade de valores inseridos foi de {q}')