def fsucessor(num):
    return num + 1

def fantecessor(num):
    return num - 1

def entrada_dados():
    num = int(input("Informe um numero inteiro: "))
    return num

def saida_dados():
    numero = entrada_dados()
    sucessor = fsucessor(numero)
    antecessor = fantecessor(numero)
    print("O sucessor de {} é {}.".format(numero, sucessor))
    print("O antecessor de {} é {}.".format(numero, antecessor))

saida_dados()
