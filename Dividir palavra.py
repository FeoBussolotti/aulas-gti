string = input("Digite uma palavra: ")
numLetras = int(input("Digite o número de letras para separar: "))

if numLetras <= 0 or numLetras >= len(string):
    print("Número inválido de letras para separar.")
else:
    primeira_parte = string[:numLetras]
    segunda_parte = string[numLetras:]

    print("Primeira Parte: ", primeira_parte)
    print("Segunda Parte: ", segunda_parte)