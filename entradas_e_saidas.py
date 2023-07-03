from datetime import date as dt


nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')
ano_nascimento = dt.today().year - int(idade)

print(f'Olá, {nome}', f'Você nasceu em: {ano_nascimento}')
