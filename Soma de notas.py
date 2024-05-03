nota1=float(input("Insira a primeira nota (0 a 25)\n"))
if (nota1 <0 or nota1 > 25):
     print ("Nota inválida")
     exit()
nota2=float(input("Insira a segunda nota (0 a 25)\n"))
if (nota2 <0 or nota1 > 25):
     print ("Nota inválida")
     exit()
nota3=float(input("Insira a terceira nota (0 a 25)\n"))
if (nota3 <0 or nota1 > 25):
     print ("Nota inválida")
     exit()
nota4=float(input("Insira a quarta nota (0 a 25)\n"))
if (nota4 <0 or nota1 > 25):
     print ("Nota inválida")
     exit()

notaTotal = nota1+nota2+nota3+nota4

if notaTotal >= 80:
    print('Aluno aprovado - EXCELENTE')
elif notaTotal >= 60:
    print('Aluno aprovado')
elif notaTotal >= 40:
    print('Aluno em recuperação')
else:
    print('Aluno reprovado')