"""
Módulo: utilidades
Responsabilidade: Funções auxiliares reutilizáveis.
"""

import time

def slow(texto, velocidade=0.1):
    """
    Exibe texto com efeito de digitação lenta.
    Utilizado apenas para melhorar experiência visual no terminal.
    """
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidade)
    print()