from time import sleep


def Menu():
    """
    Tela de menu do Programa de Cadastro
    :return: Menu do Programa.
    """
    print(f'{'MENU PRINCIPAL'.center(50)}')
    print('-' * 50)
    print(
        '\033[0;33m1\033[m - \033[0;34mVer pessoas cadastradas\033[m\n\033[33m2\033[m - \033[0;34mCadastrar nova pessoa\033[m\n\033[0;33m3\033[m - \033[0;34mSair do sistema\033[m')
    print('-' * 50)


def Cadastro(Lista_original, arquivo):
    """
    Realizar cadastro de novo usuário no Sistema.
    :return: Cadastro é adicionado a lista. E retorna seu nome com a mensagem de aprovação.
    """
    print(f'{'NOVO CADASTRO'.center(50)}')
    print('-' * 50)
    Lista_copy = dict()
    while True:
        try:
            Lista_copy['Nome'] = str(input('Nome: '))
            Lista_copy['Idade'] = int(input('Idade: '))
        except:
            print('ERRO: Digite um número inteiro válido.')
        else:
            Lista_original.append(Lista_copy.copy())
            print(f'Novo registro de {Lista_copy['Nome']} adicionado.')
        try:
            a = open(arquivo, 'at')
        except:
            print('Houve um erro na abertura do arquivo.')
        else:
            try:
                a.write(f'{Lista_copy['Nome']};{Lista_copy['Idade']}\n')
            except:
                print('Houve um erro na hora de escrever os dados.')
            a.close()
        Lista_copy.clear()
        sleep(1.5)
        break
    print('-' * 50)
    return Lista_original


def Sistema(Lista, arq):
    """
    Lista de Pessoas Cadastradas no sistema.
    :param Lista: Lista de cadastro
    :return: Lista de cadastro de forma com Nome e Idade.
    """
    try:
        with open(arq, 'rt') as a:
            linhas = a.readlines()
    except:
        print('Erro ao ler arquivo.')
    else:
        print(f'{"PESSOAS CADASTRADAS".center(50)}')
        print('-' * 50)
        print(f'{"Nome":<30}{"Idade":>10}')
        print('-' * 50)
        for linha in linhas:
            dados = linha.strip().split(';')
            if len(dados) == 2:
                nome, idade = dados
                print(f'{nome:<30}{idade:>10} anos')
        print('-' * 50)
        sleep(1.5)
