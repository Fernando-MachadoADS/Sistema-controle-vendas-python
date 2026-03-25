#Refatorando funções repetitivas:


senha= input("digite o código de acesso")        
if senha != "123456":
   print("código de acesso inválido")
   exit()
   
  
 #Essa nova função seguinte
 #organiza e concentra o código facilitando controle e manutenção:

def obter_valor_positivo(mensagem): 
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor 
            else:
                print("O valor deve ser maior que zero")
        except ValueError:
           print("Digite um número válido")
            

def adicionar_venda(vendas):
    valor = obter_valor_positivo("valor da venda: ")
    vendas.append({"tipo": "venda", "valor": valor})
    print("venda registrada com sucesso")


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
    valor= obter_valor_positivo("valor da baixa")
    if conferir_quebra(vendas, valor, "baixa"):
        vendas.append({"tipo":"baixa", "valor": -valor})
        print("Baixa registrada com sucesso")
    else:
        print("Baixa inválida")

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
