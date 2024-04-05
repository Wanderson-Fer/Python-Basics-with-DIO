if __name__ == '__main__':
    print('Atribução direta')
    pessoa = {
        'nome': 'Wanderson',
        'idade': 21,
        'hobbys': ['Ler', 'Programar', 'Escutar música']
    }

    print(pessoa)

    print('Construtor da classe')
    aluno = dict(
        nome='Wanderson',
        curso='Engenharia da Computação',
        notas=[7.0, 8.5, 6.3]
    )

    print(aluno)

    print(pessoa['nome'])
    print(pessoa['idade'])
    # Ou
    print(pessoa.get('hobbys'))

    print('Alterando valores de dicionário')

    pessoa['nome'] = 'Wanderson Fernandes'
    print(pessoa['nome'])
    pessoa['hobbys'].append('Exercícios')
    print(pessoa['hobbys'])

    print('Método clear')
    print('Antes')
    print(aluno)
    aluno.clear()
    print('Depois')
    print(aluno)

    print('Método keys')
    print(pessoa.keys())
