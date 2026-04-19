def entrada_usuario():
    entrada = input("Digite algo pelo teclado: ")
    return entrada

entrada = entrada_usuario()

print("A entrada é um número? {}".format(entrada.isnumeric()))
print("A entrada são letras? {}".format(entrada.isalpha()))
print("A entrada está toda maiúscula? {}".format(entrada.isupper()))
print("A entrada está toda minúscula? {}".format(entrada.islower()))
print("A entrada é alfanumérica? {}".format(entrada.isalnum()))
print("A entrada é UTF-8? {}".format(entrada.isascii()))
print("A entrada é capitalizada? {}".format(entrada.istitle()))