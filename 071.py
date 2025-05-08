print('Caixa eletrônico')
dinheiro = celula50 = celula25 = celula10 = celula1 = 0
while True:
    dinheiro = int(input('Qual o valor a ser sacado?R$'))
    if dinheiro / 50 > 1:
        celula50+=dinheiro//50
        dinheiro -= ((dinheiro//50)*50)
    if dinheiro/ 20 >= 1:
        celula25+=dinheiro//20
        dinheiro -= ((dinheiro//20)*20)
    if dinheiro / 10 >= 1:
        celula10+=dinheiro//10
        dinheiro -= ((dinheiro//10)*10)
    if dinheiro / 1 >= 1:
        celula1+=dinheiro//1
        dinheiro -= ((dinheiro//1)*1)
    break
if celula50 > 0:
    print(f'{celula50} células de R$50')
if celula25 > 0:
    print(f'{celula25} células de R$20')
if celula10 > 0:
    print(f'{celula10} células de R$10')
if celula1 > 0:
    print(f'{celula1} células de R$1')