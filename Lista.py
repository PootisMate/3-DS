import random
atividade = int(input("Escolha qual atividade você quer olhar."))

#1#
if atividade == 1:
 nome = input("Qual é o seu nome?")
 idade = input("Qual é a sua idade?")
 print("Olá,", nome, "você tem", idade, "anos.")

#2#
if atividade == 2:
 N1 = int(input("Escolha um numero:"))
 N2 = int(input("Escolha mais um numero:"))
 soma = N1 + N2
 subtracao = N1 - N2
 multiplicacao = N1 * N2
 divisao = N1 / N2

 print(soma)
 print(subtracao)
 print(multiplicacao)
 print(divisao)

#3#
if atividade == 3:
 numero =  int(input('Qual número você quer saber?'))
 if (numero > 0):
  print('Esse número é positivo.')
 elif(numero == 0):
  print('Esse número é igual a zero.')
 elif(numero < 0):
  print('Esse número é negativo.')

#4#
if atividade == 4:
 nota = int(input("Qual é a nota desse aluno?"))
 if (nota >= 6):
    print('Aprovado')
 elif (nota < 4):
    print('Reprovado')
 else:
    print('Recuperação')

#5#
if atividade == 5:
 velhice = int(input("Quanto anos essa pessoa tem?"))
 if (velhice <= 12):
    print('Essa pessoa é uma criança')
 elif (velhice >= 18):
    print('Essa pessoa é um adulto')
 else:
    print('Essa pessoa é um adolescênte')

#6#
if atividade == 6:
 for i in range(1, 21):
  print(i)

#7#
if atividade == 7:
 senha_acesso = "1234"

 while True:
  senha = input("Digite a senha: ")
  if senha == senha_acesso:
   print("Acesso liberado.")
   break
  else:
   print("Acesso negado, tente novamente.")

#8#
if atividade == 8:
 nomes = []

 for i in range(5):
   nome = input(f"Digite o {i+1}° nome: ")
   nomes.append(nome)

 print("Nomes digitados: ", nomes)

#9#
if atividade == 9:
 palavras = ["abacate", "mongoloide", "porteiro", "caçamba"]