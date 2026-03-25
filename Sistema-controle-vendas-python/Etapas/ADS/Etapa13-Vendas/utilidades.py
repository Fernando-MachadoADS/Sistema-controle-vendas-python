import time


def slow(texto, velocidade=0.05):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidade)
    print()