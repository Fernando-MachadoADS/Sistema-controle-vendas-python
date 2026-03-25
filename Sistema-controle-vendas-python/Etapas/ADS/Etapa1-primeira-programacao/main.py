print("ambiente configurado com sucesso")

"""aqui eu crio um contexto pra executar varias vezes essa primeira função basica
até fixar o conceito"""


nome = ("Fernando")
idade= ("21")
cidade= ("Caxias Do Sul")
email= ("limanando301@gmail.com")
qualidade = ("esforçado")


print("olá, eu sou", nome)
print("eu tenho", idade, "anos" )
print("moro em", cidade , )
print("meu e-mail pra contato é:", email ,)
print("ainda não tenho experiência com programação")
print("mas to disposto a aprender")
print("não tenho duvidas de que")
print("ficarei bom nisso, pois sou muito", qualidade ,)
print("e honestamente acredito que o nosso melhor")
print("sempre acaba sendo suficiente")
print("e nenhum esforço é em vão")
print("e realmente quero e vou dar o meu melhor!")


"""aqui eu introduzo a interação com o "usuário" """

nome = input("digite seu nome: ")
idade = input("digite sua idade: ")

print("olá", nome, )
print("você tem", idade, "anos")

"""aqui uso interação com o usuário com o basico de operações"""


meus_pontos = int(input("digite sua pontuação ")) 
pedro = 26
eduardo = 25
lucas = 25
joão = 10

total_de_pontos = (meus_pontos + pedro - eduardo * lucas - joão)

print("o total de pontos é:", total_de_pontos)


"""aqui eu testo o conceito de "if" e "else" """

idade = int(input("digite sua idade"))

if idade >= 18:
    print("você é maior de idade")
else:
    print("você é menor de idade")

"""em seguida decido abrir outra pagina pra me organizar melhor"""

