r1 = float(input('Insira o comprimento da primeira reta: '))
r2 = float(input('Insira o comprimento da segunda reta: '))
r3 = float(input('Insira o comprimento da terceira reta: '))
if r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1:
    print('Sim, é possível formar um triângulo com essas retas')
    if r1 == r2 and r2 == r3 and r3 == r1:
        print('Isso é um triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isso é um triângulo Isósceles')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('Isso é um triângulo escaleno')
else:
    print('Não é possível formar um triângulo com essas retas.')