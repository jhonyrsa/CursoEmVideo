km_percorrido = float(input("Informe a quantidade de quilômetros percorridos pelo veículo: "))

dias_alugado = int(input("Informe a quantidade de dias que o veículo foi alugado: "))

PRECO_DIA = 15.99
PRECO_KM = 0.15

preco_pagar = dias_alugado * PRECO_DIA + km_percorrido * PRECO_KM

print(f"O carro foi alugado por {dias_alugado} dias e percorreu {km_percorrido:.1f} km.")
print(f"O preço final a pagar é de R$ {preco_pagar:.2f}. Acerte no caixa no fim do corredor para retirar o recibo.")