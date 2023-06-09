from datetime import datetime #importa a biblioteca responsavel por inserir data e hora
import pandas as pd
import os
import time

class Perguntas(): 

    respostas = []# Lista para armazenar respostas do questionário 

    def __init__(self, idade, genero, p1, p2, p3, p4):  #metódo construtor 
        self.__idade = idade #encapsulamento para proteção do atributo 
        self.__genero = genero       
        self.__p1 = opcoes(p1)
        self.__p2 = opcoes(p2)
        self.__p3 = opcoes(p3)
        self.__p4 = opcoes(p4)               

    def add_lista(self):
        self.respostas = []
        hora_atual = datetime.now() #Registra o horário
        data_e_hora_atual = hora_atual.strftime('%d/%m/%Y %H:%M') #registra a data e implementa o horário da variável 'hora atual'.
        self.respostas.append([self.__idade,self.__genero,self.__p1,self.__p2,self.__p3,self.__p4,data_e_hora_atual])
        return self.respostas #O self é usado para acessar os atributos e métodos da instância dentro da própria classe.

def opcoes(p): #Validação das perguntas do questionário exceto idade 
        if p == '1':
            p = 'Sim'
        elif p == '2':
            p = 'Nao'
        elif p == '3':
            p = 'Nao sei responder'
        return p

def imprimirOpcoes():
    print('*'*30)
    print('Sim (1), Não (2), Não sei responder (3)? ')



def escreverCsv(dados): 
# Verifica se o arquivo CSV já existe
    nome_arquivo = 'dados.csv'
    arquivo_existe = os.path.isfile(nome_arquivo)
    
    # Dados a serem adicionados ao arquivo CSV
    for i in range(len(dados)):
        novos_dados = {'Idade': [dados[i][0][0]], 'Genero': [dados[i][0][1]], 'Pergunta1': [dados[i][0][2]], 'Pergunta2': [dados[i][0][3]], 'Pergunta3': [dados[i][0][4]], 'Pergunta4': [dados[i][0][5]], 'Data/Hora': [dados[i][0][6]]}
    # Se o arquivo já existe, carrega o conteúdo existente
        if arquivo_existe:
            # Carrega o arquivo CSV existente para um DataFrame
            df_existente = pd.read_csv(nome_arquivo)

            # Adiciona os novos dados ao DataFrame existente
            df_novo = pd.DataFrame(novos_dados)
            df_final = pd.concat([df_existente, df_novo], ignore_index=True)

            # Salva o DataFrame atualizado de volta para o arquivo CSV
            df_final.to_csv(nome_arquivo, index=False)
        else:
            # Se o arquivo não existe, cria um novo arquivo CSV com os novos dados
            df_novo = pd.DataFrame(novos_dados)
            df_novo.to_csv(nome_arquivo, index=False)
    print("\nSalvando Pesquisa...\n")        
    time.sleep(1)
    print('Pesquisa salva com sucesso!\n')
            
