#nome = str(input('Me diga seu nome completo: '))
#nome = nome.split(' ')
#nome = ' '.join(nome)
#print(f'Seu primeiro nome é {nome[0:nome.find(' ')]}\ne seu último nome é{nome[nome.rfind(' '):]}')
#o codigo acima dava erro se colocasse espaço

n = str(input('me diga seu nome completo')).strip()
nome = n.split()
print(f'seu primeiro nome é {nome[0]} e seu ultimo nome é {nome[len(nome)-1]}')