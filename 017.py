from math import hypot
cateto_oposto = float(input('Insira o comprimento do Cateto Oposto: '))
cateto_adjacente = float(input('Insira o comprimento do Cateto Adjacente: '))
print(f'A hipotenusa vai medir {hypot(cateto_oposto, cateto_adjacente):.2f}')