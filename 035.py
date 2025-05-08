r1 = float(input('Insira o comprimento da primeira reta: '))
r2 = float(input('Insira o comprimento da segunda reta: '))
r3 = float(input('Insira o comprimento da terceira reta: '))
if r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1:
    print('Sim, é possível formar um triângulo com essas retas')
else:
    print('Não é possível formar um triângulo com essas retas.')