print()
print('Jodo da Velha')
print()
print('Vamos Jogar')

posicao1 = ' '
posicao2 = ' '
posicao3 = ' '
posicao4 = ' '
posicao5 = ' '
posicao6 = ' '
posicao7 = ' '
posicao8 = ' '
posicao9 = ' '

while True:
# (horizontal)
	if	posicao1 != ' ' and posicao2 != ' ' and posicao3 != ' ':
		if	posicao1 == posicao2 and posicao1 == posicao3:
			print('Fim de Jogo, o Jogador ' + posicao1 + ' Venceu!')
			break
	if	posicao4 != ' ' and posicao5 != ' ' and posicao6 != ' ':
		if	posicao4 == posicao5 and posicao4 == posicao6:
			print('Fim de Jogo, o Jogador ' + posicao4 + ' Venceu!')
			break
	if	posicao7 != ' ' and posicao8 != ' ' and posicao9 != ' ':
		if	posicao7 == posicao8 and posicao7 == posicao9:
			print('Fim de Jogo, o Jogador ' + posicao7 + ' Venceu!')
			break
# vertical
	if	posicao1 != ' ' and posicao4 != ' ' and posicao7 != ' ':
		if	posicao1 == posicao4 and posicao1 == posicao7:
			print('Fim de Jogo, o Jogador ' + posicao1 + ' Venceu!')
			break
	if	posicao2 != ' ' and posicao5 != ' ' and posicao8 != ' ':
		if	posicao2 == posicao5 and posicao2 == posicao8:
			print('Fim de Jogo, o Jogador ' + posicao2 + ' Venceu!')
			break
	if	posicao3 != ' ' and posicao6 != ' ' and posicao9 != ' ':
		if	posicao3 == posicao6 and posicao3 == posicao9:
			print('Fim de Jogo, o Jogador ' + posicao3 + ' Venceu!')
			break

# cruzado
	if	posicao1 != ' ' and posicao5 != ' ' and posicao9 != ' ':
		if	posicao1 == posicao5 and posicao1 == posicao9:
			print('Fim de Jogo, o Jogador ' + posicao1 + ' Venceu!')
			break
	if	posicao3 != ' ' and posicao5 != ' ' and posicao7 != ' ':
		if	posicao3 == posicao5 and posicao3 == posicao7:
			print('Fim de Jogo, o Jogador ' + posicao3 + ' Venceu!')
			break

	qtd = 0
	qtd_max = 13
 	while (qtd < qtd_max):
 		print()
 		qtd += 1	

	print('Posições..')
	print('1 | 2 | 3 ')	
	print('4 | 5 | 6 ')	
	print('7 | 8 | 9 ')	
	jogadorX = int(input('Jogador X, Digite sua Posição: '))

	if 	jogadorX == 1:
		posicao1 = 'X'	
	elif jogadorX == 2:
		posicao2 = 'X'	
	elif jogadorX == 3:
		posicao3 = 'X'	
	elif jogadorX == 4:
		posicao4 = 'X'	
	elif jogadorX == 5:
		posicao5 = 'X'	
	elif jogadorX == 6:
		posicao6 = 'X'	
	elif jogadorX == 7:
		posicao7 = 'X'	
	elif jogadorX == 8:
		posicao8 = 'X'	
	elif jogadorX == 9:
		posicao9 = 'X'

	print()
	print(posicao1 + ' | ' + posicao2 + ' | ' + posicao3)							
	print(posicao4 + ' | ' + posicao5 + ' | ' + posicao6)							
	print(posicao7 + ' | ' + posicao8 + ' | ' + posicao9)							

	print('Posições..')
	print('1 | 2 | 3 ')	
	print('4 | 5 | 6 ')	
	print('7 | 8 | 9 ')	
	jogadorO = int(input('Jogador O, Digite sua Posição: ')) 

	if 	jogadorO == 1:
		posicao1 = 'O'	
	elif jogadorO == 2:
		posicao2 = 'O'	
	elif jogadorO == 3:
		posicao3 = 'O'	
	elif jogadorO == 4:
		posicao4 = 'O'	
	elif jogadorO == 5:
		posicao5 = 'O'	
	elif jogadorO == 6:
		posicao6 = 'O'	
	elif jogadorO == 7:
		posicao7 = 'O'	
	elif jogadorO == 8:
		posicao8 = 'O'	
	elif jogadorO == 9:
		posicao9 = 'O'

	print()
	print(posicao1 + ' | ' + posicao2 + ' | ' + posicao3)							
	print(posicao4 + ' | ' + posicao5 + ' | ' + posicao6)							
	print(posicao7 + ' | ' + posicao8 + ' | ' + posicao9)							

#	qtd = 0
#	qtd_max = 13
#	while (qtd < qtd_max):
#		print()
#		qtd += 1	

	

