pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# for k in pessoas.keys():
# for k in pessoas.values():
# del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')