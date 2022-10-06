n = int(input('Digite um número para ver sua tabuada: '))
print('-'*13)
for i in range(1, 11):
    print(f'{n:2} x {i:2} = {n*i}')
print('-'*13)
