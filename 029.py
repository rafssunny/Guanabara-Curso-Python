km = float(input('insira a quantos quilometros o carro estava: '))
if km > 80:
    print(f'como seu carro estava a {km}Km/h, você vai pagar uma multa de R${(km-80)*7:.2f}')
else:
    print('Seu carro não ultrapassou 80 km/h, logo não sofreu a multa!')