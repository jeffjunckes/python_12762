"""funções:
quando falamos de funções temos basicamente 3 tipos de funções
1- funções integradas(built-in).
    sao funções que fazem parte da linguagem.
        ex:print , type , input, sum-


2- funções definidas pelo usuário(programador).
    sintaxe:
    #função sem parametros
    def nome da funçao(): 
        codigo da função(o que ela vai fazer quando chamada)


    #função com dois parametros obrigatorios    
    def nome da funçao(a,b):
        codigo da função
    #função com dois parametros 1 obrigatorio e 1 opcional
    def nome da funçao (a, b = 0): #repare que B ja entra com um valor padrao.
        #codigo da função
        



UMA FUNÇÃO PODE OU NAO RETORNAR UM VALOR AO FINAL DE SUA EXECUÇÃO.
PARA RETORNAR UM VALOR UTILIZAMOS O COMANDO "RETURN VALOR" NORMALMENTE NO FINAL DA FUNÇÃO
    FUNÇÕES INTEGRADAS E FUNÇÕES DEFINIDAS PELO USUARIO
        sao criadas em tempo de compilação
    FUNÇÕES ANONIMAS OU LAMBDA
        criadas em tempo de execução
#SINTAXE
É DEFINIDA POR LAMBDA AO INVEZ DE DEF. E NAO POSSUEM NOME,




escopo de variaveis:

"""
#função com dois parametros obrigatorios e que retorna um valor.
def somaDoisNumeros(n1,n2):
    nsoma = n1 + n2
    return nsoma
#função que nao retorna resultado
def somaDoisNumerosMasNaoRetornaResultado(n1,n2):
    soma = n1 + n2
    
    #função com dois parametros obrigatorios e um padrao opcional ja definido
def somatresNumeros(n1,n2, n3 = 0):
    nsoma = n1 + n2 + n3
    return nsoma

def multiplicaDoisNumeros(n1 = 0 ,n2 = 0 ):
    nproduto = n1 * n2
    return nproduto
def imprimeDoisNumeros():
    n1 = 7
    n2 = 7
    print("uma string({}, {})".format(n1,n2))
def somaVariosNumeros(*arg):
    return sum(arg)
def analiseVariosArgumento(*args):
    print("varios argumentos: {}".format(args))
    print("tipo da variavel args: {}".format(type(args)))
    for valor in args:
        print("{}".format(valor))
        print("{}".format(args[3]))

#PROGRAMA PRINCIPAL.
g_n1 = 5
g_n2 = 3
g_n3 = 2

g_nresultado = somaDoisNumeros(g_n1,g_n2)
print("resultado da função somaDoisNumeros: {}".format(g_nresultado))
g_nresultado = somaDoisNumerosMasNaoRetornaResultado(g_n1,g_n2)
print("resultado da função somaDoisNumerosMasNaoRetornaResultado: {}".format(g_nresultado))
#note que a segunda forma de fazer, nao vai dar certo por que nao pede pra retornar um resultado(o resultado é none)
g_nresultado = somatresNumeros(g_n1,g_n2)
print("o resultado da função somaTresNumeros: {}".format(g_nresultado))
g_nresultado = multiplicaDoisNumeros()
print("resultado da função multiplcadoisnumeros: {}".format(g_nresultado))
n1 = 5
n2 = 4
imprimeDoisNumeros()
print("uma string({}, {})".format(n1,n2))
#   PARA UMA QUANTIDADE DE ARGUMENTOS VARIAVEIS UTILIZAMOS (*args)
#na hora de chamar é sem o asterisco
g_nresultado = somaVariosNumeros(n1,n2,g_n3,g_n1)
print("resultado da função somavariosnumeros: {}".format(g_nresultado))
analiseVariosArgumento(5,3,7,"teste",False)








"""
inicio do programa
    g_n1
    g_n3
    g_n3
    g_nresultado
    execução a função somadoisnumeros(g_n1,g_n2)
    n1 = g_n1
    n2 = g_n2
    nsoma = n1+n2
    return nsoma
    FIM DA EXECUÇÃO
        DESTROI N1
        DESTROI N2
        DESTROI NSOMA
g_nresultado = resultado retornado pela somadoisnumeros



"""









