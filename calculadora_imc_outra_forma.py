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

"""Copiei o mesmo programa, e mudei o final, colocandou a variavel (linha_1)
para formartar, o ponto flutuante do resultado do IMC, e comentei os prints """

linha_1= f'{variavel_nome} você tem IMC de {variavel_imc:,.2f} '

print(linha_1)
#print(variavel_nome)
#print('Seu IMC é de:')
#print(variavel_formatação)

if variavel_imc>=24.9:
    print("Você está com sobre peso.")

elif variavel_imc<24.9:
    print('Você está com o IMC correto')



