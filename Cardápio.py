print("""
╭╮╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
┃┃╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱╱┃┃╱╱╱┃╭━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
┃┃╱╱╭━━┳━╮╭━━┫╰━┳━━┳━╮╭━┻╮╭╋━━╮╭━╯┣━━╮┃╰━━┳━━┳━┳━╮╭━━┳━╮╭━╯┣━━╮
┃┃╱╭┫╭╮┃╭╮┫╭━┫╭╮┃╭╮┃╭╮┫┃━┫┃┃┃━┫┃╭╮┃╭╮┃┃╭━━┫┃━┫╭┫╭╮┫╭╮┃╭╮┫╭╮┃╭╮┃
┃╰━╯┃╭╮┃┃┃┃╰━┫┃┃┃╰╯┃┃┃┃┃━┫╰┫┃━┫┃╰╯┃╰╯┃┃┃╱╱┃┃━┫┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰╯┃
╰━━━┻╯╰┻╯╰┻━━┻╯╰┻━━┻╯╰┻━━┻━┻━━╯╰━━┻━━╯╰╯╱╱╰━━┻╯╰╯╰┻╯╰┻╯╰┻━━┻━━╯""")

print ("-------- Salgados --------\n")
print ("__________________________")
print ("1 ---- Coxinha ---- R$5,00")
print ("2 ---- Pastel ----- R$4,50")
print ("3 ---- Quibe ------ R$6,00")
print ("4 ---- Esfiha ----- R$5,50")
print ("__________________________")

salgado=int(input("Digite qual salgado deseja: \n"))
if salgado == 1:
    preco_salgado = 5.00
    pedido_salgado = ('Coxinha ---- R$5,00, ')
elif salgado == 2:
    preco_salgado = 4.50
    pedido_salgado = ('Pastel ---- R$3,40, ')
elif salgado == 3:
    preco_salgado = 6.00
    pedido_salgado = ('Quibe ---- R$6,00, ')
elif salgado == 4:
    preco_salgado =5.50
    pedido_salgado = ('Esfiha ---- R$5,50, ')
print ("__________________________")
print ("R$",preco_salgado) 

print ("__________________________")
print ("--------- Bebidas ---------\n")
print ("1 ---- Coca Cola -- R$3,50")
print ("2 ---- Guarapam --- R$3,00")
print ("3 ---- Água s/gás - R$2,00")
print ("4 ---- Sucos ------ R$4,00")
print ("__________________________")

bebida=int(input("Digita qual bebida deseja\n"))
if bebida == 1:
    preco_bebida = 3.50
    pedido_bebida =("Coca Cola ---- R$3,50")
elif bebida == 2:
    preco_bebida = 3.00
    pedido_bebida =("Guarapam ---- R$3,00")
elif bebida == 3:
    preco_bebida = 2.00
    pedido_bebida =("Água s/gás ---- R$2,00")
elif bebida == 4:
    preco_bebida = 4.00
    pedido_bebida =("Sucos ---- R$4,00")
print ("__________________________")
print ("R$",preco_bebida)
print ("__________________________")
print (pedido_salgado+pedido_bebida)
print("Valor TOTAL:R$",preco_salgado+preco_bebida)


    