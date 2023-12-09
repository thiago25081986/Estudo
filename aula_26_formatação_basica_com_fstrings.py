
"""Formatação Basica de Strings"""

# Formatação por Fstrings é mais novo, logo com a formatação de interpolação, 
#pode ser que algumas coisas não funcionem.
"""
S - string
d - int
f - float
< numero de digitos> f
x ou X - Hexadecimal
( Caractere) ( ><^ ) ( quantidade )
> - Esquerda
< - Direita
^ - Centro
= - Força o numero a aparecer antes do zeros
Sinal - + ou -
Ex.: 0 > - 100, .1f
Conversion flags - !r !s !a
"""
# exemplos:

variavel = " ABC "

print(f' {variavel} ')

# Suponha que tenho a variavel de novo e quero preencher as laterais do lado esquerdo dela com espaço  
# até prencher com 10 caracteres. no caso eu preencho com : o caractere que quero, 
# no caso abaixo será o espaço, Sinal de esquerda (>), mais a quantidade
# de caractere. exemplo:

print(f' {variavel: >10}')

# Posso colocar tbm para a direita: obs: o ponto no final é apenas para enchergar o espaço

print(f'{variavel: <7}.')

#posso colocar no centro tbm: OBS: ponto direito e esquerdo novamente é para enchegar os espaços

print (f'.{variavel : ^10} .')

#exemplo com outros caracteres

print (f'.{variavel :#^10} .')
print (f'.{variavel :#>10} .')
print (f'.{variavel :&^10} .')

# agora com . (numero de digitos) f. Posso usar o . para separar o ponto flutuante e 
# posso usar a ,(virgula), paa separar o milhar

print(f'{100.4873648123746:,.2f}')

# também posso especificar o numero se é positivo ou negativo  + (positivo) ou - (negativo), 
# Colocando os sinais na frente. exemplo de um positivo:

print(f'{100.4873648123746:+,.2f}')

#posso usar o sinal = (igual) para aparecer os zeros antes do numero. 
# exemplo abaixo, vou usar 20 caracteres:

print(f'{100.4873648123746:0=+20,.2f}')

# fazendo o hexadecimal. obs: coloquei 0(numero de 0), e 8(numero de caracteres). pode ser x ou X
# (minusculo ou maiusculo)

print(f'O hexadecimal de 1500 é {1500: 08x}')

