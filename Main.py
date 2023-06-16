import global_funcion

numNotas = []
numMoedas = []

# Valores que podem ser recebidos

# Notas
notas = [100, 50, 20, 10, 5]
notas.sort()
notas.reverse() 

# Moedas
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
moedas.sort()
moedas.reverse()

print('''
|############################################|
|  Bem vindo ao sisteme de calculo de Troco  |
|############################################|
|Criado por Samuel Moraes                    |
|############################################|
''')

global_funcion.calcula_troco()

'''
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
'''