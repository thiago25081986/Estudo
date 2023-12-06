# Operadores Logicos

# or (ou) 

# OBS: OR é parecido com and, só que com uma diferença:
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada 
# naquele valor. 


# São considerados Falsy (o que já vi). OBS: Verificar o que é falsy
# 0 (zero), 0.0 (zero.zero), "" (str vazia), False

# Também existe o tipo None que é usado para representar um não valor. 

# Usar o or para melhorar o programa anterior:

entrada=input("[E]ntrar [S]air ")

senha_digitada = input ('Senha: ')

senha_permitida = "123456"

# if entrada=="E" and senha_digitada == senha_permitida:
#    print("Entrar")

# else :
#    print("Sair")

# no exemplo acima, o usuario tem que digitar o E ou S maiusculo, se não o programa 
# não aceita. ness caso é preciso permitir o E (maiusculo) ou e (minusculo). 
# Agora vamos utilizar o comando or para isso. 
# OBS: para não dar erro (ambiguidade), para o programa entender que é 1 avaliação
#E ou e, pod se usar o () para ele ler primeiro o que está dentro, igual nas operações
# aritméticas, tudo que está entre parenteses() é resolvido primeiro. 
# Fica:

if (entrada == "E" or entrada== "e") and senha_digitada == senha_permitida:
    print(" Entrar")

else:
    print("sair")

# obs: esse comando vai parar no primeiro verdadeiro que ele achar. Exe:
# print( 0 or false or 0 or 'abc' or True)
# no caso acima ele pararia no abc e já retornaria 
# isso permite fazer uma avaliação "if" com apenas uma linha de comando. exemplo:

senha=input('Senha:  ') or 'Sem Senha'
print(senha)