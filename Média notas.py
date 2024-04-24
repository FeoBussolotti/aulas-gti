def calcular_media(nota1, nota2, nota3):
    # Calcula a média das três notas
    media = (nota1 + nota2 + nota3) / 3
    return media

def main():
    # Solicita as notas do usuário
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Imprime a média no console
    print("A média do aluno é:", calcular_media(nota1, nota2, nota3))

if __name__ == "__main__":
    main()
