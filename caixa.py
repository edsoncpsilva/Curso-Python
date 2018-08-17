#!/usr/bin/env python3

# linha de comentarios
print('teste1-simples')
print('-------')
print('|     |')
print('|     |')
print('|     |')
print('-------')
print(' ')
print('teste2-multiplicando')
print('-'*7)
print('|' + ' '*5 + '|')
print('|' + ' '*5 + '|')
print('|' + ' '*5 + '|')
print('-'*7)
print(' ')
print('teste3-Variavel')
coluna = int(input('Digite qtd e colunas:'))
print(type(coluna))
print('-'*coluna)
print('|' + ' '*(coluna-2) + '|')
print('|' + ' '*(coluna-2) + '|')
print('|' + ' '*(coluna-2) + '|')
print('-'*coluna)
print(' ')
print('teste4-while')
a=1
while a>5:
	if 	a==1:
		print('-'*7)
	elif 	a==5:
		print('-'*7)
	else:
		print('|' + ' '*5 + '|')
	a = a-1
print(' ')
	

