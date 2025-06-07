def main():
  idade = int(input("Digite sua idade: "))

  if idade >= 18:
    print("entrada liberada!")
  elif idade >= 16:
    acompanhante = input("possui um acompanhante? (s/n): ")
    if acompanhante  or acompanhante == "s" :
      print("entrada liberada!")
    else:
      print("entrada proibida!")
  else:
    print("entrada proibida!")
  return 0
main()
