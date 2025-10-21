from .base import Questao
from .utils import leia_int

class Questao3(Questao):
    def __init__(self):
        super().__init__(3, "Leia dois números inteiros e mostre a somatória entre eles.")

    def resolver(self):
        print("\n" * 2)
        print(f"--- Executando Questão {self.numero}: {self.enunciado} ---\n")
        num1 = leia_int("Digite o primeiro número inteiro para somar: ")
        num2 = leia_int("Digite o segundo número inteiro para somar: ")
        soma = num1 + num2
        print(f"A soma de {num1} e {num2} = {soma}")
        print("\n--- Fim da Questão 3 ---")
        input("Pressione Enter para voltar ao menu...")
