quantidade_turmas = (int(input("qual a quantidade de turmas que você tem? ")))
contador = 1
soma_alunos = 0
print("programa para medir a media de alunos por turma")
while contador <= quantidade_turmas:
    quantidade_de_alunos = int(input("qual a quantidade da turma {} ? ".format(contador)))
    if quantidade_de_alunos > 40:
        print("quantidade limite é de 40 alunos por favor tente novamente. ")
    else:   
        soma_alunos = (soma_alunos + quantidade_de_alunos)
        contador = (contador + 1)
    
    
    
contador_media = (soma_alunos / quantidade_turmas)
print("a media para essa escola é {} ".format(contador_media))
    





















