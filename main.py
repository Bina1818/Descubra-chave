from adivinha import gerar_chave, verificar_chave

erros = 0
chave = gerar_chave()
print("Descubra a chave !")
print("Está entre 0 e 100")
while True:
    try:
        op = int(input(": "))
        resultado = verificar_chave(chave, op)
    except ValueError:
        print("Erro de Valor: Chave precisa ser um número inteiro")
        continue
    if resultado == 1:
        print("Chave é maior")
        erros = erros + 1

    elif resultado == -1:
        print("Chave é menor")
        erros = erros + 1

    else:
        print("Chave é igual")
        break
print(f"Erros: {erros}")