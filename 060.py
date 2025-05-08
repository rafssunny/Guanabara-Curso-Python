numero = int(input('Escolha o número: '))
c = numero-1
fatorial = numero*c
while c != 0:
    c = c - 1
    fatorial = fatorial*c
    if c == 1:
        print(f'!{numero} = {fatorial}')