#armazena valores do frete
transportadora = 100.00
sedex = 200.00

#armazena os valores de cada modelo de camiseta
MCS = 1.80
MLS = 2.10
MCE = 2.90
MLE = 3.20

def imprime_modelos():
    print('MCS - Manga Curta Simples')
    print('MLS - Manga Longa Simples')
    print('MCE - Manga Curta Com Estampa')
    print('MLE - Manga Longa Com Estampa')

#valorDoModelo = 0
def escolha_modelo():
    while True:
#        print('Entre com o modelo desejado: ')
        imprime_modelos()
        modelo = str(input())
        if (modelo == 'MCS'): 
            valorDoModelo = MCS
#            return valorDoModelo
            break
        elif(modelo == 'MLS'):
            valorDoModelo = MLS
#            return valorDoModelo
            break
        elif(modelo == 'MCE'):
            valorDoModelo = MCE
#            return valorDoModelo
            break
        elif(modelo == 'MLE'):
            valorDoModelo = MLE
            break
#            return valorDoModelo
    
        else:
            print('Escolha inválida, entre com o modelo novamente')
            continue
    
    return valorDoModelo
    
    

    
escolha_modelo()
modelo_valor=escolha_modelo()
print(f'valor do modelo {valorDoModelo}' ) 
'''
def num_camisetas(valorDoModelo):
    numeroDeCamisetas=int(input('Entre com o número de camisetas: '))
    while True:
        if numeroDeCamisetas > 20000:
            print('Não aceitamos tantas camisetas de uma vez')
            numeroDeCamisetas = int(input('Por favor, entre com o número de camisetas novamente: '))
            continue
        else:
            if numeroDeCamisetas >= 20 and numeroDeCamisetas < 200:
                numero_camisetas = (valorDoModelo*numeroDeCamisetas) / 0,5
                break
            elif numeroDeCamisetas >= 200 and numeroDeCamisetas < 2000:
                numero_camisetas = (valorDoModelo*numeroDeCamisetas) / 0,7 
                break
            elif numeroDeCamisetas >= 2000 and numeroDeCamisetas < 20000:
                numero_camisetas = (valorDoModelo*numeroDeCamisetas) / 0,12
                break
            else:
                numero_camisetas = valorDoModelo*numeroDeCamisetas
                break
    return numero_Camisetas

def menu_frete():
    print(f'1 - Frete por transportadora - R$ {transportadora}')
    print(f'2 - Frete por Sedex - R$ {sedex}')
    print( '0 - Retirar pedido na fábrica - R$ 0.00')
    
def frete():
    while True:
        menu_frete()
        opcao = int(input())
        if opcao == 0:
            valor = 0.00
            break
        else:
            if opcao == 1:
                valor = 100.00
                
                break
            elif opcao == 2:
                valor = 200
                break
            else:
                opcao = int(input('Opção incorreta. Escolha o tipo de frete: '))
                continue 
    return valor

print('Bem vindo a Fábrica de Camisetas do Tiago Costa Moraes')

escolha_modelo()
'Entre com o modelo desejado: '
num_camisetas ()

frete('Escolha o tipo de frete: ')

total = (valorDoModelo * numero_camisetas) + valor

'''