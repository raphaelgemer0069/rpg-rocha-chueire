loja_frutas = {
    'maca':3.00,
    'banana':3.60,
    'uva':7.60,
}

#função get: método usado para acessar o valor em dicionário ->
preco_uva = loja_frutas.get('uva',{})
print ('uva',preco_uva)

#função update:método usado para atualizar os vaolers do dicionario
loja_frutas.update({'uva': 8.90, 'tomate': 10})
print(loja_frutas,'#tomate adicionado')
#função pop: método para remover uma chave
#específica de um dicionário e retornar
#o valor associado ela.
loja_frutas.pop('tomate')
print(loja_frutas,'#tomate removido')

#função itemns: método de leitura de um dicionario,
# que separa key e value do mesmo,