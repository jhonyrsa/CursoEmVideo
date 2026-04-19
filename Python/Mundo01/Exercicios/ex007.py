def media_nota(num1, num2):
    return (num1 + num2) / 2

print("{:=^5} Média de notas {:=^5}".format("", ""))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = media_nota(nota1, nota2)

print("A média do aluno é {:.2f}.".format(media))