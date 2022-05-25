from cmath import pi
import os
#cwd : current working directory
#o diretorio onde você esta  executado meu script python.
print("objeto os : {} ".format(os))
#print("tipo do objeto os: {}".format(type(os))
sDiretorio = os.getcwd()
print(sDiretorio)

lstConteudoDiretorio = os.listdir(".")
print("conteudo do diretorio atual : {}".format(lstConteudoDiretorio))
#pra cada diretorio que ele encontrar na arvore de diretorios do diretorio raiz incluindo o proprio diretorio
#vai me retornar 3 tuplas, uma com o caminho do diretorio
#uma com o nome dos diretorios
#e uma com o nome dos arquivos e ele exclui o ponto e o ponto ponto
for root, dirs, files in os.walk(sDiretorio):
    print("=" * 50)
    print("root: " + str(root))
    print("dirs: " + str(dirs))
    print("files: " + str(files))
    print("." * 50)


















