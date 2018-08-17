def fatorial(n):
	ret = 1
	for i in range(1, n+1):
		ret *= i
	return ret

n = int(input('Digite o numero que voce deseja calcular o fatorial: '))

if	n < 0:
	print('nao sei calcular fatorial de numero negativo.')
	exit()

print(fatorial(n))
