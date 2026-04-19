import math

largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))

area = largura * altura

qde_litros = math.ceil(area / 2.0)

print(f"Para uma parede de area {area:.2f} u.a. são necessários {qde_litros} L de tinta.")
