x = int(input('Digite um Numero para Calculo do Fatorial: '))
fim = 'nok'
fatorial = x
total = 0
while (fim == 'nok'):
	if	x == 0:
		fim = 'ok'		
	else:
		total = total + (fatorial * (x - 1))
		x -= 1
		print(str(total))
	
print('Fatorial: ' + str(total))	


