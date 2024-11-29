soma = 0
contador = 0
while contador < 5:
    nota = float(input("Digite a nota: "))
    soma += nota
    contador += 1
media = soma / 5
print(f'A média das notas é {media}:')