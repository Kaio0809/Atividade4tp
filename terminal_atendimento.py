from sisbanco import *

def terminal():
    sisbanco = Banco()
    while True:
        print("\nSisBanco::Bem-Vindo!")
        print(".::OPÇÕES::.")
        print("[0] - Cadastrar_Conta")
        print("[1] - Creditar")
        print("[2] - Debitar")
        print("[3] - Transferir")
        print("[4] - Consultar_Saldo")
        print("[5] - Render_Juros")
        print("[6] - Render_Bonus")
        print("[7] - Alterar_Taxa_Juros")
        print("[8] - Alterar_Taxa_Imposto")
        print("[9] - Sair")
        
        opcao = int(input("Digite uma opção: "))

        if opcao == 0:
            tipo = str(input("Tipo da conta:\nS - Simples | P - Poupança | E - Especial | I - Imposto"))
            numero = str(input("Digite o número da conta: "))
            if tipo == "S":
                conta = Conta(numero)
            elif tipo == "P":
                conta = ContaPoupanca(numero)
            elif tipo == "E":
                conta = ContaEspecial(numero)
            elif tipo == "I":
                conta = ContaImposto(numero)
            
            sisbanco.cadastrar(conta)

        elif opcao == 1:
            numero = str(input("Digite o número da conta:"))
            valor = float(input("Digite o valor creditado: "))
            sisbanco.creditar(numero,valor)

        elif opcao == 2:
            numero = str(input("Digite o número da conta:"))
            valor = float(input("Digite o valor debitado: "))
            sisbanco.debitar(numero,valor)

        elif opcao == 3:
            origem = str(input("Digite o número da conta de origem: "))
            destino = str(input("Digite o número da conta destino: "))
            valor = float(input("Digite o valor a ser traferido: "))
            sisbanco.transferir(origem,destino,valor)

        elif opcao == 4:
            numero = str(input("Digite o número da conta: "))
            print(sisbanco.saldo(numero))

        elif opcao == 9:
            print("SisBanco::Bye!")
            return
        
        elif opcao == 5:
            numero = str(input("Digite o número da conta: "))
            sisbanco.render_juros(numero)
        
        elif opcao == 6:
            numero = str(input("Digite o número da conta: "))
            sisbanco.rende_bonus(numero)

        elif opcao == 7:
            nova_taxa = float(input("Digite a nova taxa de correção da poupança: "))
            sisbanco.set_taxa_poupanca(nova_taxa)

        elif opcao == 8:
            nova_taxa = float(input("Digite a nova taxa de correção da conta Imposto: "))
            sisbanco.set_taxa_imposto(nova_taxa) 


        else:
            print("Operação Inválida!")
            continue

if __name__ == "__main__":
    terminal()