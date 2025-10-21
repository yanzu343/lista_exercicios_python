def leia_float_brl(prompt: str) -> float:
    """
    Lê um número do usuário e retorna um float.
    Aceita formatos:
      - Brasileiro: 1.234,56 ou 1234,56
      - Americano: 1,234.56 ou 1234.56
      - Inteiros: 1000, 1.000, etc.
    """
    while True:
        s = input(prompt).strip()
        s = s.replace(' ', '')  # remove espaços

        # Detecta formato brasileiro: vírgula decimal
        if ',' in s and '.' in s:
            if s.rfind(',') > s.rfind('.'):
                s = s.replace('.', '').replace(',', '.')
            else:
                s = s.replace(',', '')
        elif ',' in s:
            s = s.replace(',', '.')
        # só ponto ou nenhum -> float padrão

        try:
            return float(s)
        except ValueError:
            print("Entrada inválida! Digite um número válido (ex: 1234,56 ou 1234.56).")

def formatar_brl(valor: float) -> str:
    """
    Formata float para padrão brasileiro:
    1234.56 -> '1.234,56'
    """
    inteiro, decimal = f"{valor:.2f}".split('.')
    inteiro_formatado = f"{int(inteiro):,}".replace(',', '.')
    return f"{inteiro_formatado},{decimal}"

def leia_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("Entrada inválida! Digite um número inteiro válido.")
