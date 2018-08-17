import getpass

tentativa = 0

palavra_secreta = getpass.getpass('Digita Palavra Secreta: ')
print('Dica: a palavra tem ' + str(len(palavra_secreta)) + ' letras')


while True:
	palpite = input('Digite seu Palpite: ')

	if	palpite == ' ':
		continue

	if	palpite in palavra_secreta:
		print('Ok, acertou')
		break
	else:
		print('não acertou')

	tentativa += 1
	if	tentativa == len(palavra_secreta):
		print('Fim da Tentativas')
		break
			
