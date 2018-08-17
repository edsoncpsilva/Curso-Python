print()
print('-'*80)
#obtem dados do aluno nome e notas
nome_aluno = input('Nome do Aluno: ')
n1 = int(input('Digita Nota1: '))
n2 = int(input('Digita Nota2: '))
n3 = int(input('Digita Nota3: '))
n4 = int(input('Digita Nota4: '))
#calcular media do aluno
media = (n1 + n2 + n3 + n4) / 4
#decide se o aluno foi aprovado/reprovado
if media >= 7:
   resultado = 'Aprovado (Parabéns)'
else: 
   resultado = 'Reprovado (Estude Mais)'	
#exibe resultado
print('-'*80)
print('O Aluno ' + nome_aluno + ' obteve media ' + str(media) + ' ' + resultado)
print('-'*80)
print()

