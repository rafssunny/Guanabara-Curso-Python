n = 0
contagem = 0
soma = 0
while n != 999:
    n = int(input('Insira um número: '))
    contagem += 1
    if n != 999:
        soma+=n
print(f'Foram digitados {contagem-1} números e a soma entre eles é de {soma}')
