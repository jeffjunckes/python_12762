nome_usuario = str(input("qual é o seu nome? "))
senha_usuario = str(input ("qual é a sua senha? "))
while nome_usuario == senha_usuario:
    if nome_usuario == senha_usuario:
        print("seu nome nao pode ser igual a senha , tente novamente")
        nome_usuario = str(input("qual é o seu nome? "))
        senha_usuario = str(input ("qual é a sua senha? "))

if (nome_usuario != senha_usuario):
    print("usuario cadastrado com sucesso muito obrigado, tenha uma boa tarde")












