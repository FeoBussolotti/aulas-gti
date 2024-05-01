contador = 0
numero = int(input('Digite um número: '))
par_ou_impar = input('Digite (P) para Par e (I) para ímpar: ').upper()
if par_ou_impar == 'P':
        while contador <= numero:
            print (contador)
            contador+= 2
elif par_ou_impar == 'I':
        contador = 1
        while contador <= numero:
            print (contador)
            contador+= 2
