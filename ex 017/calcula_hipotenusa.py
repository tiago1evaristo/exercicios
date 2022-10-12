from math import sqrt, pow
"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa."""

o = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {sqrt((pow(o,2)+(pow(a,2)))):.2f}')
