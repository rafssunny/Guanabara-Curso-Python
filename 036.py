print('Empréstimo bancário')
Casa = float(input('Insira o valor da casa: '))
Salario = float(input('Insira o seu salário: '))
Anos = int(input('Em quantos anos você vai pagar: '))
Prestacao = Casa/(12*Anos)

if Prestacao > Salario*0.30:
    print(f'\033[31mSeu empréstimo foi negado.\033[m')
elif Prestacao <= Salario*0.30:
    print(f'\033[32mSeu empréstimo foi aprovado!\033[m\n\033[1mA prestação mensal será em torno de R${Prestacao:.2f}')