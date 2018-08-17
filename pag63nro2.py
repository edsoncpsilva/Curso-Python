n1 = int(input('Digite Numero 1: '))
n2 = int(input('Digite Numero 2: '))
n3 = int(input('Digite Numero 3: '))

ok = 0

if 	n1 > n2 and n1 > n3:
	print('Numero 1 maior, conteudo: ' + str(n1))
	ok += 1

if 	n2 > n1 and n2 > n3:
	print('Numero 2 maior, conteudo: ' + str(n2))
	ok += 1

if 	n3 > n1 and n3 > n2:
	print('Numero 3 maior, conteudo: ' + str(n3))
	ok += 1

if	ok == 0:
	print('Os numeros são Iguais')

print('Fim do Teste')

print()
print('==> Usando o max')
print('O Numero Maior é: ' + str(max(n1, n2, n3)))
print()
print('==> Usando o min')
print('O Numero Menor é: ' + str(min(n1, n2, n3)))

		


