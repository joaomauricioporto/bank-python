from armazenamento import salvar_contas

def criar_conta(contas):
    nome = input("Digite seu nome completo: ")
    cpf = input("Digite seu CPF: ")
    numero = len(contas) + 1

    conta = {
        "nome": nome,
        "cpf": cpf,
        "numero": numero,
        "saldo": 0,
        "extrato": []
    }

    contas.append(conta)
    salvar_contas(contas)

    print("\nCadastro criado com sucesso!")
    print(f"Seu número de conta é: {numero}")
    input("Pressione Enter para continuar...")

def listar(contas):
    if not contas:
        print("\nNenhuma conta foi criada.")
        input("Digite ENTER para voltar...")
        return
    
    for conta in contas:
        print(f"Conta: {conta["numero"]}")
        print(f"Nome: {conta["nome"]}")
        print(f"CPF: {conta["cpf"]}")
        print(f"Saldo: {conta["saldo"]}")
    input("\nPressione Enter para continuar...")

def deletar_conta(contas):
    if not contas:
        print("\nNenhuma conta foi criada.")
        input("Digite ENTER para voltar...")
        return
    
    numero = int(input("\nDigite o número da conta a deletar: "))
    
    for i, conta in enumerate(contas):
        if conta["numero"] == numero:
            confirmar = input(f"\nTem certeza que deseja deletar a conta de {conta['nome']}? (s/n): ")
            if confirmar.lower() == "s":
                contas.pop(i)
                salvar_contas(contas)
                print("\nConta deletada com sucesso!")
                input("Pressione Enter para continuar...")
            else:
                print("\nOperação cancelada.")
                input("Pressione Enter para continuar...")
            return
    
    print("\nNúmero de conta não encontrado.")
    input("Pressione Enter para voltar...")