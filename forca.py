import random
palavras = ["casa", "prato", "ceu"]

sorteada = random.randint(0,2)

print("A Palavra sorteada foi " + palavras[sorteada])
print(len(palavras[sorteada]))

letra = input("Digite a letra que você deseja buscar")

i = 0
while i < len(palavras[sorteada]):
    if palavras[sorteada][i] == letra:
        print("Palavra encontrada na posição " + str(i))
    i += 1
