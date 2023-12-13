class Animal:
    def __init__(self, numero_patas):
        self.numeo_patas
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} : {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, numero_patas):
        super().__init__(numero_patas)

class Gato(Mamifero):
    pass

class Onitorrinco(Mamifero, Animal):
    def __init__(self, numero_patas, cor_pelo, cor_bico):
        # print(Onitorrinco.mro())
        print(Onitorrinco.__mro__)
        super().__init__(numero_patas=numero_patas, cor_pelo=cor_pelo, cor_bico=cor_bico)