print('Calculadora IMC')

variavel_entrada=input("Você quer entrar no sistema para calcular o IMC? Digite sim ou não.   ")
if variavel_entrada=="sim":
    print('Você entrou no sistema')

elif variavel_entrada=="não":
    print('você saiu do sistema')

else:
    print("Você não digiou sim ou não")

print('Para calcular preencha os seguintes dados:')

variavel_nome=input('Seu nome completo e ao final clique enter  ')

numero_altura=float(input('Digite sua altura em numeros e após tecle enter '))

numero_peso=float(input('Digite seu peso e após tecle entar '))


variavel_imc=numero_peso /(numero_altura*numero_altura)

# Mano os 3 printś abaixo queria fazer numa unica linha, 
# mas uma hora dava certo, e outra dava errado, não sei o pq, acho que é o programa. 
# Pensei em fazer assim: print(f'{variavel_nome} Seu IMC é de:{variavel_im:.3f}').
# estaria correto?
print(variavel_nome)
print('Seu IMC é de:')
print(variavel_imc)

if variavel_imc>=24.9:
    print("Você está com sobre peso.")

elif variavel_imc<24.9:
    print('Você está com o IMC correto')



