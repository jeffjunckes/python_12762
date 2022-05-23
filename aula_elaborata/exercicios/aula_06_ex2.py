def valor_pagamento(a,b):
    
    if b <= 0:
        print("você vai pagar: {} reais".format(a))
    else:
      return (((b * 0.01) * (a * b) / 100) + (a * 3) / 100 ) 





valor_pgto = float(input("qual o valor de pagamento? "))
multa = ((valor_pgto * 3) / 100)
dia_atrasado = float(input("quantos dias está atrasado? "))

valor_total = (valor_pagamento(valor_pgto,dia_atrasado) + multa)
preço_final = (valor_total + valor_pgto)
print(preço_final)



