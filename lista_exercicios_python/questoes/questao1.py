
from .base import Questao

class Questao1(Questao):
    def __init__(self):
        super().__init__(1, "Leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.")

    def resolver(self):
        print("\n" * 2)
        print(f"--- Executando Questão {self.numero}: {self.enunciado} ---\n")
        nome = input("Qual é o seu nome? ").strip()
        if not nome:
            nome = "Usuário"
        print(f"\nOlá {nome}, é um prazer te conhecer!")
        print("\n--- Fim da Questão 1 ---")
        input("Pressione Enter para voltar ao menu...")
