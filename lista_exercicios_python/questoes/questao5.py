from .base import Questao
from .utils import leia_int

class Questao5(Questao):
    def __init__(self):
        super().__init__(5, "Leia um número inteiro e mostre o seu antecessor e seu sucessor.")

    def resolver(self):
        print("\n" * 2)
        print(f"--- Executando Questão {self.numero}: {self.enunciado} ---\n")
        numero = leia_int("Digite um número inteiro: ")
        sucessor = numero + 1
        antecessor = numero - 1
        print(f"O antecessor de {numero} é {antecessor}\nO sucessor de {numero} é {sucessor}")
        print("\n--- Fim da Questão 5 ---")
        input("Pressione Enter para voltar ao menu...")
