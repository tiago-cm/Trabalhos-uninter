print('Bem vindo a Empresa do Tiago Costa Moraes')
print('-----------------------------------------')

#Definição da lista
lista_funcionarios = []
#Armazena meu ID
id_global = 4929254 

#Função de cadastro de funcionarios
def cadastrar_funcionario():
    print('-------MENU CADASTRAR FUNCIONÁRIO--------')
    #Cadastro de funcionario
    print(f'Id do Funcionário: {id_global}')
    funcionario = {
        "id": id_global,
        "nome": input("Digite o nome do funcionário: "),
        "setor": input("Digite o setor do funcionário: "),
        "salario": float(input("Digite o salário do funcionário: "))
    }
    lista_funcionarios.append(funcionario)
    print('-----------------------------------------')

#Função de consulta de funcionarios
def consulta_funcionarios():
    while True:
        print('Escolha a opção desejada: ')
        print('1 - Consultar Todos os Funcionários ')
        print('2 - Consulta Funcionários por id ')
        print('3 - Consultar Funcionário(s) por setor ')
        print('4 - Retornar ')
        print('--------------------------')
        opcaoMenuConsultaFuncionario = int(input('>>'))
        #Verifica opção de consulta
        if (opcaoMenuConsultaFuncionario == 1):
            for funcionario in lista_funcionarios:
                print(f"Id: {funcionario['id']}\nNome: {funcionario['nome']}\nSetor: {funcionario['setor']}\nSalário: {funcionario['salario']}\n")
                

        elif (opcaoMenuConsultaFuncionario == 2):
            id_global = int(input("Digite o id do funcionário: "))
            print('--------------------------')
            for funcionario in lista_funcionarios:
                if funcionario["id"] == id_global:
                    print(f"Id: {funcionario['id']}\nNome: {funcionario['nome']}\nSetor: {funcionario['setor']}\nSalário: {funcionario['salario']}\n")
                    print('--------------------------')
                    break

        elif (opcaoMenuConsultaFuncionario == 3):
            setor_consulta = input("Digite o setor do funcionário: ")
            print('--------------------------')
            for funcionario in lista_funcionarios:
                if funcionario["setor"] == setor_consulta:
                    print(f"Id: {funcionario['id']}\nNome: {funcionario['nome']}\nSetor: {funcionario['setor']}\nSalário: {funcionario['salario']}\n")
                    print('--------------------------')

        elif (opcaoMenuConsultaFuncionario == 4):
            break
        
        else:
            print('Opção Inválida')
            continue

#Função de remover funcionarios
def remover_funcionario():
    while True:
        id_global = int(input("Digite o id do funcionário a ser removido: "))
        #Loop que busca o funcionario peloi ID para remoção.
        for funcionario in lista_funcionarios:
            #Se achou id, remove, se não, informa na tela e volta no menu principal
            if funcionario["id"] == id_global:
                lista_funcionarios.remove(funcionario)
                print("Funcionário removido com sucesso")
                break
            else:
                print("Id inválido")
                break
        break

#Menu principal
while True:
    print('-------------Menu Principal--------------')
    print('1 - Cadastrar Funcionários')
    print('2 - Consultar Funcionário(s)')
    print('3 - Remove Funconário')
    print('4 - Sair')
    opcaoMenuPrincipal = int(input('>>'))
    if (opcaoMenuPrincipal == 1):
        id_global += 1
        cadastrar_funcionario()
    elif(opcaoMenuPrincipal == 2):
        consulta_funcionarios()
    elif(opcaoMenuPrincipal == 3):
        remover_funcionario()
    elif(opcaoMenuPrincipal == 4):
        break
    else:
        print('Opção Inválida\nTente novamente: ')
        continue


