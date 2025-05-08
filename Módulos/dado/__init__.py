def leiadinheiro(p):
    n = str(input(p)).replace(',','.').strip()
    while True:
        if n.isalpha() == False and n.isspace() == False:
            break
        print('-'*30)
        print(f'\033[2;31;40mERRO: "{n.strip()}" é um preço inválido!\033[m ')
        n = input('Digite o preço:').strip()
    return float(n)

def leiaint():
    while True:
        try:
            number = int(input('Digite um número inteiro: '))
        except KeyboardInterrupt:
            print(f'\033[2;31;40mO usuário preferiu não digitar esse número\033[m')
            number = 0
            break
        except:
            print('\033[2;31;40mERRO: digite um número inteiro válido!\033[m')
        else:
            break
    return number
def leiafloat():
    while True:
        try:
            number = float(input('Digite um número real: '))
        except KeyboardInterrupt:
            print(f'\033[2;31;40mO usuário prefiriu não digitar esse número\033[m')
            number = 0
            break
        except:
            print('\033[2;31;40mERRO: digite um número real válido!\033[m')
        else:
            break
    return number