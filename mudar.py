print('-'*50)
x = int(input('Digite x: '))
y = int(input('Digite y: '))
print('Antes...')
print('x é ' + str(x))
print('y é ' + str(y))
########################################
a = x
x = y
y = a
########################################
print('-'*50)
print('Depois 1...variavel TEMP')
print('x é ' + str(x))
print('y é ' + str(y))
########################################
print('-'*50)
print('Depois 2..."x, y = y, x"')
x, y = y, x
print('x é ' + str(x))
print('y é ' + str(y))
