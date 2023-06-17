import global_funcion 

moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
notas = [100, 50, 20, 10, 5]


print('''
|############################################|
|  Bem vindo ao sisteme de calculo de Troco  |
|############################################|
|Criado por Samuel Moraes                    |
|############################################|
''')

val = global_funcion.calcula_troco()
numNotas, numMoedas = global_funcion.calcula_notas(val)
global_funcion.mostrador(notas, moedas, numNotas, numMoedas)