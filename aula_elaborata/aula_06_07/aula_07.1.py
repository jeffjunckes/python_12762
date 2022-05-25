iNumElementos = 40
iContador = 1
lst_numeros = []
#lst_numeros = list(range(1,11))


while (iContador <= iNumElementos):
    lst_numeros.append(iContador)
    iContador = iContador + 1


print(lst_numeros)

lstPares = []
for iNumero in lst_numeros:
    if iNumero % 2 == 0:
        lstPares.append(iNumero)
print(lstPares)
print(lst_numeros)
print("\n")
lstImpares = [iNumero for iNumero in lst_numeros if iNumero % 2 != 0]
print(lstImpares)





























