# Mais explicações sobre if e elif
# exemplo abaixo a condição é verdadeira.

condicao = False

if condicao: 
    print('Este é o codigo if')

#else é sempre o contrario de if
else:
    print("Este é o else do primeiro if ")

if 10==10:
    print("Outro if")

print("Fora do if")

'''no exemlo acima, resultado: não apareceu o primeiro if, pq era falsa a condição, 
apareceu else (Este é o else do primeiro if), pq era a alternativa, o if 10 == 10 
(Outro if - Outro ifpq está em outro bloco de codigo)
e o print fora do if, isso mostra que o sistema lê esse comando por blocos''' 

#OBS: pode ter if, sozinho, mas não pode ter elif e else sozinhos. 

# Outro exemplo:
condicao_1=True
condicao_2=False
condicao_3=False
condicao_4=False

# no exemplo abaixo, coloquei dois prints, apenas como exemplo para amostrar que
#posso ter quantas linhas de programação eu quiser abaixo, só tem que respeitar
#a hierarquia (espaço do bloco). No caso apareceu codig para condição 1, duas vezes
# e como o sistema achou uma condição verdadeira, ele pula o restante que do bloco

#OBS: se tivesse mais de duas condições verdadeiras, ele só iria mostrar 
# a primeira que encontrasse, e pularia a segunda. 
if condicao_1:
    print("Codigo para condição 1")
    print("Codigo para condição 1")

elif condicao_2:
    print("Codigo para condição 2")

elif condicao_3:
    print("Codigo para condição 3")

elif condicao_4:
    print("Codigo para condição 4")


else:
    print("Nenhuma condição foi satisfeita")

#No exemplo acima, posso ter varios elif para varias condições. 



