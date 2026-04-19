def solicita_mensagem():
    nome = input("Informe seu nome: ")
    return nome

print("Bem vindo! {}".format(solicita_mensagem()))