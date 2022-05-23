"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
 imprima o número de alunos com média maior ou igual a 7.0."""
vetor_medias = []
vetor_aprovados = []
contador = 0


for items in range(1,11):
    n1 = float(input("digite a primeira nota: "))
    n2 = float(input("digite a segunda nota: "))
    n3 = float(input("digite a terceira nota: "))
    n4 = float(input("digite a quarta nota: "))
    media = float(((n1 + n2 + n3 + n4) / 4))
    vetor_medias.append(media)
    if media > 7:
        vetor_aprovados.append(media)
        contador = contador + 1
print("o numero de aluns com media maior ou igual a 07 é {}\n".format(contador))
print("com as medias {}".format(vetor_aprovados))












