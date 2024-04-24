def calcular_valor_por_hora(salario_total, horas_por_dia):
    # Considerando o mês com 30 dias
    dias_no_mes = 30
    # Calcula o total de horas trabalhadas no mês
    horas_no_mes = horas_por_dia * dias_no_mes
    # Calcula o valor recebido por hora
    valor_por_hora = salario_total / horas_no_mes
    return valor_por_hora

def main():
    # Solicita o salário total e a quantidade de horas trabalhadas por dia ao usuário
    salario_total = float(input("Digite o salário total: R$"))
    horas_por_dia = float(input("Digite quantas horas você trabalha por dia: "))

    # Calcula o valor recebido por hora
    valor_por_hora = calcular_valor_por_hora(salario_total, horas_por_dia)

    # Imprime o valor recebido por hora
    print(f"Você recebe R${valor_por_hora:.2f} por hora trabalhada.")

if __name__ == "__main__":
    main()
