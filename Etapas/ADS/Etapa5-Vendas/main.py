#Adicionando blindagem utilizando "try, except" e refinando o código:

def adicionar_venda(vendas):
    try:
     valor = int(input("valor de venda: "))
     if valor <= 0:
         print("valor de venda inválido")
     else:
      vendas.append({"tipo": "venda", "valor" : valor})
      print("venda registrada!")
     
    except ValueError:
        print("digite um >número< ")
        

def adicionar_baixa(vendas):
    try:
     valor = int(input("valor da baixa: "))
     vendas.append({"tipo":"baixa", "valor": -valor}) 
     print("baixa registrada")
    except ValueError:
        print("digite um >número<") 


def mostrar_total(vendas):
    
  total = sum(item["valor"]for item in vendas)
  return total
        
        
    
    


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
        total = mostrar_total(vendas)
        print("total acumulado: ", total) 

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
