#LISTAS
#Listas são uma forma de armazenar mais de um valor em única váriavel. Os valores podem ser de tipos diferentes.
#A lista é definida pelo uso dos colchetes "[]"

#Uma lista de números
valores=[2,3,5,7,9,11]

#Uma lista com valores de tipos variados
mix=["batata", 1.25, True, "Tomate", 44]

#Lista de Strings
legumes=["batata", "tomate", "abobrinha", "cenoura"]

#Operações sobre listas
#1) Percurso: Significa percorrer a lista do primeiro ao ultimo elemento, fazendo algo com cada um deles.

#Imprimindo cada um dos elementos, um por linha:
for val in valores:
    print(val)

for lis in mix:
    print(lis)

#imprimindo o dobro de valor de cada elemento da lista
for x in valores:
    print (x*2)

#imprimindo um traço de 40 hífens
print ("-"*40)

#2)Inserindo um novo elemento no *FIM* da lista 

valores.append(13)
legumes.append("cebola")


print(valores)
print(legumes)

#3)Inserindo um novo elemento em uma posição especidicada
#       Parâmetros:
#       1º: a posicção onde será inserido um novo elemento
#       2º: O novo elemento a ser inserido

legumes.insert(2,"mandioquinha")
print(legumes)

#4)Acessando um valor em uma posição específica
print ("Elemento na QUARTA posição: ", valores [3])
print ("Elemento na PRIMEIRA posição: ", valores [0])
print ("Elemento na ULTIMA posição: ", valores [-1])
print ("Elemento na PENULTIMA posição: ", valores [-2])