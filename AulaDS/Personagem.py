class Personagem:
    def __init__(self, nome, hp, forca, velocidade, mana, carisma):
        self.nome = nome
        self.hp = hp
        self.forca = forca
        self.velocidade = velocidade
        self.mana = mana
        self.carisma = carisma

    def socar(self, adversario):
        if self.hp <= 0:
            print(f"{self.nome} Não pode atacar, você está sem pontos de vida")
            return
        dano = self.forca
        oponente.vida