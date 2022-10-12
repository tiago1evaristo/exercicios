from math import sin, radians, cos, tan
"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
 cosseno e tangente desse ângulo."""

angulo = int(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {angulo} tem o SENO de {sin(radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cos(radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tan(radians(angulo)):.2f}')
