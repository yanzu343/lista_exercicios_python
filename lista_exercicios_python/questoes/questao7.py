from .base import Questao
from .utils import leia_float_brl

class Questao7(Questao):
    def __init__(self):
        super().__init__(7, "Leia uma distância em metros e mostre em outras medidas (km, hm, dam, dm, cm, mm).")

    def resolver(self):
        print("\n" * 2)
        print(f"--- Executando Questão {self.numero}: {self.enunciado} ---\n")
        distancia = leia_float_brl("Digite o valor em metros: ")
        conversions = {
            'km': distancia / 1000,
            'hm': distancia / 100,
            'dam': distancia / 10,
            'dm': distancia * 10,
            'cm': distancia * 100,
            'mm': distancia * 1000,
        }
        print("Resultados:")
        for k, v in conversions.items():
            print(f"De metros para {k} = {v}")
        print("\n--- Fim da Questão 7 ---")
        input("Pressione Enter para voltar ao menu...")
