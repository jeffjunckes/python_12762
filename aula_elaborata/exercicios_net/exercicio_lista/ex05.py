"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
m Imprima os três vetores."""
vetor_par = []
vetor_impar = []
vetor_numeros = []




for item in range(1, 11):
    numero = int(input("digite um numero: "))
    vetor_numeros.append(numero)
    if (numero %2 == 0):
        vetor_par.append(numero)
    else:
        vetor_impar.append(numero)


print("você digitouu {} os numeros pares sao {} e os numeros impares sao {}".format(vetor_numeros, vetor_par, vetor_impar))
