'''
Interpolação basica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''
# INTERPOLAÇÃO É A MESMA COISA QUE FOI FEITO COM O FORMAT ou FSTRINGS. Pode escolher uma das tres
# EXPLICAÇÃO:

nome = "Thiago" #nome é uma string

preco = 1000.95897643 #preço é um numero de ponto flutuante


# variavel=" Thiago o preço total foi de R$ 1000.95"

# a variavel acima mostraria o que eu quero escrever, mas posso formatar isso po interpolação. 
# Seria assim:

#variavel = ' %s, o preço total foi de R$ %f ' % (nome, preco)

# no caso acima coloquei % e o s (s representa a string, conforme a tabela no começo) 
# para substituir o nome e % f (f representa numero float, conforme tabela no começo )
# depois eu abro parenteses e ponho as variaveis dentro dele. OBS: Precisa ser na sequencia, exemplo:
# primeiro veio %s (s de string) e no parenteses primeiro tem que ver o nome (variavel string) e assim
# por diante. Não pode faltar e nem inverter as variaveis entre os parenteses. Mesma quantidade dos dois 
# lados e mesma sequencia. O print será: Thiago, o preço total foi de R$ 1000.958976 

#OBS: tbm posso formatar quantas casas decimais quero do ponto flutuante, u
# sando o .(numero de casas decimais) e of igual o fstring. Ficaria assim:
# variavel = ' %s, o preço total foi de R$ %.2f ' % (nome, preco)

variavel= " %s , o preço total é de R$ %.2f" %(nome, preco)

#print é: Thiago , o preço total é de R$ 1000.96 (dois pontos de casas decimais conforme 0 .2f)

print(variavel)

# Outro exemplo usando agora para hexadecimal. Vou fazer direto:

print((' O hexadecimal de %d é %x') %(524, 524))

# a Resposta será: O hexadecimal de 524 é 20c. O 20c, poderia ser maisculo se no %x, eu colocasse o 
# X maiusculo. Ficaria: O hexadecimal de 524 é 20C
# tbm posso colocar quantas casas decimais quero apresentar no haxadecimal, colocando por exemplo
# um numero na frente do x. exemplo %08x. Ficaria 8 casas decimais no hexadecimal. 