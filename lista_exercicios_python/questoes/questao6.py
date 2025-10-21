from .base import Questao
from .utils import leia_float_brl, formatar_brl

class Questao6(Questao):
    def __init__(self):
        super().__init__(6, "Leia um número real e mostre o seu dobro e a sua terça parte.")

    def resolver(self):
        print("\n" * 2)
        print(f"--- Executando Questão {self.numero}: {self.enunciado} ---\n")
        numero = leia_float_brl("Digite um número real: ")
        dobro = numero * 2
        terc = numero / 3
        print(f"O dobro de {numero} é {formatar_brl(dobro)}\nA terça parte de {numero} é {formatar_brl(terc)}")
        print("\n--- Fim da Questão 6 ---")
        input("Pressione Enter para voltar ao menu...")
