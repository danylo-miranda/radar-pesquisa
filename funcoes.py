from datetime import datetime #importa a biblioteca responsavel por inserir data e hora

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
        
    

# Nome do arquivo CSV
