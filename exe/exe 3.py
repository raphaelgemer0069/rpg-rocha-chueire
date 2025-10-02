loja_frutas = {
    'uva':{'preço': 3.50,
        'quantidade':10},
    'tomate':{'preço': 3.50,
        'quantidade':10},
    'banana':{'preço': 3.50, 
        'quantidade':10}
}
loja_frutas.update({'uva':{'preço': 23.00,'quantidade':70},
                'tomate':{'preço': 20.00,'quantidade':70.00},
                'banana':{ 'preço': 20.00,'quantidade':10}})
print(loja_frutas)

for k,v in loja_frutas.items():
    loja_frutas.get(k)['preço']*=1.15

for k,v in loja_frutas.items():
  loja_frutas.get(k)['quantidade']+=20
  print(loja_frutas)

loja_frutas.pop('uva')