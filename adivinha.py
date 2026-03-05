from random import randint

def gerar_chave(inicio = 0, fim = 100):
    if inicio > fim:
        inicio, fim = fim, inicio

    if inicio < 0 or fim < 0:
        raise ValueError("Erro: Valores devem ser positivos")
    
    chave = randint(inicio, fim)
    return chave

def verificar_chave(chave, valor):
    if chave > valor:
        return 1

    elif chave < valor:
        return -1

    else:
        return 0