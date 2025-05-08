from Módulos import moeda
v = float(input('Insira um valor: '))
print(f'O dobro desse valor é {moeda.dobro(v)}')
print(f'A metade desse valor é {moeda.metade(v)}')
print(f'Aumentando 10% desse valor, temos {moeda.aumentar(v, 10 )}')
print(f'Diminuindo 13% desse valor, temos {moeda.diminuir(v, 13)}')