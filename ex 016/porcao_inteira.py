from math import trunc
""" Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. """

n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a sua porçao inteira é {trunc(n)}')
