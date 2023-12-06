#exemplo abaixo mostra que o input, entra como string (str)
numero_1=int (input('Digite um numero:  '))
numero_2=int (input('Digite outro numero:  '))

print(' A soma dos dois numeros é', numero_1+numero_2)
#no caso acima, resultado foi 15 pq houve a concatenação. é necessário converter
#a str

# para inverter pode-se envolver nas linha das variaveis a inversão, mas pode 
#ocorrer problemas. há outra maneira de fazer, a sequencia é sempre de dentro para fora
#exe: numero_1=int(input(' Digite um numero:  '))

'''OBS: dessa maneira pode acontecer eerro, pq digamos que o usuario digite ao invés de
um numero, uma letra. Ai o programa já trava logo no começo, sem passar da primeira
linha. O certo é fazer uma checagem, mas isso vou ver mais para frentem mas
por exemplo:'''
numero_1=int (input('Digite um numero:  '))
numero_2=int (input('Digite outro numero:  '))
int_numero_1= int(numero_1)
int_numero_2= int(numero_2)
print(' A soma dos dois numeros é', int_numero_1+int_numero_2)

# o caso acima, o usuario ainda pode digitar uma str no lugar do numero, mas o codigo 
#quebra depois. 
