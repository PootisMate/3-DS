import random

palavras = ["barco", "paralelo", "caçamba", "iogurte"]

palavra_oculta = list(random.choice(palavras))
tamanho_palavra = len(palavra_oculta)
chances = 10
display = ["_"] * tamanho_palavra

print("Bem-vindo ao jogo da forca!")
print(display)
print(f"Você possui {chances} tentativas")

while chances > 0:
    letra = input("Digite a letra: ").lower()

    if letra in palavra_oculta:
        for i in range(tamanho_palavra):
            if palavra_oculta[i] == letra:
                display[i] = letra

        print(f"Letra encontrada! Palavra atual: {''.join(display)}")

        if "_" not in display:
            print("Parabéns! Você acertou a palavra!")
            break
    else:
        chances -= 1
        print(f"Letra não encontrada. Você tem {chances} tentativas restantes.")

    print(f"Palavra: {''.join(display)}")

if "_" in display:
    print(f"Você perdeu! A palavra era: {''.join(palavra_oculta)}")