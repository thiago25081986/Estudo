"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""



variavel_nome = input("Digite seu nome: ")
variavel_idade = input(' Digite sua idade: ')

if variavel_nome and variavel_idade:
    print (f'Seu nome é: {variavel_nome}')

    nome_invertido = variavel_nome [ : : -1]

    print ('Seu nome invertido é:', nome_invertido)

    if ' ' in variavel_nome:  # esse comando eu não lembrava, procurei nas aulas e não achei. Comando '' para buscar espaço na string
        print('Seu nome contèm espaços')

    else:
        print('Seu nome não contem espaços')


    print ('Seu nome tem:', len(variavel_nome), 'letras') # poderia ter usado fstring. Ficaria:
    # print(f' Seu nome tem: {len(variavel)})

    print (f'A primeira letra do seu nome é:{variavel_nome[0]}')

    print ('A ultima letra do seu nome é:', variavel_nome[-1])

else:
    print('Desculpe, você deixou campos vazios')