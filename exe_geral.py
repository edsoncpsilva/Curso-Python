def meu_abs(n):
	ret = n
	if	n < 0:
		ret = n * -1
	return ret

def meu_len(l):
	tam = len(l)
	cont = 0
	for i in range(tam):
		cont = cont + 1
	return cont

def meu_max(n):
	lista = list(n)
	ret_max = ''
	for i in lista:
		if	i >= ret_max:
			ret_max = i
	return ret_max

def meu_min(n):
	lista = list(n)
	pri_vez = 's'
	for i in lista:
		if	pri_vez == 's':
			ret_min = i
			pri_vez = 'n'

		if	i <= ret_min:
			ret_min = i

	return ret_min

def meu_sum(n):
	lista = list(n)
	ret_sum = 0
	for i in lista:
		ret_sum += int(i)
	return ret_sum

def	meu_media(m):
	tam = len(m)
	acumular = meu_sum(m)
	ret_med = acumular / tam
	return ret_med

nro_abs = int(input('Digite um Numero: ' ))
print('usando o abs, fica: ' + str(meu_abs(nro_abs)))

campo_len = input('Digite um Texto: ' )
print('usando o len, fica: ' + str(meu_len(campo_len)))

campo_max = input('Digite uma lista: ' )
print('usando o max, fica: ' + str(meu_max(campo_max)))
print('usando o min, fica: ' + str(meu_min(campo_max)))

campo_sum = input('Digite uma lista numerica: ' )
print('usando o sum, fica: ' + str(meu_sum(campo_sum)))
print('usando a Media, fica: ' + str(meu_media(campo_sum)))

