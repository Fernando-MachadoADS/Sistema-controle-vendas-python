#fixando regras de user experience:



senha= input("digite o código de acesso")         #inserindo uma senha pra praticar meu entendimento
     
if senha != "123456":
   print("código de acesso inválido")
   exit()
   
  
   

def adicionar_venda(vendas):
    try:
        valor = float(input("valor de venda: "))

        if valor <= 0:
            print("valor de venda inválido")
            return

        vendas.append({"tipo": "venda", "valor": valor})
        print(f"venda registrada: R$ {valor:.2f}")

    except ValueError:
        print("digite um número válido")


def funcao_cerebro(vendas):
    total = 0

    for item in vendas:
        total += item["valor"]

    return total


def conferir_quebra(vendas, valor, tipo):
    total_atual = funcao_cerebro(vendas)

    if tipo == "baixa":
        if total_atual - valor < 0:
            print("baixa inválida, total negativo")
            return False

    return True


def adicionar_baixa(vendas):
    try:
        valor = float(input("valor da baixa: "))

        if valor <= 0:
            print("baixa inválida")
            return

        if conferir_quebra(vendas, valor, "baixa"):
            vendas.append({"tipo": "baixa", "valor": -valor})
            print(f"baixa registrada: R$ {valor:.2f}")
        else:
            print("baixa não registrada")

    except ValueError:
        print("valor inválido")


def mostrar_total(vendas):
    total = funcao_cerebro(vendas)

    if total >= 50000:
        print("meta de 50000 atingida")

    return total


def mostrar_historico(vendas):
    for venda in vendas:
        print(f"{venda['tipo']} - R$ {venda['valor']:.2f}")


def mostrar_sobra(vendas):
    meta = 50000
    total = funcao_cerebro(vendas)

    if total > meta:
        print(f"valor excedente: R$ {(total - meta):.2f}")
    else:
        print("não há valor de sobra")


# execução principal 



vendas = []

while True:
    print("1 - adicionar venda")
    print("2 - total")
    print("3 - listar vendas")
    print("4 - mostrar sobra")
    print("5 - sair")
    print("6 - adicionar baixa")

    opcao = input("opção: ")

    if opcao == "1":
        adicionar_venda(vendas)

    elif opcao == "2":
        total = mostrar_total(vendas)
        print(f"total acumulado: R$ {total:.2f}")

    elif opcao == "3":
        mostrar_historico(vendas)

    elif opcao == "4":
        mostrar_sobra(vendas)

    elif opcao == "5":
        print("processo encerrado")
        break

    elif opcao == "6":
        adicionar_baixa(vendas)

    else:
        print("opção inválida")
