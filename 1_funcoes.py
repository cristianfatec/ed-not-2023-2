# FUNCAO QUE CALCULA O IMC DE UMA PESSOA
def calc_imc(peso, altura):
    return peso / altura **2

# p=85 
# a=1.72  #em todas as linguagens de programação usa-se ponto e não vírgula
# imc=calc_imc (p,a)

# print('o individuo tem imc igual á: ' , imc)

print(calc_imc(85,1.72 ))

#------------------------------------Exemplo Aula 14-08-2023----------------------------------

#docstrig (identificada por """ 3 aspas duplas - Comentário de documentação para funções e classes) - A diferença desse para "#" é que convencionou-se que a ultima por sua vez atende a função de comentar qualuqer coisa e as aspas tripla para cmentar pa funcoes e classes, e também um aceita somente uma linha de texto enquanto o outro várias

# = é para atribuição (ex a=2) = = é para comparação 
"""
    funcao que calcula a área de uma figura geométrica plana
"""
from math import pi 

def calc_area (base, altura, tipo):
   resultado= none                                  #Valor não existente

    if tipo=="R"                                    :#Retângulo
        resultado=base*altura
    elif tipo == "T":                               #Triângulo
        resultado=base*altura/2
    elif tipo == "E":                               #Elipse
        resultado=(base/2)*(altura/2)*pi
    return resultado
print ("Retângulo 20x30: ", calc_area(5,4, "R"))
print ("Triângulo 45x32: ", calc_area(45,32, "T"))
print ("Elipse 10x15: ", calc_area(10,15, "E"))
print ("Desconhecido 12x16: ", calc_area(12,16, "X"))



