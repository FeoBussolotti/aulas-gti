valorCasa = float(input('Qual o valor do imóvel a ser adquirido?\n'))
salario = float(input('Qual o seu salário?\n'))
anos = int(input('Em quantos anos você pretende pagar o imóvel?\n'))
if valorCasa / (anos * 12) > (salario * 0.3):
    print('Infelizmente você não pode financiar este imóvel.')
else:
    print('O imóvel de %.2f, será financiado por %d ano(s), pagando %d parcela(s) de R$%.2f'%(valorCasa, anos, (anos*12), (valorCasa/(anos*12))))
