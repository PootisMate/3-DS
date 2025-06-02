class veiculo:
    def __init__(self, marca, modelo, ano, portas, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.portas = portas
        self.cilindrada = cilindrada

class automovel(veiculo):
  def acelerar(self):
      print(f"{self.marca} está acelerando acelaradamente acelerado!")

class motocicleta(veiculo):
    def rappar(self):
        print(f"{self.marca} está derrapando derrapadamente!")
