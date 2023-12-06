#nessa aula vamos ver operadores aritméticos(matematica).adição 2 numeros int, resultado
#sempre será um numero inteiro. adição 1 int e 1 float, o resultado sempre será float.
adicao = 10+10
print('Adição:', adicao)

subtracao = 10-5
print('Subtração:', subtracao)

multiplicacao = 10 * 10
print('Multiplicação:', multiplicacao)

# a divisão abaixo com 1 barra, sempre vai devolver um float, independente
# se for a divisão por 2 numeros int. no caso abaixo= 5.0
divisao = 10 / 2
print('Divisão:', divisao)

# Outra divisão com 2 barras, pode dar resultado, tanto numero inteiro como float. 
#Irá depender, se tive 2 numeros float, retorna float, se tiver 2 int, retorna int. 
# mas ela pode truncar o numero. Ela não retorna as casas decimais, ela corta. 
#exemplo, na de cima de 1 barra o resultado foi:4.54545454... 
# na de baixo com 2 barras o reaultado foi: 4.0
divisao_inteira = 10 // 2.2
print('Divisão inteira:', divisao_inteira)

exponenciacao = 2 ** 10
print ('Exponenciação:', exponenciacao)

# modulo retorna o resto de uma divisão. Exemplo abaixo, o retorno é de 1, ou seja
#55 não é divisivel por 2. Dessa forma d'para saber se o numeo é par ou impar
modulo = 55 % 2 
print('Modulo:', modulo)

# Segundo exemplo
modulo = 10 % 5
print('Modulo:', modulo)
# no exemplo acima, resultado é 0, pq não tem resto da divisão de 10 para 5.  

# Posso usar o boolean para saber sobre resto tbm. exemplo. 
print(10 % 8 ==0)
#no caso acima, é falso pq a divisão de 10 para 8 não tem sobra 0. 

# 2 exemplo com boolean
print(10 % 5 == 0)
# no caso acima será verdadeiro, pq não tem resto da divisão de 10 para 5.

