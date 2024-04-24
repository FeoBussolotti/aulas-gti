nome = (input ('Qual o seu nome?'))
idade = int (input ('Qual a sua idade?'))
salario = float (input ('Qual o seu salário?'))
hora = int (input ('Quantas horas você trabalha por dia?'))

salarioStr = str('%.2f'%salario)
salarioReal = salarioStr.replace('.',',')

salarioDia = (salario ) / 30
salarioDiaStr = str('%.2f'%salarioDia)
salarioDiaReal = salarioDiaStr.replace('.',',')

print ('Olá %s, você tem %d anos, trabalha %d horas por dia, seu salário é de R$%s e você recebe R$%s por dia trabalhado!' % (nome, idade, hora, salarioReal, salarioDiaReal))