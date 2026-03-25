def mostrar_menu():
  print("//menu de vendas\\") 
  print("1 - adicionar vendas")
  print("2 - conferir total acumulado")
  print("3 - conferir valor de quebra")
  print("4 - encerrar operação")

def adicionar_venda(total):
  valor = int(input("digite o valor de venda"))
  total += valor 
  print("venda adicionada:", total)
  return total


def mostrar_total(total):
  print("total acumulado;", total)

def mostrar_quebra(total):
  if total > 50000:
    print("valor de quebra:", total - 50000)
  else:
    print("meta ainda não atingida")

"""aplicando partimentação "def" """

total = 0

while True:
  mostrar_menu()
  opcao = input("escolha uma opção: ")

  if opcao == "1":
    total= adicionar_venda(total)

  elif opcao == "2":
    mostrar_total(total)

  elif opcao == "3":
    mostrar_quebra(total)

  elif opcao == "4":
    print("processo encerrado")
    break

  else:
    print("opção inválida")



