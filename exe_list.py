lista_nome = ['edson', 'celso', 'pereira', 'da', 'silva']

#lista tabela
#ind = 0
#while ind < len(lista_nome):
#	print('Indice: ' + str(ind) + ' Nome: ' + lista_nome[ind])
#	ind += 1

#exemplo FOR
for nome in lista_nome:
	print(nome + ' esta aqui')

while True:
	print()
	nome = input('Digite parte do seu Nome para Pesquisa: ')

	if	nome in lista_nome:
		print()
		print('OK, Você sabe seu Nome.')
		print('Tamanho do seu Nome: ' + str(len(nome)))
		print('Tabela/Lista: ' + str(lista_nome ))
		break
	else:
		print()
		print('*** Não sabe seu nome, Tente Novamente')

print('Fim da Pesquisa')		
	
