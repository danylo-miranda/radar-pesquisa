from funcoes import*
import csv
import pandas as pd
import os
import time

def escrever(dados): 
# Verifica se o arquivo CSV já existe
    nome_arquivo = 'dados.csv'
    arquivo_existe = os.path.isfile(nome_arquivo)
    
    # Dados a serem adicionados ao arquivo CSV
    novos_dados = {'Idade': [dados[0]], 'Genero': [dados[1]], 'Pergunta1': [dados[2]], 'Pergunta2': [dados[3]], 'Pergunta3': [dados[4]], 'Pergunta4': [dados[5]], 'Data/Hora': [dados[6]]}

    # Se o arquivo já existe, carrega o conteúdo existente
    if arquivo_existe:
        # Carrega o arquivo CSV existente para um DataFrame
        df_existente = pd.read_csv(nome_arquivo)

        # Adiciona os novos dados ao DataFrame existente
        df_novo = pd.DataFrame(novos_dados)
        df_final = pd.concat([df_existente, df_novo], ignore_index=True)

        # Salva o DataFrame atualizado de volta para o arquivo CSV
        df_final.to_csv(nome_arquivo, index=False)
        print("\nSalvando Pesquisa...")
        time.sleep(1)

    else:
        # Se o arquivo não existe, cria um novo arquivo CSV com os novos dados
        df_novo = pd.DataFrame(novos_dados)
        df_novo.to_csv(nome_arquivo, index=False)
        print("\nSalvando Pesquisa...")
        time.sleep(1)




while True:
    genero_lista =['1','2','3']
    opcoes_validas = ['1','2','3'] #validar a entrada do usuário e garantir que ele digite uma opção válida
    while True:
        idade = input('Qual a idade do candidato? ')
        if idade == '00':
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
    
    if genero == '1':
        genero = 'Masculino'
    elif genero == '2':
        genero = 'Feminino'
    elif genero == '3':
        genero = 'Outro'                  
    
    def opcoes(p):
        if p == '1':
            p = 'Sim'
        elif p == '2':
            p = 'Nao'
        elif p == '3':
            p = 'Nao sei responder'
        return p
    
    
    p1 = opcoes(p1)
    p2 = opcoes(p2)
    p3 = opcoes(p3)
    p4 = opcoes(p4)  
    
    questionario = Perguntas(idade, genero, p1, p2, p3, p4)
    
    dados = questionario.add_lista() 
    print(dados)
    escrever(dados)


    
    
    
    


    