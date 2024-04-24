distancia = int(input('Qual a distância(Km) deseja percorrer? \n'))
if distancia <= 200:
    preco = distancia * 0.50
    precoStr = str ('%.2f'%preco)
    precoReal = precoStr.replace('.',',')
else:
    preco = distancia * 0.45
    precoStr = str ('%.2f'%preco)
    precoReal = precoStr.replace('.',',')
print('O preço da passagem é de R$%s'%precoReal)