"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
 informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida."""


vetor_idade  = []
vetor_altura = []

for item in range(0,2):
    idade = int(input("qual é a sua idade? "))
    vetor_idade.append(idade)
    altura = float(input("qual é sua altura? "))
    vetor_altura.append(altura)
print(vetor_altura[::-1])
print(vetor_idade[::-1])




















