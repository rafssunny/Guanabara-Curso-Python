nome = nbarato = continuar = ''
preco = gasto = barato = quantidade = 0
while True:
    nome = str(input('Qual é o nome do produto?'))
    preco = float(input('Qual é o preço do produto?R$'))
    if gasto == 0:
        barato += preco
        nbarato = nome
    gasto += preco
    if preco > 1000:
        quantidade+=1
    if preco < barato:
        barato-=barato
        barato+=preco
        nbarato = nome
    continuar = str(input('Deseja continuar?')).lower().strip()
    while continuar != 'sim' and continuar != 'nao':
        continuar = str(input('Deseja continuar?')).lower().strip()
    if continuar == 'sim':
        print('')
    else:
        break
print(f'O total gasto na compra foi de R${gasto:.2f}\n{quantidade} produtos custam mais de R$1000,00\n{nbarato} é o produto mais barato e custa R${barato:.2f}')


