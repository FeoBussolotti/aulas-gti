num = int(input('Digite um número: '))
if num == 0 or num == 1:
    print('Esse número não é primo!')
    exit()

elif num % 2 == 0:
    print('Esse número não é primo!')
    exit()

for x in range(3, num, 2):
    if num % x == 0:
        print('Esse número não é primo!')
        exit()
print('Esse número é primo!')