from datetime import datetime #importa a biblioteca responsavel por inserir data e hora.
import csv #importa a biblioteca CSV

class Perguntas(): 
    
    respostas = []
    
    def __init__(self, idade, genero, p1, p2, p3, p4):  #metodo construtor da lista de perguntas.
        self.idade = idade        
        self.genero = genero       
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4                       
        
    def add_lista(self): #metodo que adiciona os dados da pesquisa na lista resposta.
        self.respostas.append({'Idade' : self.idade})
        self.respostas.append({'Genero' : self.genero}) 
        self.respostas.append({'Pergunta 1' : self.p1}) #adiciona os dados como chaves para uma melhor visualização.
        self.respostas.append({'Pergunta 2' : self.p2})
        self.respostas.append({'Pergunta 3' : self.p3})
        self.respostas.append({'Pergunta 4' : self.p4})
        hora_atual = datetime.now() #Registra o horário
        data_e_hora_atual = hora_atual.strftime('%d/%m/%Y %H:%M') #registra a data e implementa o horário da variável 'hora atual'.
        self.respostas.append({'DATA E HORA' : data_e_hora_atual})
        print(self.respostas)  #O self é usado para acessar os atributos e métodos da instância dentro da própria classe.
    
    def save_csv(self,nome_arquivo): #metodo que salva o arquivo em .csv/ abre o arquivo CSV no modo de escrita.
        with open(f'{nome_arquivo}.csv', 'w', newline='') as arquivo_csv:#parâmetro newline='' para que não haja linhas em branco no arquivo.  
            escrever_csv = csv.writer(arquivo_csv) #cria um objeto que irá escrever no arquivo CSV. 
            escrever_csv.writerow(['Respostas']) #cabeçalho da tabela utilizando o método writerow.
            for dados in self.respostas: #percorrer a lista respostas e escreve cada um dos elementos no arquivo CSV.
                escrever_csv.writerow([dados])
        print(f'Arquivo *{nome_arquivo}* criado e os dados foram escritos.')
        
    
    

