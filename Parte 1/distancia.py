x1 = int(input("Digite a primeira coordenada do plano x: "))
y1 = int(input("Digite a primeira coordenada do plano y: "))
x2 = int(input("Digite a segunda coordenada do plano x: "))
y2 = int(input("Digite a terceira coordenada do plano y: "))

if x2 - x1 >= 10 or y2 - y1 >= 10:
    print("longe")
else:
    print("perto")
