from datetime import datetime #importa a biblioteca responsavel por inserir data e hora
import csv
import pandas as pd
import os
import time

class Perguntas(): 
    
    respostas = []
    
    def __init__(self, idade, genero, p1, p2, p3, p4):  #criador
        self.idade = idade        
        self.genero = genero       
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4                  
        
    def add_lista(self):
        self.respostas = []
        self.respostas.append(self.idade)
        self.respostas.append(self.genero) 
        self.respostas.append(self.p1)
        self.respostas.append(self.p2)
        self.respostas.append(self.p3)
        self.respostas.append(self.p4)
        hora_atual = datetime.now() #Registra o horário
        data_e_hora_atual = hora_atual.strftime('%d/%m/%Y %H:%M') #registra a data e implementa o horário da variável 'hora atual'.
        self.respostas.append(data_e_hora_atual)
        return self.respostas
          #O self é usado para acessar os atributos e métodos da instância dentro da própria classe.
        

def escreverCsv(dados): 
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

def opcoes(p):
        if p == '1':
            p = 'Sim'
        elif p == '2':
            p = 'Nao'
        elif p == '3':
            p = 'Nao sei responder'
        return p
