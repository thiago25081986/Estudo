# Introdução a if, elif e else
# if= se
# elif = se não se
# else = se não
# nesse comando podemos mudar o fluxo de codigo, pois condiciona, tipo faça isso,
# ou faça aquilo, ou seja, faz com que o interpretador atue numa linha de codigo 
# ou não. há varios blocos de codigo e um deles é i if, elif, else
# começando com a entrada de dados:
entrada=input(' Você quer entrar no sistema?  ')
# agora começa com if, depois passa uma condição (pergunta), e quando faço a pergnta
# eu tenho como retorno um dado boolean, então nessa condição eu tenho true ou false
# mas não necessariamente eu preciso colocar true e false depois do if, eu posso colocar, 
#por exemplo abaixo if entrada=='entrar', ou seja se o usuario digitar 'entrar'
# eu quero eu quero executar esse techo do codigo: print("Você entrou no sistema").
#para fazer com que o print (trecho), pertença ao if, devo apertar tab para ter o 
# espaço conforme abaixo:
if entrada== "entrar":
    print("Você entrou no sistema")

# agora se o usuario digitou sair, vai para a proxima condição que é: se entrada é 
# igual a sair, print= vc saiu do sistema. exemplo abaixo=

elif entrada== "sair":
    print('Você saiu do sistema')

#agora temos uma terceira opção: else, serve para por exemplo, se caso o usuario não 
#escreveu entrar e nem sair, escreveu outra coisa. segue abaixo
else:
    print("Você não digitou nem entrar e nem sair")

#if, elif e else, dependem um do outro. a unica que pode ser sozinho é o if, pq é 
#a primeira condição, então posso ter if, if e else, e if elif e else. 
#e o elif pode se repetir.

''' e no caso dos blocos, apenas o bloque que o usuario escolheu, será apreentado
ou seja, se ele escolheu entrar, o bloco e print do elif e do else, não rodam, mas o 
restante das linhas da programação após rodam. ou seja o interpretador do pyton só 
roda o que for verdadeiro e o restante da programação exemplo abaixo:'''
entrada=input(' Você quer entrar no sistema?  ')
if entrada== "entrar":
    print("Você entrou no sistema")

    print('AEUFF')

elif entrada=='sair':
    print('Você saiu do sistema')

else:
    print('Você Não digitou nem entrar e nem sair')

print(1341234)

#no caso acima eu digitei entrar e depois apresentou: print("Você entrou no sistema")
# print('AEUFF')
# print(1341234)
# o print(1341234) está fora dos blocos pq ele não está com o tab. o print('AEUFF')
# está na condição de if (dentro do bloco), devido ao espaço, se tirar o espaço, o 
#o programa dá erro. 