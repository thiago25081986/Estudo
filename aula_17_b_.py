

# Outro exemplo:
condicao_1=False
condicao_2=True
condicao_3=True
condicao_4=False


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

print(" Outro Bloco")

"""OBS: No caso acima, há duas condições verdadeirass, mas o programa só irá mostrar 
a primeira que ele encontrar, e pula a segunda, pulando tbm todo o bloco, e só 
mostra o que tiver fora do bloco. No caso acima ele mostrou: Codigo para condição 2
e depois : print(" Outro Bloco"), pois esse print já está fora do bloco """