def entrada_dados():
    numero = int(input("Informe um número: "))
    return numero

def calcula_tabuada(numero, i):
    return numero * i

def saida_dados():
    numero = entrada_dados()
    print("====== Tabuada do {:2d} ======".format(numero))
    for i in range(0,11):
        print("{:4d} x {:2d} = {:4d}".format(numero, i, calcula_tabuada(numero, i)))

saida_dados()