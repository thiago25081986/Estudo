# INTRODUÇÃO FORMATAÇÃO DE ISTRING
nome= "Thiago Seixas"
altura= 100050.4
peso= 150
imc= peso/ (altura*2)

linha_1= f"{nome} tem {altura} de altura"

print(linha_1)
#no caso acima eu usei o comando f para nomear a função nme e altura e elas buscarem
# os valores da função nome e altura. 
# o resultado no print é: hiago Seixas tem 1.8 de altura
# também é possivel formatar a quantidade de casas decimais de um ponto. para isso é 
#é só colocar na função :. ,a qauntidade de casas decimais e o f. no caso abaixo ele 
#mostrou minha altura: 1.800, pq coloquei :.3f. 
# obs:se or um numero alto e quiser colocar vircula é só inserri virgula antes 
# do ponto. 
linha_1= f'{nome} tem {altura:,.3f} de altura'
linha_2= f'pesa {peso:.4f} qulos e seiu imc é'
linha_3= f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)


# NÃO FUNCIONOU. FALAR COM O MARCOS !!!!!!!!!!!!!








