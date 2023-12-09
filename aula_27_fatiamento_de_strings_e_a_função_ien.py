'''
Fatiamento de Strings

LEMBRANDO QUE AS STRINGS SÃO ITERAVEIS, PODEMOS IR DE ELEMENTO A ELEMENTO
DENTRO DA ESTRING. PODEMOS PEGAR LETRA POR LETRA.

TEMOS BM OS INDICES. NO CASO ABAIXO, NO INDICE 0 TEMOS O O, 
NO INDICE 2, TEM O L E ASSIM POR DIANTE. 


  012345678
  Olá Mundo
 -987654321

 TAMBÉM TEMOS INDICES PODITIVOS E NEGATIVOS: -9 É O O. -8 É O L. OU SEJA NO CASO 
 ACIMA O O É REPRESENTADO TANTO PELO 0 COMO PELA -9


 Fatiamento  [ i : f : p ] [ : : ]
 
 obs.: a função len retona a quantidade de caracteres da string 
 
 '''

variavel = "Olá mundo"
#PODEMOS ACESSAR QUALQUER INDICE DA VARIAVEL ACIMA, USANDO OS COLCHETES. EXEMPLO:
#abaixo vou acessar o indice 5 (letra U). NO PRINT SAIRÁ = U

print(variavel [5])

# OU SE EU QUISER USAR O INDICE NEGATIVO, TERÁ QUE SER O -4 PARA ESSA LETRA, NESSE
# EXEMPLO:
print (variavel [-4])

# Agora o que podemos fazer é utilizar o fatiamento (pegar uma fatia da string):
# [ inicio : fim ]

# primeiro define de onde vai começar o fatiamento. no caso abaixo, vou definir que 
# irá começar no indice 4 até o fim. nesse caso eu 
# não ponho nada (omito o fim) depois dos :(pontos)

print (variavel [4: ])

# agora se eu definir o final, em python geralmente o final não é incluido. 
# exemplo: digamos que quero parar no 7 (letra d), se eu colocar 7, 
# ele não vai incluir a letra d. Resultado do print abaixo foi: mun

print (variavel [4:7])

# ou seja sempre que eu quiser o final eu vou colocar um indice a mais.
# pegando o mesmo caso de cima,ficaria assim:


print (variavel [4 : 8])

# Posso omitir o inicio também. assim ele sabe que 
# é para começar no inicio da string. exemplo:

print (variavel [ : 5])

# Poderia usar os indices negativos também:
print (variavel [-8: -2])

# OBS: lembrando para não confundir.. se pegar algum espaço, é um caracter normal, 
# conta bytes, normal da programação, mas ele não vai exibir nada na tela. 
#Exemplo abaixo, peguei o indice 3. Como é um espaço, ele não vai aparecer nada
# na tela:

print( variavel [3])

# inclusive em python existe a função len. Essa função conta 
# os caracteres das strings. exemplo abaixo, passei a função,colocando o indice 3, 
#ou seja só vai mostrar a quantidade de 1 carctere. print: 1

print(len(variavel [3]))

# Se eu tirar o indice e jogar a função len, ela vai contar 
# todos os caracteres da string. exemplo abaixo dará 9. print 9
# obs: contagem de indice começa do zero. Agora a quantidade 
# de caracter começa do 1. 
# no exemplo abaixo, essa string, tem 9 caracteres. 

print(len(variavel))


# Ou seja, quando quiser checar o tamanho de uma string, pode usar a função len. 

# Passo:

# mostra a string de 1 em 1, ou de 2 em 2 e assim por diante.exemplo abaixo. 
# vou pegar do 0 ao 9 com passo de 2 em 2. comando será [0:9:2]. exemplo:

print(variavel [0:9:2])

# resultado será: Oámno. 

# Pode ser de 4 em 4. exemplo:

print(variavel[0:9:4])

# Curiosidade:
# no exemplo abaixo se colocar de 3 em 3 ele fica confuso pq pega o espaço (pula):

print(variavel[0:9:3])

# pode inverter a string, se no passo colocar numero negativo. No exempplo abaixo
# ele está pegando de 0 a 9, pelos numeros negativos. 

print (variavel [::-1])

# resultado do print: odnum álO

# Agora se quiser colocar o incio e o fim negativo 
# usando o passo, tenho que colocar o incio e o fim tbm negativos. exemplo:

print(variavel [ -1:-10: -1])

# pode ir negativo e pular de 2 ou mais também:

print(variavel [-1 : -10 : -2])

# resultado do print: onmáO


