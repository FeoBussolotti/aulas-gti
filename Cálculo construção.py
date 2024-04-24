def calcular_custo_construcao(area):
    # Custo por metro quadrado de construção
    custo_por_metro_quadrado = 850
    # Calcula o custo total de construção multiplicando a área pela taxa de custo por metro quadrado
    custo_total = area*custo_por_metro_quadrado
    return custo_total

def main():
    # Solicita as medidas do terreno ao usuário
    comprimento = float(input("Digite o comprimento do terreno (em metros): "))
    largura = float(input("Digite a largura do terreno (em metros): "))

    # Calcula a área do terreno retangular
    area_terreno = comprimento*largura

    # Calcula o custo para construir uma casa no terreno
    custo_construcao = calcular_custo_construcao(area_terreno)

    # Imprime o custo total da construção
    print(f"O custo total para construir uma casa nesse terreno é de R${custo_construcao:.2f}.")

if __name__ == "__main__":
    main()
