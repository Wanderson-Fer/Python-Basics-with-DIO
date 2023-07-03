preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = preco / 2
print(preco)

preco = preco // 2
print(preco)
print(int(preco))

preco = str(preco)
print(preco)

message = 'O preço é ' + preco

language = 'Python'
print(float(language))
r'''
    Traceback (most recent call last):
        File "C:\Users\wanderson.wf\Documents\Test\PYTHON\DIO_Python\conversões.py", line 20, in <module>
            print(float(language))
                  ^^^^^^^^^^^^^^^
    ValueError: could not convert string to float: "Python"
'''
