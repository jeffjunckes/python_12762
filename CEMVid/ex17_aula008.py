from math import hypot, sqrt
cateto1 = float(input("qual é o valor do primeiro cateto? "))
cateto2 = float(input("qual é o valor do segundo cateto? "))
hipotenusa = (sqrt((cateto1 ** 2 + cateto2 ** 2)))
print("o cateto 1 vale {} e o cateto 2 vale {} a soma do quadrado dos catetos é igual a hipotenusa que é {:.2f}".format(cateto1, cateto2, hipotenusa))
print("a hypotenusa vale {:.2f}".format(hypot(cateto1, cateto2)))


















