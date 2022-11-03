"""Desafio 105
Faça um programa que tenha a função notas()
que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações
- quantidade de notas
- a maior nota
- a menor nota
- a média da turma
- a situação (opcional)
Adicione também as docstrings da função
"""
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)