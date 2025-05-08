dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos kms rodados? '))
preco_dia = dias*60
preco_km = km*0.15
print(f'O total a pagar é de R${preco_dia+preco_km:.2f}')