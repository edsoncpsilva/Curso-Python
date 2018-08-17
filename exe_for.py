lista_nome = ['edson', 'celso', 'pereira', 'da', 'silva']
letra = input('Qual letra varrer os nomes: ')
qtd_ok = 'n'

#exemplo FOR
for nome in lista_nome:
	if	letra in nome:		
		print('Nome com a Letra "a":' + nome)
		qtd_ok = 's'
		
if	qtd_ok == 'n':
	print('Não achou letra')

print('Fim da Pesquisa')		
	
