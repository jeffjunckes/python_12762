"""FUNÇÕES ANONIMAS OU LAMBDA
        criadas em tempo de execução
#SINTAXE
É DEFINIDA POR LAMBDA AO INVEZ DE DEF. E NAO POSSUEM NOME,
variavel = lambda <lista de parametros separados por (,)<comandos da função>
"""
from ctypes.wintypes import RGB


def multiplicacao(x,y):
    return x * y

#(var) = palavra chave parametro1,parametro2 : operação. 
soma = lambda x, y: x + y #aqui so sera executado na linha apenas
#perceba que definimos o parametro, e depois o que a função vai fazer.
#separados por : 
#usamos o nome da variavel como se fosse uma função
#lambda nao precisa do return.
print(multiplicacao(3,5))
print(soma(3,5))
import random

fncor = lambda: "rgb({}, {}, {})".format(random.randint(0, 255),
                                         random.randint(0, 255),
                                         random.randint(0, 255))
print(fncor())

