temporaria = list()
principal = list()
maior = menor = 0
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resp = str(input('Quer continuar? sim ou não '))
    if resp in 'nao':
        break
print(f'Ao todo foram cadrastadas {len(principal)} pessoas')
print(f'O maior peso foi {maior}. As pessoas com maior peso são', end = ' ')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end = ', ')
print(f'\nO menor peso foi {menor}. AS pessoas com menor peso são ', end = ' ')
for n in principal:
    if n[1] == menor:
        print(f'{n[0]}', end = ', ')