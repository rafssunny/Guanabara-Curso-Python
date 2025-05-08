soma = 0
for numeros in  range(1, 7):
    x = int(input('Insira um número: '))
    if x % 2 == 0:
        soma+=x
print(soma)
