"""
Python= linguagem de programação
tipo de tipagem= dinamica/forte
str > string > são textos, colocados dentro de aspas simples ou duplas
"""
print(1234)

# aspas simples, exemplo abaixo
print('Thiago Seixas')

# aspas duplas, exemplo abaixo
print("thiago seixas")

# escape
# se quiser colocar uma aspas dentro do meu texto, eu tenho que usar o scape 
# o escape é \"
#exemplo com aspas duplas
print('thiago\"o incrivel\"')
#exemplo com aspas simples 
print("thiago \'o incrivel\'")
# r
# se eu colocar o R ele mostrará a barra, serve para expressões regulare, 
#vamos ver isso mais pra frente, mas exemplo:
print(r'thiago\'o incrivel\'')
print('thiago "seixas"')
print("thiago \'seixas\'")
print(1, 3, sep="$")
print(1, 3, "Thiago'o incrivel'", end='##')
print('casa', end="$%$")
print("casa 'thiago'")
print ('thiago', end="@")
print(r"thiago\'o incrivel\'", end='\n')
#comentario dando tudo errado 
print(1,2, end='#\n')
print("thiago, 'o incrivel'")
print('thiago\"o incrivel\"')