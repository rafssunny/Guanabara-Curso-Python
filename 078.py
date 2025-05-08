lista = []
maior = menor = pos_maior = pos_menor = 0
for valor in range(0,5):
    lista.append(int(input(f'Insira um valor na posição {valor} :')))
    if valor == 0:
        maior = lista[valor]
        menor = lista[valor]
    if maior < lista[valor]:
        maior = lista[valor]
        pos_maior = valor
    if menor > lista[valor]:
        menor = lista[valor]
print(f'Você digitou os valores {lista}\nO maior valor digitado foi {maior} nas posições ', end = '')
for pos, val in enumerate(lista):
    if val == maior:
        print(f'{pos}', end = '... ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end = '')
for pos, valo in enumerate(lista):
    if valo == menor:
        print(f'{pos}', end = '... ')