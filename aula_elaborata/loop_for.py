#vetor é variavel todos com o valor fixo
#cada laçõ a variavel item recebe um elemento da coleção
"""colecao_de_itens = [1,2,3,4,5]
for (item) in (colecao_de_itens):
    print(item) """
#como criar uma lista \/
#continue volta para o inicio do slaço

from unittest.util import strclass
num_str = "1"

lista_numeros = [] #uma lista vazia
lista_strings = []
lista_opcoes = ["1 - exibir listas ", "2 - entrada de dados ", "3 - fim" ]
#acima vemos uma lista com tres  elementos(lista_opcoes)
opcao = ""
entrada_dados = "1"
while (opcao != "3" ):
    #exibir lista de opções\/
    #print(lista_opcoes)
    for (item) in (lista_opcoes):
        print(item)
    #entrada de dados\/
    opcao = input("selecione uma opção: ")
    print("a opção selecionada foi: {}".format(opcao))    

    if (opcao == "1"):
            print("lista de numeros")
            print(lista_numeros)
            print("lista de string")
            print(lista_strings)
        
    elif(opcao == "2"):
        while (num_str != ""):
            print("processar entrada de dados")
            num_str = input("digite um numero ou uma string: ")
            if (num_str.isnumeric()):
                lista_numeros.append(num_str)
            elif (num_str.isalpha()):
                lista_strings.append(num_str)
            elif(num_str.isdigit()):
                lista_numeros.append(num_str)
            elif(num_str == ""):
                break
            
            
            
        
        
    elif(opcao == "3"):
        print("fim")

    else:
        print("erro opção invalida")
        










