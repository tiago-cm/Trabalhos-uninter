def imprimeMenu():
    print('-----Bem-vindo a Loja de Marmitas do Tiago Costa Moraes----')
    print('-------------------------Cardápio--------------------------')
    print('-----------------------------------------------------------')
    print(f'---| Tamanho | Bife Acebolado(BA) | Filé de Frango(FF) |---')
    print(f'---|    P    |      R$ {BA_tamanho_p}       |      R$ {FF_tamanho_p}       |---')
    print(f'---|    M    |      R$ {BA_tamanho_m}       |      R$ {FF_tamanho_m}       |---')
    print(f'---|    G    |      R$ {BA_tamanho_g}       |      R$ {FF_tamanho_g}       |---')
    print('-----------------------------------------------------------')

#armazena valores do Bife Acebolado de acordo com seu tamanho
BA_tamanho_p = 16.00
BA_tamanho_m = 18.00
BA_tamanho_g = 22.00

#armazena valores do Filé de Frango de acordo com seu tamanho
FF_tamanho_p = 15.00
FF_tamanho_m = 17.00
FF_tamanho_g = 21.00

totalCompra    = 0
valor_unitario = 0

#chama a função que imprime o menu
imprimeMenu()

#Loop do menu.
while True:
    #Entrada do sabor digitado pelo cliente
    sabor = str(input('Entre com o sabor desejado (BA/FF): '))
    
    #Verificação da entrada, Se BA ou FF, pede entrada do tamanho. Se não for igual BA ou FF, solicita nova inclusão do sabor
    if (sabor == 'BA') or (sabor == 'FF'):
        #Se sabor BA, pergunta o tamanho do Bife Acebolado
        if (sabor == 'BA'):
            produto = 'Bife Acebolado'
            tamanho = str(input('Entre com o tamanho desejado (P/M/G): '))  
            if   tamanho == 'P':
                valor_unitario = BA_tamanho_p
            elif tamanho == 'M':
                valor_unitario = BA_tamanho_m
            elif tamanho == 'G':
                valor_unitario = BA_tamanho_g
            else:
                print('Tamanho inválido. Tente novamente')
                continue
        
        #Se sabor FF, pergunta o tamanho do Filé de Frango
        elif (sabor == 'FF'):
            produto = 'Filé de Frango'
            tamanho = str(input('Entre com o tamanho desejado (P/M/G): '))
            if   tamanho == 'P':
                valor_unitario = FF_tamanho_p
            elif tamanho == 'M':
                valor_unitario = FF_tamanho_m
            elif tamanho == 'G':
                valor_unitario = FF_tamanho_g
            else:
                print('Tamanho inválido. Tente novamente')
                continue
        
        totalCompra += valor_unitario
        
        print(f'Você pediu um {produto} no tamanho {tamanho}: R$ {valor_unitario:.2f}')

        #Se cliente quiser mais pedido, continua no loop, se não, sai do loop
        sair = str(input(('Deseja mais alguma coisa? (S/N): ')))
        if sair == 'S':
            continue 
        else:
            break
    else:
        print('Sabor inválido. Tente novamente')
    
print(f'O valor total a ser pago: R$ {totalCompra:.2f}')