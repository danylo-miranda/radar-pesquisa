from funcoes import*

while True:
    opcoes_validas = ['1','2','3'] #validar a entrada do usuário e garantir que ele digite uma opção válida
    idade = input('Qual a idade do candidato?')
    if idade == '00':
        break
    genero = input('Qual o gênero do candidato? ')    
    
    print('*'*30)
    print('Sim (1), Não (2), Não sei responder (3)? ')
    p1 = input('Compraria um carro pela internet? ')
    while p1 not in opcoes_validas:
        p1 = input('Opção inválida. Sim (1), Não (2), Não sei responder (3)? ')

    print('*'*30)
    print('Sim (1), Não (2), Não sei responder (3)? ')
    p2 = input('Se o preço do carro fosse 15% abaixo do valor de mercado, você compraria? ')
    while p2 not in opcoes_validas:
        p2 = input('Opção inválida. Sim (1), Não (2), Não sei responder (3)? ')

    print('*'*30)
    print('Sim (1), Não (2), Não sei responder (3)? ')
    p3 = input('Tem intenção de comprar um carro nos próximos 6 meses? ')
    while p3 not in opcoes_validas:
        p3 = input('Opção inválida. Sim (1), Não (2), Não sei responder (3)? ')

    print('*'*30)
    print('Sim (1), Não (2), Não sei responder (3)? ')
    p4 = input('Gostaria do serviço de despachante na compra do seu carro?')
    while p4 not in opcoes_validas:
        p4 = input('Opção inválida. Sim (1), Não (2), Não sei responder (3)? ')
        
    questionario = Perguntas(idade, genero, p1, p2, p3, p4)
    questionario.add_lista()
    questionario.save_csv('Dados da Pesquisa')#parametro posicionado com o nome do arquivo a ser salvo   
    
    
        
