# Operadores in e not in
# in (está entre) not in (não está entre)

# Strings são iteráveis ( iteravel é algo que vc pode navegar item por item), exemplo:
# abaixo a string Thiago, pode navegar em cada letra, utilizando os indices da string, 
# tanto positivos como negativos. exemplo: abaixo o T está no indice 0, o h no 
# indice 1, o i o indice 2, e assim por diante até terminar a string. 
# E temos indices negativos tbm. Exemplo: o T está no -6, o h no -5 e assim por diante:
#  0 1 2 3 4 5
#  T h i a g o 
# -6-5-4-3-2-1

# na pratica, quero acessar um indice, por exemplo o i. para isso eu crio a variavel:

nome="Thiago"
# e comando print, com a variavel (no caso nome) e o indice tenho que colocar dentro
# de colchete: 

print(nome [2])

#no caso acima ele vai me retornar : i

# poderia fazer ao contrario, buscando com o negativo, o
# lhando da direita para esquerda [-4]:

nome="Thiago"
print(nome [-4])

# no exemplo abaixo: o programa busca no nome (usando o in) se existe a letra que 
# digitou:

nome=input(" Digite seu nome")
encontrar=input("Digite o que encontrar")

if encontrar in nome:
    print( encontrar, "está no",  nome)

else:
    print(encontrar, "não está no", nome)

# O operador not in é o inverso. exempo abaixo, o in procura a letra no nome e 
# responde True para sim e false para não. 
nome= ('Thiago')
print('T' in nome)
print('w' in nome)
#Agora com in not:
print('T' not in nome)
print('w' not in nome)
