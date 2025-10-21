
#Classe base para as questões
class Questao:
    def __init__(self, numero: int, enunciado: str):
        self.numero = numero
        self.enunciado = enunciado

    def resolver(self):

        raise NotImplementedError("Cada questão deve implementar o método resolver().")
