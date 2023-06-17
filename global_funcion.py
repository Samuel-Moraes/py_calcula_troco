import subprocess
import os

# Limpa o console
def limpar_console():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)
#

def calcula_troco(): 
    repetidor = 1
    total_compra = float(input("Digite o total da compra: "))
    while repetidor:
        valor_recebido = float(input("Digite o valor recebido: "))
        troco = valor_recebido - total_compra

        if(valor_recebido < total_compra):
            print('O valor recebido é inferior ao total da compra!')
        else:
            repetidor = 0
            return troco
        
def calcula_notas(val):
    numNotas = []
    numMoedas = []

    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    notas = [200, 100, 50, 20, 10, 5]
    moedas.sort()
    moedas.reverse()

    notas.sort()
    notas.reverse() 

    for i in notas:
        numNotas.append(val/i)
        val %= i


    for i in moedas:
        numMoedas.append(val/i)
        val %= i
    
    return numNotas, numMoedas

def mostrador(notas, moedas, numNotas, numMoedas):
    print('')
    for i in range(len(notas)):
        print("Notas de %d = %d" % (notas[i], numNotas[i]))

    print("")

    for i in range(len(moedas)):
        print("Moedas de %a = %d" % (moedas[i], numMoedas[i]))
    print('')

def chama_cabecalho():
    print('''
|############################################|
|  Bem vindo ao sisteme de calculo de Troco  |
|############################################|
|Criado por Samuel Moraes                    |
|############################################|
''')
