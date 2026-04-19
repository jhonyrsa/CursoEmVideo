salario_atual = float(input("Informe o salário do funcionário: R$ "))

ACRESCIMO = 0.15

novo_salario = salario_atual * (1 + ACRESCIMO)

print(f"O salário do funcionário X era R$ {salario_atual:.2f} e com o aumento de 15% foi para R$ {novo_salario:.2f}")