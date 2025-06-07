import random

def main():
  print( "Lista de chamada")
  i = int(input("Digite a aquantidade de alunos: "))
  vet = [""] * i
  j = 0

  for i in vet:
    vet[j] = input("Digite o nome do aluno: ")
    j = j + 1

  nome = "Raissa Moura da Silva"

  print("As 5 primeiras letras do seu nome são: ", nome[0:5])
  print ("Alunos que viram hoje /n" , vet)

  return 0
main()
