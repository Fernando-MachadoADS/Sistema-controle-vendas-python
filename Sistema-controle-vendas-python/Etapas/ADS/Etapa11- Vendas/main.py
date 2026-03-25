import time

def slow(texto , velocidade = 0.1):                            #textando esse import bem interessante e versátil
    for letra in texto:
        print(letra, end= "", flush = True)
        time.sleep(velocidade)

    print()

slow(" OLÁ USUÁRIO")


senha= input("Insira seu código de acesso(É '123'):   ")
if senha != "123":
   print("Código de acesso inválido")
   exit()


slow("BEM VINDO!")
print("----MENU----")

class contavendas:

    def __init__(self, meta=50000):
        self.vendas = []                  #registra entradas e saidas 
        self.meta = meta                  #meta de vendas

        #função cérebro pra calcular o total atual:

    def calcular_total(self):
        total= 0
        for item in self.vendas:
            total += item["valor"]

        return total
    
        #função pra adicionar venda:

    def adicionar_venda(self, valor ):
        if valor <= 0:
            return False, "valor de venda inválido"
        
        elif valor >= self.meta:
            self.vendas.append({"tipo":"venda", "valor": valor })
            return True, f"meta de: R$ {self.meta:2f} atingida!"
        else:
            self.vendas.append({"tipo":"venda", "valor": valor})
            return True, "venda registrada"
        

        #função pra adicionar baixa:

    def adicionar_baixa(self, valor):                       #adicionar função de obervação na baixa*
            
        if valor <= 0:
            return False, "baixa inválida"
        if self.validar_baixa(valor):
            
            
            while True:

              try:
                print("Selecione um motivo:")
                print('1 - Devolução')
                print('2 - Sangria')
                print('3 - Vale')
            
                
                opcao = input("Digite uma opção:  ")
                obs = opcao

                

                if opcao == '1':
                    obs = "devolução"
                    
                if opcao == '2':
                    obs = "sangria"

                if opcao == '3':
                    obs = "vale"
                
              except ValueError:
                    print('selecione um motivo válido' )

              self.vendas.append({
                    'tipo':'baixa',
                    'valor': -valor,
                    'observacao': obs})
            
                
              return True, "baixa registrada!"
        else:
            return False, "baixa não registrada: total insuficiente"
        
        #valida baixa pra não permitir total negativo:

    def validar_baixa( self, valor):
        return self.calcular_total() - valor >= 0 
    
   
    



    #função pra conferir sobras acima da meta:




    def conferir_sobra(self):
        total= self.calcular_total()
        if total >= self.meta:
            return total - self.meta
        return 0
    
    #função pra mostrar o histórico detalhado:

    def exibir_extrato(self,):
        print("|||extrato de vendas e baixas:|||")

        for item in self.vendas:

            if item ["tipo"] == "venda":
                print(f"venda de: R$ {item['valor']:.2f}")
            
            
            if item ["tipo"] == "baixa":
                print(f"baixa de: -R$ {abs(item['valor']):.2f}  motivo: {item['observacao']}")
                
                


        print(f"Total atual: R$: { self.calcular_total():.2f}")
        sobra = self.conferir_sobra()
        if sobra > 0 :
            print(f"valor excedente á meta, sobra de: R$ {sobra:.2f}")

        print("-"*30)  


       
 #operações principais:




conta = contavendas()
while True:
    print("1 - Adicionar venda")
    print("2 - Adicionar baixa")
    print("3 - Exibir valor total")
    print("4 - Exibir histórico")
    print("5 - Calcular quebra de caixa")
    print("6 - Encerrar e sair")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        print("Você selecionou: adicionar venda")
        try:
            valor = float(input(">>>Insira o valor da venda:"))
            ok, msg =  conta.adicionar_venda(valor)
            print(msg)

        except ValueError:
            print("Insira um valor de venda válido")

    elif opcao == "2":
        print("você selecionou: adicionar baixa")
        try:
            valor = float(input(">>>Insira o valor da baixa:"))
            ok, msg = conta.adicionar_baixa(valor)
            
            print(msg)
        except ValueError:
            print("Insira um valor de baixa válido")

    elif opcao == "3":
        print("Você selecionou: Exibir valor total")
        print(f"Total atual: R$ {conta.calcular_total():.2f}")

    elif opcao == "4":
        print("Você selecionou: Exibir extrato")
        conta.exibir_extrato()

    elif opcao == "5":
        print('Você selecionou: Conferir sobra')
        sobra= conta.conferir_sobra()
        if sobra > 0:
            print(f"Valor excedente: R$ {sobra:.2f}")
        else:
            print("Não há sobras no momento")


    elif opcao == "6":
        print("//|||Operação finalizada!|||\\")
        break


    else:
        print("Insira uma opção válida!")

        