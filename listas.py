if __name__ == '__main__':
    frutas = ['laranja', 'maçã', 'uva', 'abacaxi', 'manga', 'tucumã']
    print('frutas: ', frutas)
    print('tipo: ', type(frutas))

    # Acesso direto
    print('primeira fruta: ', frutas[0])
    print('uma fruta: ', frutas[3])
    print('última fruta: ', frutas[-1])

    # Slices
    print('Fatiando listas')
    print(frutas[2:])
    print(frutas[:2])
    print(frutas[::2])
    print(frutas[::-1])

    print('Usando um loop')
    for fruta in frutas:
        print(fruta)

    print('Compressão de listas')
    numeros = list(range(20))

    print('Lista origiral:', numeros)

    print('Usando um laço tradicional: ')
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    print('Números pares: ', pares)

    impares = [numero for numero in numeros if numero % 2 != 0]
    print('Números impares: ', impares)

    print('Métodos da classe')

    # append - acrescenta um elemento na lista
    print('frutas: ', frutas)
    frutas.append(input('Insira uma fruta na lista: '))
    print('frutas: ', frutas)

    # clear - limpa a lista sem excluí-la
    print('antes: ', numeros)
    numeros.clear()
    print('depois: ', numeros)

    # copy - copia a lista para evitar o vínculo entre listas
    numeros = pares
    print('É o mesmo item? ', id(numeros) == id(pares))

    print('Usando copy')
    numeros = pares.copy()
    print('É o mesmo item? ', id(numeros) == id(pares))

    # count - retorna a quantidade de itens na lista
    print('Quantidade de uvas na cesta: ', frutas.count('uva'))

    # index - retorna a primeira ocorrência de um elemento na lista
    print('Primeira ocorrencia de "uva": ', frutas.index('uva'))

    # pop - remove o última elemento adicionado
    print('Antes: ', frutas)
    frutas.pop()
    print('Depois: ', frutas)

    # remove - remove um elemento pello seu valor
    print('Frutas', frutas)
    fruta = input('Que fruta você quer remover? ')
    frutas.remove(fruta)
    print('Frutas', frutas)

    # reverse - inverte a lista
    frutas.reverse()
    print('Frutas com reverse', frutas)

    # sort - ordena itens da lista
    frutas.sort()
    print('Frutas ordenadas', frutas)
    frutas.sort(reverse=True)
    print('Frutas ordenadas e invertidas', frutas)

    # extend - junta duas listas, de forma contíngua.
    impares.extend(pares)
    print('impares extends pares ', impares)

    """ Output/
    Métodos da classe
    frutas:  ['laranja', 'maçã', 'uva', 'abacaxi', 'manga', 'tucumã']
    Insira uma fruta na lista: uva
    frutas:  ['laranja', 'maçã', 'uva', 'abacaxi', 'manga', 'tucumã', 'uva']
    antes:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    depois:  []
    É o mesmo item?  True
    Usando copy
    É o mesmo item?  False
    Quantidade de uvas na cesta:  2
    Primeira ocorrencia de "uva":  2
    Antes:  ['laranja', 'maçã', 'uva', 'abacaxi', 'manga', 'tucumã', 'uva']
    Depois:  ['laranja', 'maçã', 'uva', 'abacaxi', 'manga', 'tucumã']
    Frutas ['laranja', 'maçã', 'uva', 'abacaxi', 'manga', 'tucumã']
    Que fruta você quer remover? uva
    Frutas ['laranja', 'maçã', 'abacaxi', 'manga', 'tucumã']
    Frutas com reverse ['tucumã', 'manga', 'abacaxi', 'maçã', 'laranja']
    Frutas ordenadas ['abacaxi', 'laranja', 'manga', 'maçã', 'tucumã']
    Frutas ordenadas e invertidas ['tucumã', 'maçã', 'manga', 'laranja', 'abacaxi']
    impares extends pares  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    """

