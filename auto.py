from funcoes import*
import csv
#import pandas as pd
import os
import random
import time


genero_lista = ['1', '2', '3']
opcoes_validas = ['1', '2', '3']

def escrever(dados): 
# Verifica se o arquivo CSV já existe
    nome_arquivo = 'dados.csv'
    arquivo_existe = os.path.isfile(nome_arquivo)

    # Dados a serem adicionados ao arquivo CSV
    novos_dados = {'Idade': [dados[0][0]], 'Genero': [dados[0][1]], 'Pergunta1': [dados[0][2]], 'Pergunta2': [dados[0][3]], 'Pergunta3': [dados[0][4]], 'Pergunta4': [dados[0][5]], 'Data/Hora': [dados[0][6]]}

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
        print('Pesquisa salva com sucesso!\n')
        
    else:
        # Se o arquivo não existe, cria um novo arquivo CSV com os novos dados
        df_novo = pd.DataFrame(novos_dados)
        df_novo.to_csv(nome_arquivo, index=False)
        print("\nSalvando Pesquisa...")
        time.sleep(1)
        print('Pesquisa salva com sucesso!\n')
        
for i in range(5):
    idade = random.randint(18, 60)
    genero = random.choice(genero_lista)
    p1 = random.choice(opcoes_validas)
    p2 = random.choice(opcoes_validas)
    p3 = random.choice(opcoes_validas)
    p4 = random.choice(opcoes_validas)

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
            p = 'Não'
        elif p == '3':
            p = 'Não sei responder'
        return p


    # Aqui você pode chamar a função 'escrever(dados)' para salvar as respostas no arquivo CSV
    questionario = Perguntas(idade, genero, p1, p2, p3, p4)

    dados = questionario.add_lista() 
    print(dados)
    escrever(dados)
    
