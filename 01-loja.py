#Imprime mensagem de boas vindas
print('Bem-vindo a loja do Tiago Costa Moraes')

#Recebe o valor do pedido
valorDoPedido = float(input('Digite o valor do pedido: '))

#Recebe a quantidade de parcelas
quantidadeParcelas = int(input('Digite a quantidade de parcelas: '))

#Verifica a quantidade de parcelas para definir a taxa de juros
if (quantidadeParcelas < 4):
    juros = 0/100
elif (quantidadeParcelas >= 4 and quantidadeParcelas < 6):
    juros = 4/100
elif (quantidadeParcelas >= 6 and quantidadeParcelas < 9):
    juros = 8/100
elif (quantidadeParcelas >= 9 and quantidadeParcelas < 13):
    juros = 16/100
else:
    juros = 32/100

#Armazena o valor da parcela
valorDaParcela = (valorDoPedido * (1+juros)) / quantidadeParcelas

#Armazena o valor total da compra com juros
valorTotalParcelado = valorDaParcela * quantidadeParcelas

#Imprime o valor das parcelas
print(f'O valor das parcelas é R$ {valorDaParcela:.2f}')

#Imprime o valor total parcelado se a quantidade de parcelas for igual ou maior que 4 
if quantidadeParcelas >= 4:
    print(f'O valor Total Parcelado é R$ {valorTotalParcelado:.2f}')