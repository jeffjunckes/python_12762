lista_relatorio = []

aluno = "a"
while aluno != "":
    lista_alunos = []
    lista_notas = []
    lista_media = []
   
    aluno = input("qual é o nome do aluno? ")
    if aluno == "":
        break
    lista_alunos.append(aluno)
    n1 = float(input("digite a primeira nota "))
    lista_notas.append(n1)
    n2 = float(input("digite a segunda nota "))
    lista_notas.append(n1)
    n3 = float(input("digite a terceira nota "))
    lista_notas.append(n1)
    media = ((n1  + n2 + n3)/3)
    lista_media.append(media)
    lista_relatorio.append(lista_alunos)
    lista_relatorio.append(lista_notas)
    lista_relatorio.append(lista_media)
print(lista_relatorio)







