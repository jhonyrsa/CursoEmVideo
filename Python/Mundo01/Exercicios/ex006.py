def dobro_numero(num):
    return num * 2

def triplo_numero(num):
    return num * 3

def raiz_numero(num):
    return num ** (1/2)

def entrada_dados():
    numero = int(input("Informe um número inteiro: "))
    return numero

def saida_dados():
    numero = entrada_dados()
    print("O dobro de {} é {}.".format(numero, dobro_numero(numero)))
    print("O triplo de {} é {}.".format(numero, triplo_numero(numero)))
    print("A raiz quadrada de de {} é {:.3f}.".format(numero, raiz_numero(numero)))

saida_dados()