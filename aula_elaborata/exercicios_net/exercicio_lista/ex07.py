"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""

vetor_soma = []
vetor_mult = []
vetor_numeros = []

num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
num3 = int(input("digite o terceiro numero: "))
num4 = int(input("digite o quarto numero: "))
num5 = int(input("digite o quinto numero: "))
vetor_numeros.append(num1)
vetor_numeros.append(num2)
vetor_numeros.append(num3)
vetor_numeros.append(num4)
vetor_numeros.append(num5)
soma = (num1 + num2 + num3+ num4 + num5)
vetor_soma.append(soma)
mult = (num1 * num2 * num3 * num4 * num5)
vetor_mult.append(mult)
print("os numeros que você digitou sao {} ".format(vetor_numeros))
print("a soma dos numeros é {} ".format(vetor_soma))
print("a divisao dos numeros é {}".format(vetor_mult))

















