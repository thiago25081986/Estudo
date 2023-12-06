# Conversão de tipos, coerção,
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutaveis e primitivos
# str, int, float, bool (uma vez criados, não pode alterar)
"""conversão de tipo, mesmo operador para fazer coisas diferentes.. 
enxemplo: comando print(1+1) resultado será 2, mas posso fazer print(‘a”+”b”), 
sendo a e b o que eu quiser definir na programação. """
print(1 + 1)
print('a'+'b')
""" mas posso usar uma conversão, por exemplo... o usuario tem que digitar um numero e 
acaba digitando junto uma string. exemplo: tem que digitar 1 e digita '1', converter
ea string(1 com aspas) em um numero (int ou Float), exemplo abaixo irá dar erro"""
#print('1'+1)
"""exemplo acima o '1' entre aspas é considerado uma string, por estar entre as aspas
nesse caso precisa converter ele para um numero (int, ou float).""" 
#exemplo abaixo fazer o comando e a clase para observação
print('1', type('1'))
# o resultado será 1 <class 'str'>"""
#para inverter a classe usar o int. Segue exemplo abaixo
print(int('1'), type(int('1')))
'''no exemplo acima, o programa mostrará = 1 <class 'int'>, sendo a primeira parte, 
o 1 e apartir do type o codigo mostra a classe na resposta'''
#na pratica agora, será colocado a soma de '1'+1 convertendo
#'1' em int
print(int('1')+1)
#o resultado será = 2
#outro exemplo, convertendo 2 numeros= 1° float e o segundo int 
print(int('1') + 1)
# outro exemplo, mostrando a classe:
print(type(int('1')+1))
#no caso acma vai aparecer <class 'float'>
# ecemplo 3- converter uma string para Boolean
print(bool("1"))
print(int('1'))
#outro exemplo, converter um int (numero em letra) 11+b
print(str (11) + 'b')
#outro exemplo, converter dois numeros em string
print(str(11) + str(10))




