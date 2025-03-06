import random
Tipo_Dado = int(input('Qual tipo de dado você que usar?'))
Quantidade = int(input('Quantos dados você quer jogar? '))
while Quantidade > 0:
    print(random.randint(1, Tipo_Dado))
    Quantidade -= 1
