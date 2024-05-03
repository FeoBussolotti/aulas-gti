consumo=float(input("Qual o valor consumido em KWH?\n"))
tipo=str(input("Qual o tipo de instalção? - Residencial(R)-Comercial(C)-Industrial(I)\n")).upper()

if tipo == ("R"):
    if consumo <= 500:
            preco = consumo *  0.40
    else:
            preco = consumo *  0.65
elif tipo == ("C"):
    if consumo <= 1000:
            preco = consumo *  0.55
    else:
            preco = consumo *  0.60
elif tipo == ("I"):
    if consumo <= 5000:
            preco = consumo *  0.55
    else:
            preco = consumo * 0.60
print("Consumo: ", consumo, "KWH")
print("Tipo de instalação: ", tipo)
print("Preço a pagar: R$", preco)