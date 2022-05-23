"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes."""
lista_vetor= []
lista_contador= [0,1,2,3,4,5,6,7,8,9]
cont_consu = 0
for item in lista_contador:
    caractere = input(("digite um caractere "))
    if (caractere == "a") or (caractere == "e") or (caractere == "i") or (caractere == "o") or (caractere == "u"):
        print("você digitou uma vogal")
    else:
        print("você digitou uma consuante")
        cont_consu = cont_consu +1
        lista_vetor.append(caractere)
print("foram digitado {} e ao todo são {} consuantes".format(lista_vetor, cont_consu))

























