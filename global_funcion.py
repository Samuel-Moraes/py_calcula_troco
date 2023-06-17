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
        
 