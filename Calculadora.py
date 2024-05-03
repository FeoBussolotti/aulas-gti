numeroUm = float(input('Digite um número:\n'))
numeroDois = float(input('Digite outro número:\n'))
sinal = str(input('Digite um sinal (+,-,/,*):\n'))
if sinal == '+':
    print('A soma dos dois números é: %.2f' %(numeroUm + numeroDois))
elif sinal == '-':
    print('A subtração dos dois números é: %.2f' %(numeroUm - numeroDois))
elif sinal == '*':
    print('A multiplicação dos dois números é: %.2f' %(numeroUm * numeroDois))
elif sinal == '/':
    if (numeroDois!=0):
        print('A divisão dos dois números é: %.2f' %(numeroUm / numeroDois))
    else:
        print('Não é possível dividir por zero')
else:
    print ('Sinal da operação inválido')
