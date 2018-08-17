print()
print('-'*80)
#obtem dados do funcionario
nome_func = input('Nome do Funcionario..: ')
salario   = int(input('Digita Salario Bruto.: '))
pc_desconto  = int(input('Digita % de Desconto.: '))
#calcular salario liquido
salario_liquido = (salario - ((salario * pc_desconto)/100))
vl_desconto = ((salario * pc_desconto)/100)
#exibe resultado
print('-'*80)
print('Demonstrativo de Pagamento')
print('Funcionario.......: ' + nome_func)
print('(+)Salario Bruto..: ' + str(salario))
print('(-)' + str(pc_desconto) + '% Desconto...: ' + str(vl_desconto))
print('(=)Salario Liquido: ' + str(salario_liquido))
print('-'*80)
print()

