from .base import Questao
from .utils import leia_float_brl,formatar_brl

class Questao12(Questao):
    def __init__(self):
        super().__init__(13, "Leia o salário de um funcionário e calcule o novo salário com 15% de aumento.")

    def resolver(self):
        print("\n" * 2)
        print(f"--- Executando Questão {self.numero}: {self.enunciado} ---\n")

        #Lógica questão 13
        salario = leia_float_brl("Digite o salário atual do funcionário (R$): ")
        aumento = salario * 0.15
        novo_salario = salario + aumento

        print(f"\nSalário original: R$ {salario:.2f}")
        print(f"Aumento (15%): R$ {formatar_brl(aumento)}\n")
        print(f"Novo salário: R$ {formatar_brl(novo_salario)}\n")

        print("\n--- Fim da Questão 13 ---")
        input("Pressione Enter para voltar ao menu...")