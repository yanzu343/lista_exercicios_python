
#Menu principal para executar as questões

import os
import sys
import pkgutil
import importlib
from questoes import QUESTOES_MAP
import ctypes

def enable_utf8_windows():
    #Habilita UTF-8 no console do Windows para suportar acentuação
    if os.name == 'nt':
        try:

            ctypes.windll.kernel32.SetConsoleCP(65001)
            ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        except Exception:
            pass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    enable_utf8_windows()
    while True:
        clear_screen()
        print("""    #############################################
#   Lista de Exercícios de Lógica em Python  #
#############################################
""")
        for key, q in sorted(QUESTOES_MAP.items(), key=lambda x: int(x[0])):
            print(f"{key} - {q.enunciado}")
        print("0 - Sair\n" + "-" * 45)
        escolha = input("Digite o número da questão que deseja executar: ").strip()
        if escolha == "0":
            print("Obrigado por usar o programa! Até a próxima.")
            break
        questao = QUESTOES_MAP.get(escolha)
        if questao:
            try:
                questao.resolver()
            except Exception as exc:
                print(f"Ocorreu um erro ao executar a questão: {exc}")
                input("Pressione Enter para voltar ao menu...")
        else:
            print("Opção inválida! Por favor, tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == '__main__':
    main()
