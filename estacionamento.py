class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class automovel(veiculo):
  def __init__(self, marca, modelo, ano, portas):
      super().__init__(marca, modelo, ano)
      self.portas = portas

class motocicleta(veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada

carro = automovel("BYD", "Seal", 2016, 4)
moto = motocicleta("Honda", "CG 160 Titan", 2019, 162.7)
