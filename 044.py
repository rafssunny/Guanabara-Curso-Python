valor = float(input('Qual o valor do produto em reais? '))
pagamento = str(input('Insira a forma de pagamento\nà vista dinheiro/cheque(1)\nà vista no cartão(2)\n2x no cartão(3)\n3x ou mais(4)\n'))
if pagamento == '1':
    print(f'O produto tem um desconto de 10% ficando por R${valor-(valor*0.10):.2f}')
elif pagamento == '2':
    print(f'O produto tem um desconto de 5% ficando por R${valor-(valor*0.5):.2f}')
elif pagamento == '3':
    print(f'O produto tem o seu preço normal de R${valor:.2f}.')
else:
    parcelas = int(input('Quantas parcelas?'))
    print(f'O produto tem 20% de juros ficando por R${valor+(valor*0.20):.2f} com parcelas de R${(valor+(valor*0.20))/parcelas:.2f}')