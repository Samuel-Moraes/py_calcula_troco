custo = float(input("Digite o total da compra: "))
val = float(input("Digite o valor recebido: "))
val = val - custo

if val > 0:
  notas = [100, 50, 20, 10, 5]
  notas.sort()
  notas.reverse() 

  moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
  moedas.sort()
  moedas.reverse()

  numNotas = []
  numMoedas = []

  for i in notas:
    numNotas.append(val/i)
    val %= i

  for i in moedas:
      numMoedas.append(val/i)
      val %= i

  print(" ") 

  for i in range(len(notas)):
    print("Notas de %d = %d" % (notas[i], numNotas[i]))

  print("")

  for i in range(len(moedas)):
    print("Moedas de %a = %d" % (moedas[i], numMoedas[i]))
  
else:
  print("Valor do pagamento é inferiror ao valor da compra")
