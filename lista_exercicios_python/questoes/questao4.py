from .base import Questao
from .utils import leia_float_brl, formatar_brl

class Questao4(Questao):
    def __init__(self):
        super().__init__(4, "Leia as duas notas de um aluno e mostre a média.")

    def resolver(self):
        print("\n" * 2)
        print(f"--- Executando Questão {self.numero}: {self.enunciado} ---\n")
        nota1 = leia_float_brl("Digite a primeira nota do aluno: ")
        nota2 = leia_float_brl("Digite a segunda nota do aluno: ")
        media = (nota1 + nota2) / 2
        print(f"A média entre {nota1} e {nota2} = {formatar_brl(media)}")
        print("\n--- Fim da Questão 4 ---")
        input("Pressione Enter para voltar ao menu...")
