def menssagem():
    print('Olá mundo!')


def saudacao(nome):
    print(f'Seja bem vindo {nome}!')


def saudacao_generalista(nome: str = 'Sr'):
    print(f'Seja bem vindo {nome}!')

def somar(numeros: list):
    return sum(numeros)

def sucesso_e_antecessor(number: int):
    return number - 1, number + 1

def add_aluno(nome: str, /, notas: list, *, curso: str):
    aluno = {
        'Nome': nome,
        'Notas': ', '.join([str(nota) for nota in notas]),
        'Média': round(sum(notas)/len(notas), 1),
        'Curso': curso
    }

    return aluno


if __name__ == '__main__':
    menssagem()
    saudacao('Wanderson')
    saudacao_generalista('Wanderson')
    saudacao_generalista()

    print(somar([10, 12, 14]))
    print(sucesso_e_antecessor(18))

    print(add_aluno('Wanderson', [8.3, 6.7, 7.9], curso='Eng. da Computação'))
