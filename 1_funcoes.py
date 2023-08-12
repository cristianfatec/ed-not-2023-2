# FUNCAO QUE CALCULA O IMC DE UMA PESSOA
def calc_imc(peso, altura):
    return peso / altura **2

# p=85 
# a=1.72  #em todas as linguagens de programação usa-se ponto e não vírgula
# imc=calc_imc (p,a)

# print('o individuo tem imc igual á: ' , imc)

print(calc_imc(85,1.72))
