class Estudante:
    escola = "DIO"
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
aluno_1 = Estudante("Pedroca", 1)
aluno_2 = Estudante("lele", 1)
aluno_3 = Estudante("duk", 1)

def mostrar_estudantes(*objs):
    for obj in objs:
        print(obj)

print(aluno_1)
# se eu fizer 
Estudante.escola + "Nova Arte"
# altera pra todas as classes por ser uma variavel de classe e não de instância

mostrar_estudantes(aluno_1, aluno_2, aluno_3)