# Operadores Logicos

# and (e) - or (ou) - not (não)

# OBS: and significa 'e'. Quando utiliza esse tipo de operador, é necessario mais 
# de uma coisa para checar. Ou seja.. condição  (e) outra condição. 

# and - Todas as condições precisam ser verdadeiras.

# Se qualquer valor for considerado falso, 
# a expressão inteira será avaliada naquele valor. 

# São considerados Falsy (o que já vi). OBS: Verificar o que é falsy
# 0 (zero), 0.0 (zero.zero), "" (str vazia), False

# Também existe o tipo None que é usado para representar um não valor. 

# exemplo de um sistema simples, para entender o funcionamento e a logica do end:
# no exemplo o usuario pode sigitar apenas E ou S:

# entrada=input("[E]ntrar [S]air ")

# if entrada=="E":
#    print("Entrar")

# else :
#    print("Sair")

#Agora digamos que eu queira colocar senha tbm, seria duas coisas a serem checadas.
# entãoa agora precisa utilizar o end.exemplo:

entrada=input("[E]ntrar [S]air ")

senha_digitada = input ('Senha: ')

senha_permitida = "123456"

#no exemplo abaixo, o if como ele é um bolean, ele deve ser verdadeiro (true) para ser
#@executado, e no caso abaixo tanto a entrada quanto a senha (ou seja a expressão
# inteira) devem ser exatas. 
# no exemplo abaixo, 1° chega a condição do E, se for avaliada como verdadeira, passa
# para a outra condição. Se a segnda tbm for verdadeira, ele vai entrar. 
#OBS : se a 1° condição for avaliada como false, ele nem checa a segunda. 

if entrada=="E" and senha_digitada == senha_permitida:
    print("Entrar")

else :
    print("Sair")




