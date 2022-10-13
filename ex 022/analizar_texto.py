from time import sleep
"""
Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome ', end='')
for i in range(1, 4):
    sleep(1)
    print(' .', end='')
sleep(1)
print('')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)-nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')
