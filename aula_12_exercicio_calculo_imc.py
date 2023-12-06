# Calcular o IMC - Indice de massa corporal
# Formula para o calculo= IMC = peso / (altura X altura)
nome = "Thiago Seixas"
altura = 1.80
peso = 100
imc = peso / (altura * altura)
print('IMC:', imc)

#Outra forma de fazer seria:
imc = peso /(altura**2)
print("IMC:", imc)

#mais completo:
print(nome, "tem", altura, 'de altura', ', pesa', peso,'quilos', 'e seu imc é', imc)

# ... Tres pontinhos é chamado de elipses
# pode ser usado como placeholder, um codigo que ainda não foi escrito e não gera erro
# exeplo, vou escrever um codigo e um treco ainda não sei o que vou colocar
# posso escrever naquele trecho ... e continuar o meu codigo que não vai ter erro
# escreve exemplo: print (...)
#print(...)  