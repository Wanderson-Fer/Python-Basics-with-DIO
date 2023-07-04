curso = 'CuRSo de PyThOn'

print('original: ', curso)
print('upper: ', curso.upper())
print('lower: ', curso.lower())
print('title: ', curso.title())
print('--------------------------')

nome = '    Wanderson    '

print('original: ', nome)
print('strip: ', nome.strip())
print('rstrip: ', nome.rstrip())
print('lstrip: ', nome.lstrip())
print('--------------------------')

curso = curso.title()

print('original: ', curso)
print('center with "*": ', curso.center(20, '*'))
print('join with "." : ', ".".join(curso))
