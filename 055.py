print('Ver maior e menor peso')
maior = 0
menor = 0
for p in range(0,5):
    peso = float(input('Insira o peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}Kg e o menor foi {menor}Kg')