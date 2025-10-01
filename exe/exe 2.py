loja_carro ={
      'ferrari f40':{
          'cor':'roxo',
          'valor': 276.000,
      },
'uno':{
          'cor':'vermelho',
          'valor': 206.000,
          }
  }
for k,v in loja_carro.items():
    loja_carro.get(k)['valor']*=1.15
    print(loja_carro)