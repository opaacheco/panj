class Bicicleta:
    def __init__(self, cor, modelo, ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("BIIIIIIIIIII")
    
    def parar(self):
        print("parando a bicicleta...\nBicicleta parada")
    
    def correr(self):
        print("vrummm")
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f"{chave.title()}={valor}" for chave, valor in self.__dict__.items()])}"    
    
b1 = Bicicleta("preto","bmx", 2022, 200)
b1.buzinar()
print(b1)