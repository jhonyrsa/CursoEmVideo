medida_m = float(input("Informe uma medida em metros: "))

medida_cm = medida_m * 100
medida_mm = medida_m * 1000

print("{:.2f} m = {:.2f} cm = {:.2f} mm.".format(medida_m, medida_cm, medida_mm))