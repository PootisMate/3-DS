import random

def defender():
    return random.randint(1, 70)

def curar(vida):
    cura = random.randint(10, 25)
    print(f"Curou {cura} pontos de vida!")
    return vida + cura

def atacar(atacante, defensor, vida_atacante, vida_defensor, defesa_valor=0):
    verificar_acerto = random.randint(1, 20)
    
    if verificar_acerto == 1:
        print("Errooouuu! Falha crítica")
        dano = random.randint(10, 20)
        print(f"{atacante} se feriu no ataque, e recebeu {dano} pontos de dano.")
        vida_atacante -= dano
    elif 2 <= verificar_acerto < 8:
        print("Erro normal, não ocorre nada")
    elif verificar_acerto == 20:
        dano = random.randint(20, 40)
        print(f"Critical hit! {defensor} se feriu gravemente, e recebeu {dano} pontos de dano.")
        vida_defensor -= dano
    else:
        dano = random.randint(10, 20)
        if dano > defesa_valor:
            dano_final = dano - defesa_valor
            print(f"{defensor} recebeu {dano_final} pontos de dano.")
            vida_defensor -= dano_final
        else:
            print(f"{defensor} anulou o dano.")
    
    return vida_atacante, vida_defensor

def mostrar_menu():
    print("####################################")
    print("###      1 - Atacar Inimigo      ###")
    print("###      2 - Defender Ataque     ###")
    print("###      3 - Curar-se            ###")
    print("####################################")

jogador = "Togekiss"
vida_jogador = 120

computador = "Swampert"
vida_computador = 120

while vida_jogador > 0 and vida_computador > 0:
    mostrar_menu()
    escolha = int(input("O que você irá fazer?: "))
    defesa_valor = 0
    
    if escolha == 1:
        vida_jogador, vida_computador = atacar(jogador, computador, vida_jogador, vida_computador)
    elif escolha == 2:
        defesa_valor = defender()
        print(f"{jogador} está defendendo com {defesa_valor} pontos de defesa!")
    elif escolha == 3:
        vida_jogador = curar(vida_jogador)
    else:
        print("Opção inválida! Tente novamente.")
        continue
    
    # Computador ataca depois da jogada do jogador
    if vida_computador > 0:
        vida_computador, vida_jogador = atacar(computador, jogador, vida_computador, vida_jogador, defesa_valor)

if vida_jogador <= 0:
    print("Swampert Ganhou!")
elif vida_computador <= 0:
    print("Togekiss ganhou!")

print("Fim da batalha")
