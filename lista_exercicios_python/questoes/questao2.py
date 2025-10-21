from .base import Questao
from .utils import leia_float_brl, formatar_brl

class Questao2(Questao):
    def __init__(self):
        super().__init__(2, "Leia o nome e o salário de um funcionário, mostrando uma mensagem no final.")

    def resolver(self):
        print("\n" * 2)
        print(f"--- Executando Questão {self.numero}: {self.enunciado} ---\n")
        nome = input("Nome do Funcionário: ").strip() or "Funcionário"
        salario_str = leia_float_brl("Salário: R$ ")
        print(f"\nO funcionário {nome} tem um salário de R${formatar_brl(salario_str)} em Junho.")
        print("\n--- Fim da Questão 2 ---")
        input("Pressione Enter para voltar ao menu...")
