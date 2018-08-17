dinheiro = int(input('Digite um Valor R$: '))

if 	dinheiro < 1000:
	if 	dinheiro < 0:
		print('Estou Negativo, preciso fazer Horas Extras')
		exit()
	print('Estou pobre!!!')
	print('preciso trabalhar mais')
	exit()

if  dinheiro > 1000:
	print('Pode sair pro buteco hoje, leve uma amigo e pague a conta')

if  dinheiro == 1000:
	print('Pode sair pro buteco hoje, leve a carteira')

print('fim normal')
