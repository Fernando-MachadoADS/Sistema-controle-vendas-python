from conta_vendas import ContaVendas
from utilidades import slow


slow("OLÁ USUÁRIO")

senha = input("Insira seu código de acesso (É '123'): ")

if senha != "123":
    print("Código de acesso inválido")
    exit()

slow("BEM VINDO!")
print("\n---- MENU ----")

conta = ContaVendas()

while True:

    print("\n1 - Adicionar venda")
    print("2 - Adicionar baixa")
    print("3 - Exibir total")
    print("4 - Exibir extrato")
    print("5 - Conferir sobra")
    print("6 - Limpar histórico")
    print("7 - Comissão total")
    print("8 - Relatório mensal")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            valor = float(input("Valor da venda: "))
            ok, msg = conta.adicionar_venda(valor)
            print(msg)
        except:
            print("Valor inválido")

    elif opcao == "2":
        try:
            valor = float(input("Valor da baixa: "))

            print("1 - Devolução")
            print("2 - Sangria")
            print("3 - Vale")

            motivos = {
                "1": "devolução",
                "2": "sangria",
                "3": "vale"
            }

            escolha = input("Motivo: ")

            if escolha in motivos:
                ok, msg = conta.adicionar_baixa(valor, motivos[escolha])
                print(msg)
            else:
                print("Motivo inválido")

        except:
            print("Valor inválido")

    elif opcao == "3":
        print(f"Total: R$ {conta.calcular_total():.2f}")

    elif opcao == "4":
        conta.exibir_extrato()

    elif opcao == "5":
        sobra = conta.conferir_sobra()

        if sobra > 0:
            print(f"Sobra: R$ {sobra:.2f}")
        else:
            print("Sem sobra")

    elif opcao == "6":
        confirm = input("Tem certeza? (1 = sim): ")
        if confirm == "1":
            conta.excluir_dados()
            print("Histórico apagado")

    elif opcao == "7":
        comissao = conta.calcular_comissao()
        print(f"Comissão total: R$ {comissao:.2f}")

    elif opcao == "8":
        mes = input("Informe o mês (01-12): ")

        total_mes = conta.calcular_total_mes(mes)
        bateu = conta.meta_mes(mes)

        print(f"Total do mês {mes}: R$ {total_mes:.2f}")

        if bateu:
            print("Meta atingida!")
        else:
            print("Meta não atingida")

    elif opcao == "9":
        print("Encerrando...")
        break

    else:
        print("Opção inválida")