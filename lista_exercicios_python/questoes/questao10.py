from .base import Questao
import math
from .utils import leia_float_brl, formatar_brl

class Questao10(Questao):
    def __init__(self):
        super().__init__(10,"Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de delta")

    def resolver(self):
        print("\n" * 2)
        print(f"--- Executando Questão {self.numero}: {self.enunciado} ---\n")

        A = leia_float_brl("Digite um valor para A: ")
        B = leia_float_brl("Digite um valor para B: ")
        C = leia_float_brl("Digite um valor para C: ")

        #calcula o valor de delta
        delta = B ** 2 - 4 * A * C
        print(f"\nO valor de delta é: {delta}")

        # Só tenta calcular as raízes se o delta for maior ou igual a zero
        if delta < 0:
            print("A equação não possui raízes reais (delta é negativo).")
        else:
            x1 = (-B + math.sqrt(delta)) / (2 * A)
            x2 = (-B - math.sqrt(delta)) / (2 * A)
            print(f"As raízes da equação são:\nX1 = {formatar_brl(x1)}\nX2 = {formatar_brl(x2)}\n")

        print("\n--- Fim da Questão 10 ---")
        input("Pressione Enter para voltar ao menu...")