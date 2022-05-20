salario = (float(input(("qual o valor do salario? ")) ))
def reajuste_20(a):
    return ((a*20)/ 100 )
def reajuste_15(a):
    return ((a*15)/ 100 )
def reajuste_10(a):
    return ((a*10)/ 100 )
def reajuste_5(a):
    return ((a*5)/ 100 )
if salario <= 1280:
    print("seu salario é de {}".format(salario))
    print("seu reajuste foi de 20 %")
    print("o reajuste sera de {} reais".format(reajuste_20(salario)))
    print("seu novo salario sera de {} reais".format(salario + reajuste_20(salario)  ))
elif (salario > 1281) and (salario <= 1700):
    print("seu salario é de {}".format(salario))
    print("seu reajuste foi de 15 %")
    print("o reajuste sera de {} reais".format(reajuste_15(salario)))
    print("seu novo salario sera de {} reais".format(salario + reajuste_15(salario)  ))
elif (salario > 1701) and (salario <= 2500):
    print("seu salario é de {}".format(salario))
    print("seu reajuste foi de 10 %")
    print("o reajuste sera de {} reais".format(reajuste_10(salario)))
    print("seu novo salario sera de {} reais".format(salario + reajuste_10(salario)  ))
elif (salario > 2501):
    print("seu salario é de {}".format(salario))
    print("seu reajuste foi de 10 %")
    print("o reajuste sera de {} reais".format(reajuste_5(salario)))
    print("seu novo salario sera de {} reais".format(salario + reajuste_5(salario)  ))


























