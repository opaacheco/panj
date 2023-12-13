class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome 
        self.idade = idade
        
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
        
p = Pessoa().criar_de_data_nascimento(2003, 3 ,17, "pedroca")

print(p.nome, p.idade)
print(p.e_maior_idade(18))
print(p.e_maior_idade(8))
