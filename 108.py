from Módulos import moeda
p = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)}, temos {moeda.moeda(moeda.aumentar(p, 10))}')