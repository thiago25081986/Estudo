primeira_variavel= input(" Digite aqui o 1° Valor  ")
segunda_variavel= input(" Digite aqui o segundo valor")

if primeira_variavel>segunda_variavel:
    print('Primeiro Valor', primeira_variavel, 
          "é maior ou igual o segundo valor =",
            segunda_variavel)

elif primeira_variavel<segunda_variavel:
    print('Segundo Valor =', segunda_variavel, 
          "é maior do que o primeiro valor =", 
          primeira_variavel)
    
elif primeira_variavel==segunda_variavel:
    print("Os dois numeros são iguais")


'''OBS: O otavio colocou f'no print.. pq?. ele colocou
print(
      f'{primeiro valor=} é maior ou igual
      f'ao que {segundo_valor=}'
)
Perguntar para o Marcos'''