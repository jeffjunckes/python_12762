#se condição - entao
#-> comandos1
#senao
#-> comando2
#fimse
#if , elif , else
#if condição :
#elif
#lembrar de identação sempre
"""if(condição):
        comando1
        comando2
        if(condição2):
            comando6()
            comando7()
        else:
            comando8()
    else:
        comando3
        comando4
    comando5"""

#percebe que o comando 5 esta na identação do if e else 
#o que significa que ele nao esta na estrutura.
"""
if(condição):
    comando1
    comando2
elif(condição2):
    comando3()
    comando4()
elif (condição3):
    comando5()
elif(condição4):
    comando6
    comando7
comando5"""

#as estruturas podem ser de 3 tipos, sequenciais, condicionais e repetição




#vetor é variavel todos com o valor fixo
#cada laçõ a variavel item recebe um elemento da coleção
"""colecao_de_itens = [1,2,3,4,5]
for (item) in (colecao_de_itens):
    print(item) """
#como criar uma lista \/

lista_numeros = [] #uma lista vazia
lista_strings = []
lista_opcoes = ["1 - exibir listas ", "2 - entrada de dados ", "3 - fim" ]
#acima vemos uma lista com tres  elementos(lista_opcoes)
opcao = ""
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
        print("processar entrada de dados")
        num_str = input("digite um numero ou uma string: ")
        if (num_str.isnumeric()):
            lista_numeros.append(num_str)
        elif (num_str.isalpha()):
            lista_strings.append(num_str)



        
        
    elif(opcao == "3"):
        print("fim")

    else:
        print("erro opção invalida")
        

#enquanto(condição1) faça
    #bloco de comandos
#fimenquanto
"""em python"""
#while(condição):
    #bloco de comandos1()
    #para nao entrar em loop infinito vocÇe pode colocar
    #if(condição for falsa):
        #break
"""
contador = 0
while contador < 10:
    print("condição verdadeira")
    contador = contador +1
    print("contador: {} ".format(contador))"""


        






