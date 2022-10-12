from random import shuffle
"""
 O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
alunos = []
for i in range(1, 5):
    alunos.append(input(f'{i}° Aluno: '))
shuffle(alunos)
print(f'A ordem de apresentação será')
for i in range(1, 5):
    print(f'{i}° {alunos[i-1]}')
