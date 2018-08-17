x = 1
print(x)

# r - read
# w - wrte

fd = open('novoarquivo.txt', 'w')

for _ in range(10):
	print('teste teste', file=fd)

fd.close()


