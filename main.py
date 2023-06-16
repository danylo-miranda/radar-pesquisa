from funcoes import*
lista2 = []
while True:
    genero_lista =['1','2','3']
    opcoes_validas = ['1','2','3'] #validar a entrada do usuário e garantir que ele digite uma opção válida
    while True:
        idade = input('Qual a idade do candidato? \nOu digite 00 para encerrar o programa: ')
        if idade == '00':
            escreverCsv(lista2)
            print('Programa encerrado.')
            exit()
        elif idade.isdigit() and int(idade) >= 18:
            break
        else:
            print('Idade inválida. Por favor, digite um número válido maior ou igual a 18.')

# Continuar com o restante do programa após obter uma idade válida

    genero = input('Qual o gênero do candidato? Masculino (1), Feminino (2), Outro (3)? ')    
    while genero not in genero_lista:
        genero = input('Opção inválida. Masculino (1), Feminino (2), Outro (3)? ')    
    
    imprimirOpcoes()
    p1 = input('Compraria um carro pela internet? ')
    while p1 not in opcoes_validas:
        p1 = input('Opção inválida. Sim (1), Não (2), Não sei responder (3)? ')

    imprimirOpcoes()
    p2 = input('Se o preço do carro fosse 15% abaixo do valor de mercado, você compraria? ')
    while p2 not in opcoes_validas:
        p2 = input('Opção inválida. Sim (1), Não (2), Não sei responder (3)? ')

    imprimirOpcoes()
    p3 = input('Tem intenção de comprar um carro nos próximos 6 meses? ')
    while p3 not in opcoes_validas:
        p3 = input('Opção inválida. Sim (1), Não (2), Não sei responder (3)? ')

    imprimirOpcoes()
    p4 = input('Gostaria do serviço de despachante na compra do seu carro?')
    while p4 not in opcoes_validas:
        p4 = input('Opção inválida. Sim (1), Não (2), Não sei responder (3)?')
        print('\n')    
    if genero == '1':
        genero = 'Masculino'
    elif genero == '2':
        genero = 'Feminino'
    elif genero == '3':
        genero = 'Outro'                  

    questionario = Perguntas(idade, genero, p1, p2, p3, p4)
    
    dados = questionario.add_lista() 
    
    lista2.append(dados)
    print('\n')
    print("Obrigado por participar da pesquisa!")
    print('\n')
    
