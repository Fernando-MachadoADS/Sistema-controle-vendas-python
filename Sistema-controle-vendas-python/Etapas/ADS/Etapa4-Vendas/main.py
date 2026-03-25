#Adicionando listas pra um sistema de vendas intermediário:

def adicionar_venda(vendas):
    valor = int(input("valor de venda: "))
    vendas.append(valor )
    print("venda registrada!")

def adicionar_baixa(vendas):
    valor = int(input("-valor da baixa"))
    vendas.append(-valor)
    
    

    print("baixa registrada")


def mostrar_total(vendas):
    print("total acumulado:",sum(vendas))


def mostrar_histórico(vendas):
    for venda in vendas:

        print(venda)


def conferir_quebra(vendas):
    total = sum(vendas)

    if total > 50000:
        print("valor da quebra: ", total - 50000)

    else:
        print("meta ainda não atingida")

    


vendas = []

while True:
    print("1 - adicionar venda")
    print("2 - total")
    print("3 - listar vendas")
    print("4 - conferir quebra")
    print("5 - sair")
    print("6 - adicionar baixa")

    opcao = input("opção: ")

    if opcao == "1":
        adicionar_venda(vendas)
    
    elif opcao == "2":
        mostrar_total(vendas)

    elif opcao == "3":
        mostrar_histórico(vendas) 

    elif opcao == "4":
        conferir_quebra( vendas)

    elif opcao == "5":
        print("processo encerrado.")
        break

    elif opcao == "6":
        adicionar_baixa(vendas)


    else:
        print("opção inválida!")
