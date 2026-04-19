val_real = float(input("Informe quanto você tem na carteira: "))

PRECO_DOLAR = 3.27

val_dolar = val_real / PRECO_DOLAR

print("Com R$ {:.2f} é possível comprar US$ {:.2f}.".format(val_real,val_dolar))