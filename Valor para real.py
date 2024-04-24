valor = float (input('Digite um valor: '))
valorStr = str ('%.2f'%valor)
valorReal = valorStr.replace('.',',')
print ('O valor digitado foi: R$%s'%valorReal,'!')