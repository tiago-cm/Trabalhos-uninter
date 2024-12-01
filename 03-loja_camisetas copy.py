#armazena valores do frete
transportadora = 100.00
sedex = 200.00

#armazena os valores de cada modelo de camiseta
MCS = 1.80
MLS = 2.10
MCE = 2.90
MLE = 3.20

#Função que imprime o menu
def imprime_modelos():
    print('MCS - Manga Curta Simples')
    print('MLS - Manga Longa Simples')
    print('MCE - Manga Curta Com Estampa')
    print('MLE - Manga Longa Com Estampa')

#Função para escolha de modelo de camisetas
def escolha_modelo():
    while True:
        print('Escolha o modelo desejado: ')
        imprime_modelos()
        modelo=str(input('>>'))
        if (modelo == 'MCS'): 
            valorDoModelo = MCS
            break
        elif(modelo == 'MLS'):
            valorDoModelo = MLS
            break
        elif(modelo == 'MCE'):
            valorDoModelo = MCE
            break
        elif(modelo == 'MLE'):
            valorDoModelo = MLE
            break
        else:
            print('Escolha inválida, entre com o modelo novamente\n\n')
            continue
    return valorDoModelo

#Função para escolha da quantidade que deseja comprar
def num_camisetas():
    while True:
        numeroDeCamisetas=int(input('Entre com o número de camisetas: '))
        modelo_e_quantidade=modelo * numeroDeCamisetas
        if numeroDeCamisetas > 20000:
            print('Não aceitamos tantas camisetas de uma vez')
            print('Por favor, entre com o número de camisetas novamente.\n\n')
            continue
        else:
            if numeroDeCamisetas >= 20 and numeroDeCamisetas < 200:
                numero_camisetas = modelo_e_quantidade * ( 1-5/100)
                break
            elif numeroDeCamisetas >= 200 and numeroDeCamisetas < 2000:
                numero_camisetas = modelo_e_quantidade *  (1-7/100 )
                break
            elif numeroDeCamisetas >= 2000 and numeroDeCamisetas < 20000:
                numero_camisetas = modelo_e_quantidade *   (1-12/100)
                break
            else:
                numero_camisetas = modelo*numeroDeCamisetas
                break
    return numero_camisetas, numeroDeCamisetas

#Função para escolha do frete
def frete():
    while True:
        print('Escolha o tipo de frete: ')
        print(f'1 - Frete por Transportadora - R$ {transportadora:.2f}')
        print(f'2 - Frete por Sedex - R$ {sedex:.2f}')
        print(f'0 - Retirar pedido na fábrica - R$ 0.00')
        estrega_escolhida=int(input('>>'))
        if (estrega_escolhida == 1): 
            valorFrete = transportadora
            break
        elif(estrega_escolhida == 2):
            valorFrete = sedex
            break
        elif(estrega_escolhida == 0):
            valorFrete = 0.00
            break
        else:
            print('Escolha inválida, entre com o modelo novamente\n\n')
            continue
    return valorFrete

modelo=escolha_modelo()
numero_camisetas, numeroDeCamisetas  = num_camisetas()
valorFrete = frete()
total = numero_camisetas + valorFrete

#Verifica a quantidade de camisetas comprada para imprimir total a pagar, com ou sem desconto
if (numeroDeCamisetas < 20):
    print(f'Total: {total} (Modelo: {modelo:.2f} * Quantidade(sem desconto): {numero_camisetas:.2f} + {valorFrete:.2f})')
else:
    print(f'Total: {total} (Modelo: {modelo:.2f} * Quantidade(com desconto): {numero_camisetas:.2f} + {valorFrete:.2f})')  


