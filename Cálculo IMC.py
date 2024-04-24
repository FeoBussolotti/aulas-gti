def calcular_imc(peso, altura):
    # Calcula o IMC usando a fórmula peso / (altura ** 2)
    imc = peso / (altura * altura)
    return imc

def main():
    # Solicita ao usuário para informar o peso e a altura
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em metros): "))

    # Calcula o IMC usando a função calcular_imc
    imc = calcular_imc(peso, altura)

    # Imprime o resultado do IMC
    print("Seu IMC é:", imc)

if __name__ == "__main__":
    main()
