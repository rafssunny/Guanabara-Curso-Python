distancia = float(input('Qual a distância da viagem?(em km) '))
if distancia <= 200:
    print(f'O preço da passagem fica de R${distancia*0.50:.2f}')
else:
    print(f'O preço da passagem fica de R${distancia*0.45:.2f}')