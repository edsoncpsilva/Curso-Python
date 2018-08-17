# fizzbuzz

# resultado.txt
print('abrindo arquivo')
fd = open('resultado.txt', 'w')

#definindo layout para gravação
layout = 'Registro {0}, {1}'

#imprima os numeros de 1 a 100
i = 000

for i in range(1, 101):
	if	(i % 2 == 0) and (i % 3 == 0):
#		print('linha', i, 'fizzbuzz', file=fd)
		print(layout.format(i, 'fizzbuzz'), file=fd)

	elif (i % 2 == 0):
#		print('linha', i, 'fizz', file=fd)
		print(layout.format(i, 'fizz'), file=fd)
	elif (i % 3 == 0):
#		print('linha', i, 'buzz', file=fd)
		print(layout.format(i, 'buzz'), file=fd)
	else:
#		print('linha', i, file=fd)
		print(layout.format(i, ''), file=fd)

print('Fechando Arquivo')
fd.close()
	

