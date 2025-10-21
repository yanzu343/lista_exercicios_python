from .base import Questao
from .utils import leia_float_brl,formatar_brl

class Questao11(Questao):
    def __init__(self):
        super().__init__(1, "Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO  PROMOCIONAL, com 5% de desconto. ")

    def resolver(self):
        print("\n" * 2)
        print(f"--- Executando Questão {self.numero}: {self.enunciado} ---\n")
        #Lógica da questão 11:

        preco = leia_float_brl("Digite o preço do produto: ")
        desconto = 0.05 #5%
        valor_desconto = preco * desconto
        preco_promocional = preco - valor_desconto

        print(f"\n{preco}\n")
        print(f"Desconto (5%): R$ {formatar_brl(valor_desconto)}\n")
        print(f"Preço promocional: R$ {formatar_brl(preco_promocional)}\n")

        print("\n--- Fim da Questão 11 ---")
        input("Pressione Enter para voltar ao menu...")
