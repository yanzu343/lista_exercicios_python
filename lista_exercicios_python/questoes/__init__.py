
#Pacote de questões expõe um dicionário QUESTOES_MAP com as instâncias das questões
from .base import Questao
from .questao1 import Questao1
from .questao2 import Questao2
from .questao3 import Questao3
from .questao4 import Questao4
from .questao5 import Questao5
from .questao6 import Questao6
from .questao7 import Questao7
from .questao8 import Questao8
from .questao9 import Questao9
from .questao10 import Questao10
from .questao11 import Questao11
from .questao12 import Questao12

QUESTOES_MAP = {
    "1": Questao1(),
    "2": Questao2(),
    "3": Questao3(),
    "4": Questao4(),
    "5": Questao5(),
    "6": Questao6(),
    "7": Questao7(),
    "8": Questao8(),
    "9": Questao9(),
    "10": Questao10(),
    "11": Questao11(),
    "12": Questao12(),
}
__all__ = ["QUESTOES_MAP"]
