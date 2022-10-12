from random import choice
"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""
aluno = []
for i in range(1, 5):
    aluno.append(input(f'{i}° Aluno: '))
print(f'O aluno escolhido foi {choice(aluno)}')
