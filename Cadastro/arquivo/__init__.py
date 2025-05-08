def ArquivoExiste(nome):
    """
    Checar se arquivo existe.
    :param nome: Nome do arquivo
    :return: Valor de True ou False para existência do arquivo.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def CriarArquivo(nome):
    """

    :param nome:Cria um arquivo com determinado nome.
    :return: Arquivo txt.
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print('Arquivo criado com sucesso!')

