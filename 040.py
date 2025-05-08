nota = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))
media = (nota+nota2)/2
print(f'Sua média foi de {media}')
if media < 5:
    print('Sua média foi abaixo de 5, você foi \033[31mREPROVADO\033[m')
elif media >= 5 and media < 6.9:
    print('Você está na \033[33mRECUPERAÇÃO\033[m')
else:
    print('PARABÉNS! você foi \033[32mAPROVADO!\033[m')

