from re import I


listaAlunos =  []
listaAluno = []


iNumerosDeNotas = 3
bExecutar = True
while(bExecutar):
    snome = input("digite o nome do aluno! ")
    if(snome == ""):
        break
    listanotas = []
    iContadorDeNotas = 1
    while (iContadorDeNotas <= iNumerosDeNotas):
        snota = input("digite a {}ª nota: ").format(iContadorDeNotas)
        if(snota.isnumeric()):
            listanotas.append(float(snota))
            iContadorDeNotas = iContadorDeNotas +1
        else:
            print("erro, valor invalido! ")
    listaAluno = [snome, listanotas]
    listaAlunos.append(listaAluno)
    
















