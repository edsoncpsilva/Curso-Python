#==> jogo de dados de 6 lados
#importar biblioteca
import random

#variaveis
sair = 's'
qtd = 0

#loop de interacao
while (sair == 's'):

	#interacao
	print()
	numero = int(input('Digite o numero que irá sair entre 1 e 6?:' ))
	nro_sorte = random.randrange(1, 7)

	if	numero == nro_sorte:
		print('Acertei, estou com sorte!!!!') 
		print()
		exit()

	if 	numero > nro_sorte:
		print('você digitou um numero Maior, tente novamente') 
		print()

	if 	numero < nro_sorte:
		print('você digitou um numero Menor, tente novamente') 
		print()

	print('-'*70)
	print('==> Numero Sorteado:' + str(nro_sorte))
	print('-'*70)

	#validar opcao de SAIR
	ok = 'nok'
	while (ok == 'nok'):
		sair = input('Deseja Continuar Tentando (s/n): ')
		if	sair == 's':
			ok = 'ok'
		if	sair == 'S':
			sair = 's'
			ok = 'ok'
		if	sair == 'n':
			ok = 'ok'
		if	sair == 'N':
			sair = 'n'
			ok = 'ok'
		if	ok == 'nok':
			print('Opcao Invalida, digite apenas "S" ou "N"')

	#controlar quantidade de tentativas
	if	sair == 's':
		qtd = qtd + 1
		if	qtd == 4:
			print()
			print('********************************************')
			print('***** excedeu a qtd de tentativas de 2 *****')
			print('********************************************')
			sair = 'n'	

print()
print('Fim de Jogo !!!!')

