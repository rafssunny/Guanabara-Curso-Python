peso = float(input('Insira seu peso:' ))
altura = float(input('Insira sua altura: '))
imc = peso/(altura*altura)
print(f'Seu imc é de \033[33m{imc:.1f}\033[m')
if imc < 18.5:
    print(f'\033[31mVocê está abaixo do peso\033[m')
elif imc >= 18.5 and imc <= 25:
    print('\033[32mPeso ideal\033[m')
elif imc > 25 and imc <= 30:
    print('\033[33mVocê está sobrepeso\033[m')
elif imc > 30 and imc <= 40:
    print('\033[31mVocê está com obesidade\033[m')
else:
    print('\033[31mVocê está com obesidade mórbida!\033[m')