preco_atual = float(input("Informe o preço atual da mercadoria: R$ "))

desconto = preco_atual * 0.05

novo_preco = preco_atual - desconto

print(f"A mercadoria x de R$ {preco_atual:.2f} sai por R$ {novo_preco:.2f} com desconto.")