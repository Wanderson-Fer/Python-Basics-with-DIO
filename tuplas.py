if __name__ == '__main__':
    # Tuplas são imutáveis

    shopping_list = ('milk', 'coffee', 'bread', 'cheese')
    print('Uma tupla: ', shopping_list)
    print('\btipo: ', type(shopping_list))

    print('Não bastam os parênteses: ')
    bread = ('cheese bread')
    print('isso não é uma tupla: ', bread, 'tipo: ', type(bread))

    print('Mas isso é: ')
    coffee = 'Cappuccino',
    print('isso é uma tupla: ', coffee, 'tipo: ', type(coffee))
