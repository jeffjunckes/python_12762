#manipulando cadeias de textos.
#uma cadeia de caracteres é uma string
#[9:13]ele para de contar no 13 mas o ultimo valor nao entra na contafem, ou seja vai
#pegar a letra da frase ate a 12 e excluir o 13, sempre exclui a ultima
#len(frase) mostra o comprimento da frase, len vem de lens 
#frase.count("o") utiliza para contar quantas vezes a letra O aparece na frase
# /\pode ser qualquer coisa dentro do parenteses 
#se voce colocar por exemplfrase.count("o", 0, 13) ele fatia a string do 0 ate o 12 e conta
#/\ quantas veszes a letra O aparece nesse range.
#frase.find("deo") ele mostra em que momento começou o parametro que você colocou
#dentro do parenteses.se a string nao existir , ela retorna o valor -1.
#voce pode usar a palavra in, por exemplo "curso" in frase<- nesse caso ele procura
#na string se existe a palavra curso e retorna True.
#METODOS
#frase = "curso em video python"
#frase.replace("python", "android") <- nesse caso ele vai procurar python na frase
#e vai subistituir por "android"a frase vai ficar "curso em video android"
#frase.upper() <- deixa todas letras em maiusculas
#frase.lower() <- deixa todas letras minusculas.
#frase.capitalize()<- joga todos caracteres para minusculo e deixa so a primeira letra maiusculo
#frase.title()<- analisa quantas palavras tem a string e deixa o maiusculo em cada primeira palavra da frase
# frase.strip()<- remove todos os espaços inuteis no começo e no fim da string
# frase.rstrip()<- remove os espaços inuteis a direita(o R é de right(direita))
# frase.lstrip() <- remove os espaços inuteis da esquerda
#divisao e junção
#frase.split()<- divide a string conforme parametro dentro dos parenteses.(o padrao é espaço)
#"-".join(frase) <- retorna a frase splitada na lista para uma string normal com o separador de "-" ou qualquer outro que você quiser


frase = "curso em video python"
print(frase[:5:2])#< pula do inicio ao final pode colocar numeros entre os : para definir parametros
print(frase.upper().count("O"))#joga frase pra maiuscula e depois conta <maiuscula e miniscula sao coisas diferentes em python
print(len(frase))#leu quantos caracteres incluindo espaços a frase tem
print(len(frase.strip())) #<- contou a frase com o len, removendo espaços antes e depois da frase.
print(frase.replace("python", "android" ))#<- vai mandar trocar python por android na frase
#lembre-se que o replace nao modifica a atribuição final , apenas manda printar com outra coisa na tela
#por exemplo
print(frase) #<- nose que a frase continua sendo a atribuida na variavel, a replace nao mudou.
print("curso" in frase) #mostra se eciste curso na palavra frase(True ou False)
print(frase.find("curso"))#mostra onde começa a palavra curso na prase(em qual posição)
print(frase.lower().find("curso")) #<- primeiro vai botar tudo em minusculo depois vai procurar, pois o pythnon diferencia maiuscula e minuscula
print(frase.split())#vai separar a fase em palavras numa lista sempre que achar um espaço(note que o padrao é espaço mas poderia ser qualquer coisa.)
dividido = frase.split() #atribui a frase.split a variavel dividido
print(dividido[0])#mandei printar a palavra na posição da lista que mandei esplitar 
print(dividido[2][3])#manda pegar a palavra na posição depois manda pegar a terceira letra dessa palavra(lembre-se em python começa do 0 entao nesse caso [2] significa a terceira palavra)





















