from armazenamento import salvar_contas

def depositar(contas):
    numero = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor do depósito: ").replace(",", "."))
    
    for conta in contas:
        if conta["numero"] == numero:
            conta["saldo"] += valor
            conta["extrato"].append(f"Depósito = +R$ {valor:.2f}")
            salvar_contas(contas)
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
            input("Pressione Enter para continuar...")
            return
    
    print("\nNúmero de conta não encontrado.")
    input("Pressione Enter para voltar...")

def sacar(contas):
    numero = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor do saque: "))
    
    for conta in contas:
        if conta["numero"] == numero:
            if conta["saldo"] >= valor:
                conta["saldo"] -= valor
                conta["extrato"].append(f"Saque = -R$ {valor:.2f}")
                salvar_contas(contas)
                print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
                input("Pressione Enter para continuar...")

        else:
            print("Saldo insuficiente.")
            input("Pressione Enter para voltar...")

        return
    
    print("\nNúmero de conta não encontrado.")
    input("Pressione Enter para voltar...")


def ver_saldo(contas):
    numero=int(input("Digite o número da conta: "))

    for conta in contas:
        if conta["numero"] == numero:

            print("===EXTRATO===")

            if not conta["extrato"]:
                print("Nenhuma movimentação realizada.")
            else:
                for movimento in conta["extrato"]:
                    print(movimento)

            print(f"\nSaldo: R$ {conta['saldo']:.2f}")
            input("\nPressione Enter para voltar...")

            return
    print("\nNúmero de conta não encontrado.")
    input("Pressione Enter para voltar...")


def ver_extrato(contas):
    numero=int(input("Digite o número da conta: "))

    for conta in contas:
        if conta["numero"] == numero:

            print("===EXTRATO===")

            if not conta["extrato"]:
                print("Nenhuma movimentação realizada.")
            else:
                for movimento in conta["extrato"]:
                    print(movimento)

            print(f"\nSaldo: R$ {conta['saldo']:.2f}")
            input("\nPressione Enter para voltar...")

            return
    print("\nNúmero de conta não encontrado.")
    input("Pressione Enter para voltar...")