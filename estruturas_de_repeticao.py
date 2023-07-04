# For loop

print('Contando até 10:')
for number in range(10):
    print(number + 1)

number = 1

while number > 0:
    print('\nDigite um numero menor que 0 para sair ou')
    number = int(input('Digite até que número será contado: '))
    for n in range(number):
        print(n + 1, end=', ')
