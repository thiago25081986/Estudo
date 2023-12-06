# operador Logico "not"
# Usado para inverter expressões
# not True = False
# not False = True

#exemplo:
print(not 1)

#no caso acima, estou invertendo, era para ser true, por causa do 1, mas como o not
#está presente, eu inverto, ou seja o 1 é false. 
#Exemlo 2:

print(not True) # False

print(not False) # True


# outro exemplo:

senha=input('Digite a senha')

if not senha:
    print(" Você não digitou nada")