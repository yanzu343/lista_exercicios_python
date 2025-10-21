
from .base import Questao
from .utils import leia_float_brl,formatar_brl

class Questao9(Questao):
    def __init__(self):
        super().__init__(9,"Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessaria para o serviço, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.")

    def resolver(self):
        print("\n" * 2)
        print(f"--- Executando Questão {self.numero}: {self.enunciado} ---\n")
        #Lógica da questão 9:
        largura = leia_float_brl("Digite o valor em metros para a largura: ")
        altura = leia_float_brl("Digite o valor em metros para a altura: ")
        #calculo da area
        area = largura * altura
        #calculo da quantidade de tinta a ser usada
        tinta = area / 2
        print(f"Area a ser pintada: {formatar_brl(area)}\n quantidade de tinta a ser usada: {formatar_brl(tinta)}\n")

        print("\n--- Fim da Questão 9 ---")
        input("Pressione Enter para voltar ao menu...")

