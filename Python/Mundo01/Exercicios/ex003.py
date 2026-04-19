#função para entrada de dados do usuário
def entrada_usuario():
    #usuário entra com dados
    numero = input("Informe um numero: ")
    #conversão do número de string para inteiro
    numero = int(numero)

    #retorna valor para usuário
    return numero

#função para soma entre dois números
def soma(n1, n2):
    #saída de dados
    return n1 + n2

#usuário entra com os números
n1 = entrada_usuario()
n2 = entrada_usuario()

#saída dos números
print("{} + {} = {}".format(n1, n2, soma(n1, n2)))