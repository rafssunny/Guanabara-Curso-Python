tupla = (int(input('Insira o primeiro número: ')),
int(input('Insira o segundo número: ')),
int(input('Insira o terceiro número: ')),
int(input('Insira o quarto número: ')))
cont = 0
for c in tupla:
    cont+=1
    if c == 3:
        print(f'O número 3 apareceu na {tupla.index(3)+1} posição')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
print('Os valores pares digitados foram', end = ' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end= ' ')