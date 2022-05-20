
lista_nome = []
lista_nota = []
lista_media = []
nome_aluno = "s"
relatorio_direcao = ("relatorio: ")

while (nome_aluno != "") :
    nome_aluno = str(input("qual é o nome do aluno? "))
    if nome_aluno == "":
        break
    lista_nome.append(nome_aluno)
    nota1 = float(input("digite a primeira nota: "))
    lista_nota.append(nota1)
    nota2 = float(input("digite a segunda nota: "))
    lista_nota.append(nota2)
    nota3 = float(input("digite a terceira nota: "))
    lista_nota.append(nota3)
    media = ((nota1 + nota2 + nota3) / 3 )
    lista_media.append(media)
    relatorio_aluno = ("o nome do aluno é {} , suas tres notas sao {} , {}, {} e sua media é {} \n".format(nome_aluno, nota1, nota2, nota3, media))
    relatorio_direcao = relatorio_aluno + relatorio_direcao
        

print("os nome dos aluno sao:{} ".format(lista_nome))
print("as notas do aluno são:{}".format(lista_nota))
print("a media do aluno sao: {}".format(lista_media))
print(relatorio_direcao)

  














