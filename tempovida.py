#obter nome
nome_usr =  input('Nome do Usuario.......:')
#obter idade
idade_usr = int(input('Idade do Usuario......:'))
#obter expectativa
exp_vida =  int(input('Expectativa Brasileira:'))
#calcular expectativa
resultado = exp_vida - idade_usr
result2 = str(resultado)
#demonstrar resultado
print (nome_usr + ', sua Expectativa de Vida é de mais ' + result2 + ' anos, então corre pro Bar e Aproveita')
print (nome_usr + ', sua Expectativa de Vida é de mais ' + str(resultado) + 'anos, então corre pro Bar e Aproveita')
