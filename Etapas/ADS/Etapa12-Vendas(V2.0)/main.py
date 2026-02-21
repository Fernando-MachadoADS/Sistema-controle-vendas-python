"""
Arquivo principal do sistema.
Responsável pela interface com o usuário (menu e inputs).
Regra de negócio isolada na classe ContaVendas.

Deixando a organização e comentários mais profissionais pra exportar pro github.

OBS:Tudo que eu aprendo e aplico nesse código é usado para testar
visando outros futuros projetos.
"""

from conta_vendas import ContaVendas
from utilidades import slow

# =========================
# REQUISIÇÃO DE SENHA SIMPLES
# =========================
slow("OLÁ USUÁRIO")

senha = input("Insira seu código de acesso (É '123'): ") #Pensando que anteriormente o usuário que fosse testar não saberia como acessar kkkk
if senha != "123":
    print("Código de acesso inválido")
    exit()

slow("BEM VINDO!")
print("---- MENU ----")

# Centro do sistema
conta = ContaVendas()

# =========================
# MENU INTERATIVO
# =========================
while True:

    print("\n1 - Adicionar venda") #Detalhe interessante de quebra de linha(igual a: 'print()')
    print("2 - Adicionar baixa")
    print("3 - Exibir valor total")
    print("4 - Exibir extrato")
    print("5 - Conferir sobra")
    print("6 - Encerrar")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        print("você selecionou: Adicionar vendas")
        try:
            valor = float(input(">>> Insira o valor da venda: "))
            ok, msg = conta.adicionar_venda(valor)
            print(msg)
        except ValueError:
            print("Valor inválido")

    elif opcao == "2":
        print("Você selecionou: Adicionar baixa")
        try:
            valor = float(input(">>> Insira o valor da baixa: "))

            print("Selecione um motivo:")
            print("1 - Devolução")
            print("2 - Sangria")
            print("3 - Vale")

            motivos = {
                "1": "devolução",
                "2": "sangria",
                "3": "vale"
            }

            escolha = input("Digite uma opção: ")

            if escolha in motivos:
                ok, msg = conta.adicionar_baixa(valor, motivos[escolha])
                print(msg)
            else:
                print("Motivo inválido")

        except ValueError:
            print("Valor inválido")

    elif opcao == "3":
        print("Você selecionou: Exibir valor total")
        print(f"Total atual: R$ {conta.calcular_total():.2f}")

    elif opcao == "4":
        print("Você selecionou: Exibir extrato")
        conta.exibir_extrato()

    elif opcao == "5":
        print("Você selecionou: Conferir sobra")
        sobra = conta.conferir_sobra()
        if sobra > 0:
            print(f"Valor excedente: R$ {sobra:.2f}")
        else:
            print("Não há sobras no momento")

    elif opcao == "6":
        print("Sistema encerrado.")
        print("Até logo!")
        break

    else:
        print("Opção inválida")