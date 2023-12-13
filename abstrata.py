from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        print("ligar")
        
    @property
    @abstractproperty
    def marca(self):
        return "LG"

class ControleTv(ControleRemoto):
    def ligar(self):
        pass
    
    def desligar(self):
        print("desligar")

contro = ControleTv() 