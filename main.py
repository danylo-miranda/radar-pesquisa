from funcoes import*

while True:
    
    idade = input('Qual a idade do candidato?')
    if idade == '00':
        break
    genero = input('Qual o gênero do candidato? ')    
    
    print('Sim (1), Não (2), Não sei responder (3)?')    
    p1 = input('Compraria um carro pela internet?')           
    print('Sim (1), Não (2), Não sei responder (3)?')
    p2 = input('Se o preço do carro fosse 15% abaixo do valor de mercado, você compraria?')    
    print('Sim (1), Não (2), Não sei responder (3)?')
    p3 = input('Tem intenção de comprar um carro nos próximos 6 meses?')    
    print('Sim (1), Não (2), Não sei responder (3)?')
    p4 = input('Gostaria do serviço de despachante na compra do seu carro?')
    questionario = Perguntas(idade, genero, p1, p2, p3, p4)
    questionario.add_lista()   

    
        
