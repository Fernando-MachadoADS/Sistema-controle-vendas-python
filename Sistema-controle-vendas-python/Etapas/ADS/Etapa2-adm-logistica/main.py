"""aqui coloco em pratica todos os conceitos até agora usando como inspiração 
uma experiência pessoal com logística, automatizando uma operação diária"""


peso_da_carga = int(input("digite o peso (kg)"))
quantidade_de_pallets = int(input("digite a quantidade de pallets (un)"))
cavalo = 10000 
pallets = 25.7  
peso_total_dos_pallets = quantidade_de_pallets * pallets 
peso_total_da_carga = peso_da_carga + quantidade_de_pallets + cavalo + peso_total_dos_pallets 

if peso_total_da_carga >= 50000:  
    print("peso da carga excedeu o limite", peso_total_da_carga)
else: 
    print("pesagem bem sucedida, peso total da carga:", peso_total_da_carga)

"""agora introdução á repetições"""

limite_de_passageiros = 1

while limite_de_passageiros <= 100:
    print("conferência passageiros", limite_de_passageiros)
    limite_de_passageiros = limite_de_passageiros + 1


