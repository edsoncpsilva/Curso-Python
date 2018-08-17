#funcao
def quadruplo(n):
	ret = n*4
	return ret

def dobro(n):
	return n*2

def dobro2(n):
	ret = dobro(dobro(n))
	return ret

#chamando as funções
print('o quadrupo de 6 eh: ' + str(quadruplo(6)))
print('o dobro de 6 eh: ' + str(dobro(6)))
print('o dobro do dobre de 2 eh: ' + str(dobro2(2)))

############################################################
def tabuada(n1, n2):
	return(n1*n2)

nro = int(input('Digite a Tabuada que seja Estudar: ' ))

cont = 1
while (cont < 11):
	print(str(nro) + ' * ' + str(cont) + ' = ' + str(tabuada(nro, cont)))
	cont += 1

cont = 1
for i in range(10):
	print(str(nro) + ' * ' + str(cont) + ' = ' + str(tabuada(nro, cont)))
	cont += 1





