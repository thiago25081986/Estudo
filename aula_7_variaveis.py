# Variaveis são usadas para salvar algo na memoria do computador.
# PEP8: imicie variaveis com letras minusculas, pode usar 
# numeros e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para 
# atribuir um valor a um nome (variavel).
# Uso: nome_variavel = expressão. 
# pode se imaginar a variavel como um apelido . exemplo abaixo
nome_completo= 'Thiago Gonçalves Toledo Seixas'
# Agora se eu executar com o comando print:
print(nome_completo)
#o resultado sera: Thiago Gonçalves Toledo Seixas
# posso passr para a variavel qualquer tipo de dado que eu quiser.Segue exemplo abaixo:
soma_dois_mais_dois= 2+2
#agora da o comando print com a variavel
print(soma_dois_mais_dois)
# resultado será 4
# juntar tudo agora, pq essas duas variaveis estão gravadas na memoria. exemplo:
print(nome_completo, soma_dois_mais_dois)
""" Variaveis não são usadas para abreviar codigos. 
Variaveis são usadas para deixar o codigo mais legivel e para você não repetir 
coisas em lugares que você vai usar a mesma coisa."""
#exemplo, pegando o exemplo de aula passado:
#print(int('1'), type(int('1')))
"""se o meu codigo tivesse varias vezes essa repetição e eu necessitasse mudar o int, 
não precisaria mudar um por um, eu crio a variavel e assi que eu mudar na variavel, 
a mudança acorrerá em todas as citações int. ou seja eu só tenho um ponto para 
alterar o meu codigo. na pratica, exemplo abaixo: """  
int_um= int('1')
print(int_um, type(int_um))
# o resultado será: 1 <class 'int'>. 
#Agora digamos que queira mudar para boolean, mudei tbm o nome da variavel 
numeral_um= (bool())
print(numeral_um, type (numeral_um))
#o resultado será: False <class 'bool'> obs: false pq náo tem numero ou espaço entre ()
#obs: o nome da variavel tem que refletir sobre o que tem nela. 
# No caso acima d VARIAVEL INT, O NOME NÃO É BOM PQ CASO ALGUEM QUE LEIA, 
#PODE ACHAR QUE É UM NUMERO INTEIRO (INT)
#EXERCICIO:

nome='Thiago'
idade= 10
maior_de_idade= idade >=18
print('Nome:', nome, 'Idade:', idade)
print('É maior de idade?', maior_de_idade)
#no caso acima a variavel idade está dentro da variavel maior de idade?



