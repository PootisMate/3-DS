import random


def atacar(atacante, adversario, vida_atacante, vida_adversario):
    verificar_acerto = random.randint(1, 20)
    if verificar_acerto == 1:
        print("ERRRRROOOOOOO Criticamene")
        dano = random.randint(10, 20)

        print(atacante + "se feriu no ataque, e recebeu " + str(dano) + " pontos de dano.")
        vida_atacante = vida_atacante - dano

        return vida_atacante, vida_adversario

    elif verificar_acerto == 20:
        print("Criticalmente crítico!")
        dano = random.randint(20, 40)

        print(adversario + " se feriu gravemente, e recebeu " + str(dano) + " pontos de dano.")
        vida_adversario = vida_adversario - dano

        return vida_atacante, vida_adversario

    elif 2 <= verificar_acerto < 8:
        print("Miss")

        return vida_atacante, vida_adversario
    else:
        print("O seu dano foi...")
        dano = random.randint(10, 20)

        print(adversario + " recebeu " + str(dano) + " pontos de dano.")
        vida_adversario = vida_adversario - dano

        return vida_atacante, vida_adversario

def defender(atacante, adversario, vida_atacante, vida_adversario):
    verificar_defesa = random.randint(1, 20)
    if verificar_defesa == 1:
        print("Defesa Falhada.")
        dano = dano * 2

        print("Você se deixou ainda mais vunerável e tomou", str(dano), "de dano.")
        vida_atacante = vida_atacante - dano


jogador = "Pootis"
vida_jogador = 120

computador = "Final legend ultra mega blaster secret boss"
vida_computador = 120


while (vida_jogador > 0) and (vida_computador > 0):
    vida_jogador, vida_computador = atacar(jogador, computador, vida_jogador, vida_computador)

    vida_computador, vida_jogador = atacar(computador, jogador, vida_computador, vida_jogador)

if (vida_computador <= 0):
   print("Fim da batalha,", jogador, "venceu.")
elif (vida_jogador <= 0):
    print("Fim da batalha,", computador, "venceu.")
