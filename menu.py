import os

def limpar_tela():
    os.system("cls")

def menu():

    limpar_tela()
    print("\n=== C412 BANK ===")
    print("1 - Criar conta")
    print("2 - Ver contas")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Ver saldo")
    print("6 - Ver extrato")
    print("7 - Deletar conta")
    print("8 - Sair")