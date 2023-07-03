def sacar(saldo, limite, valor: float) -> None:
    if (valor <= limite) and (valor <= saldo):
        print('Sacando...')
    elif valor > saldo:
        print('Saldo insuficiente!')
    else:
        print('Valor acima do limite!')

def permitir_beder(idade: int) -> None:
    if idade >= 18:
        print('Pode beber!')
    else:
        print('Não pode beber!')


age = int(input('Digite sua idade: '))
permitir_beder(age)

saldo_na_conta = 1000.0
limite_diario = 500.0
valor_do_saque = float(input('Digite o valor que deseja sacar: '))

sacar(saldo_na_conta, limite_diario, valor_do_saque)

