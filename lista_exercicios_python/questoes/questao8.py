from .base import Questao
from .utils import leia_float_brl,formatar_brl

class Questao8(Questao):
    def __init__(self):
        super().__init__(8,"Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00=3,45.")

    def resolver(self):
        print("\n" * 2)
        print(f"--- Executando Questão {self.numero}: {self.enunciado} ---\n")

        # Lê o valor em reais
        carteira = leia_float_brl("Digite o valor da sua carteira em R$: ")

        # Cotação do dólar
        cotacao = 3.45

        # Calcula quantos dólares podem ser comprados
        dolares = carteira / cotacao

        # Mostra o resultado formatado com 2 casas decimais
        print(f"\nCom R$ {carteira:.2f}, você pode comprar US$ {formatar_brl(dolares)}\n")
        print("\n--- Fim da Questão 8 ---")
        input("Pressione Enter para voltar ao menu...")