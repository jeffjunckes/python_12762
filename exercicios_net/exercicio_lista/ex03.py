"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela."""
from sre_compile import isstring


print("programas para ver media de alunos , aperte enter para pausar notas")
soma = 0
contador = 0
lista_contador = [1,2,3,4]
lista_nota = []
lista_media = []
lista_total = []

for item in lista_contador:
    notas = float(input("digite a {} nota: ".format(item)))
    soma = (soma + notas)
    contador = (contador + 1)
    lista_nota.append(notas)
media = (soma / contador)
lista_media.append(media)    
lista_total.append(lista_nota)
lista_total.append(lista_media)
print(lista_nota)
print(lista_media)
print(lista_total)
print( "as notas sao {} e a media é {}".format(lista_nota, lista_media))

   



    













