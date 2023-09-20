import Exercicios1
import Exercicios2
import os

os.system("cls")
lista = int(input("Que lista de exercicio você gostaria de acessar?\n1) Lista de exercicios 1\n2) Lista de exercicios 2\n"))

if lista == 1:
    os.system("cls")
    Exercicios1.execute()
elif lista == 2:
    os.system("cls")
    Exercicios2.execute()