#maquina finita de estado
lugar = 'Casa do Jogador'
while True:
	if	lugar == 'Casa do Jogador':
		print('Voce nasceu e esta em sua casa.')
		lugar = input('Para onde deseja ir? ')
	elif lugar == 'Iate':
		print('Você Venceu!')
		break
	elif lugar == 'Inferno':
		lugar = input('Voce esta no Inferno, deseja ir pra onde? ')
	elif lugar == 'ceu':
		print('Você venceu, esta no Ceu')
		break	
	else:
		print('Voce esta perdido na vida, *** desconhecido ***')

print('Game Over')
