def escreva(msg):
    """
    -> Impressão de linhas que se adaptam a quantidade de caracteres da mensagem
    :param msg: mensagem a ser impressa
    :return: sem retorno
    Função criada por Sara Rodolfo para fixação do Exercício 097, Curso em Vídeo.
    """
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Gustavo Guanabara')
escreva('Funções em Python')
escreva('Curso em Vídeo')
escreva('Estudando Python as 7h18m do dia 26/05/2022')
