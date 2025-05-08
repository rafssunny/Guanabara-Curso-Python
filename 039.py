from datetime import date
idade = int(input('Qual ano você nasceu? '))
ano = date.today().year
if ano-idade < 18:
    print('\033[33mVocê ainda vai se alistar no serviço militar, pode ficar tranquilo\033[m')
    print(f'Faltam \033[32m{18-(ano-idade)} anos\033[m para seu alistamento!')
elif ano-idade > 18:
    print('\033[31mJá passou da hora de você se alistar do serviço militar\033[m')
    print(f'Você está \033[31m{(ano-idade)-18} anos\033[m atrasado!')
else:
    print('\033[32mEstá na hora de se alistar no serviço militar!\033[m')