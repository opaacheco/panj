class Passaro():
    def voar(self):
        print("voando...")
        
class Pardal(Passaro):
    def voar(self):
        super().voar()
                
class Avestruz(Passaro):
    def voar(self):
        print("avestruz nao voa!!!")
        
def plano_de_voo(obj):
    obj.voar()
    
    
p1 = Pardal()
p2 = Avestruz()
plano_de_voo(p1)
plano_de_voo(p2)
