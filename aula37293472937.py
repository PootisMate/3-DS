import random
forca = []
palavra = []
continuar = True
while ( continuar == True):
   palavra.append(input("Colocará qual palavra?"))
   print(palavra)
   if (input('Deseja continuar?').upper() == 'Y'):
      continuar = True
   else:
      continuar = False

sorteada = print(palavra[random.randint(0, len(palavra)-1)])
