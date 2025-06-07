import random

def main():
  print ("Bem vindo ao jogo de adivinhação!")
  numAleattório = random.randint(1, 200)

  tentativas = 0
  numDigitado = 0

  while numDigitado != numAleatorio
    numDigitado = int(input("Digite um número: "))

    if numDigitado > numAleatorio:
      print("voc~e acertou!")
      break
    elif numDigitado < numAleatorio
      print("o numero digitado é maior que o numero aleatório")
    else:
      print("o numero digitado é menor que o numero aleatório") 
    tentativas += 1

  print("você acertou com ", tentativas, "tentativas")

  return 0
main()
