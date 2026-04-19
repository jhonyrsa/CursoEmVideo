entrada = input("Digite algo: ")

print("A entrada é um número? {}".format(entrada.isnumeric()))
print("A entrada é somente letras? {}".format(entrada.isalpha()))
print("A entrada é um texto com números? {}".format(entrada.isalnum()))
print("A entrada está toda maiúscula? {}".format(entrada.isupper()))
print("A entrada está toda minúscula? {}".format(entrada.islower()))