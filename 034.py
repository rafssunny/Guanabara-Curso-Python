salario = float(input('Insira o seu salário: R$'))
if salario > 1250:
    print(f'O seu salário com o aumento de 10% fica de R${(salario*0.10)+salario:.2f}')
if salario <= 1250:
    print(f'O seu salário com o aumento de 15% fica de R${(salario*0.15)+salario:.2f}')