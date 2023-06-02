from funcoes import*
import csv
nome_arquivo = 'dados.csv'




def escrever(dados,p1, p2, p3, p4):
    
    try:
        with open(nome_arquivo, 'r') as file:
            reader = csv.reader(file)
            
            primeira_linha = next(reader)
            tem_dados = True
    except StopIteration:
        tem_dados = False
    if  tem_dados == False:
        with open(nome_arquivo, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['idade', 'genero', 'p1', 'p2', 'p3', 'p4', 'data_hora'])
            writer.writerow(dados)
        print(f'Arquivo {nome_arquivo} criado e dados foram escritos.')
    else:
        with open(nome_arquivo, 'a', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow(dados)
while True:
    genero_lista =['1','2','3']
    opcoes_validas = ['1','2','3'] #validar a entrada do usuário e garantir que ele digite uma opção válida
    idade = input('Qual a idade do candidato?')
    
    if idade == '00':
        break
    while idade.isnumeric() == False:
        idade = input('Idade inválida. Qual a idade do candidato?')
    genero = input('Qual o gênero do candidato? Masculino (1), Feminino (2), Outro (3)? ')    
    while genero not in genero_lista:
        genero = input('Opção inválida. Masculino (1), Feminino (2), Outro (3)? ')    
    
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
        p4 = input('Opção inválida. Sim (1), Não (2), Não sei responder (3)?')
        
    questionario = Perguntas(idade, genero, p1, p2, p3, p4)
    dados = questionario.add_lista() 
    #dados_transpostos = list(map(list, zip(*dados)))
    #dados_planos = [item for sublist in dados for item in sublist]
    
    escrever(dados,p1, p2, p3, p4)
     

    
    
    
    


    