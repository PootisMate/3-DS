import random

palavras = ["barco", "paralelo", "caçamba", "iogurte"]

palavra_oculta = list(random.choice(palavras))
tamanho_palavra = len(palavra_oculta)
chances = 10
posicoes = []
display = []
for _ in range(tamanho_palavra):
    display += "_"

print(display)
print(f"Você possui {chances} tentativas")
continuar = True

while continuar:
    letra = input("Digite a letra: ")
    if letra in palavra_oculta:
        for i in range(len(palavra_oculta)):
            if palavra_oculta[i] == letra:
                print("Letra encontrada na posição: " + str(i))
                posicoes.append(i)

        for i in range(len(posicoes)):
            palavra_oculta[posicoes[i]] = letra

        print(display)
        posicoes.clear()

if display == list(palavra_oculta):
    print("Você acertou!")
    continuar = False;
