lista = ["cat", "baby", "bird"]
string = "bceabjtytttttttttttttttttttt"
letra = []
palavraFinal0 = []
palavraFinal1 = []
palavraFinal2 = []
for item in range(len(string)):
    letra += string[item]
        
for item in letra:
    if item in lista[0]:
        palavraFinal0.append(item)
        if "".join(palavraFinal0) == lista[0]:
            print("".join(palavraFinal0))


for item in letra:
    if item in lista[1]:
        palavraFinal1.append(item)
        if "".join(palavraFinal1) == lista[1]:
            print("".join(palavraFinal1))

for item in letra:
    if item in lista[2]:
        palavraFinal2.append(item)
        if "".join(palavraFinal2) == lista[2]:
            print("".join(palavraFinal2))



