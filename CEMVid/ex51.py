import time
primeiro_termo = int(input("de onde você quer começar? "))
razao = int(input("de quanto em quanto você quer pular? "))
contador = 0

for item in range(primeiro_termo, 9999999999999,razao):
    print(item)
    contador += 1
    time.sleep(1)
    if contador == 10:
        break












