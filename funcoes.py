from datetime import datetime #importa a biblioteca responsavel por inserir data e hora

class Perguntas(): 
    
    respostas = []
    
    def obter_resposta(self):  #método criado para fazer o questionamento das 6 perguntas e registrar data e hora
        self.idade = input('Insira sua idade: ')        
        self.genero = input('Qual é o seu gênero? ')
        
        while True:
            try:                
                print('\n Para responder o questionário utilize : Sim (1), Não (2), Não sei responder (3)?')
                self.p1 = input('\nCompraria um carro pela internet? ')
                self.p2 = input('\nSe o preço do carro fosse 15% abaixo do valor de mercado, você compraria? ')
                self.p3 = input('\nTem intenção de comprar um carro nos próximos 6 meses? ')
                self.p4 = input('\nGostaria do serviço de despachante na compra do seu carro? ')
                if self.p1 and self.p2 and self.p3 and self.p4 < '1' or self.p1 and self.p2 and self.p3 and self.p4 > '3':
                    raise ValueError  #função utilizada para levantar uma exceção explicitamente em seu código
            except ValueError:
                print('Insira um numero entre 1 e 3 ')        
        
    def add_lista(self):
        self.respostas.append([self.idade])
        self.respostas.append([self.genero]) 
        self.respostas.append([self.p1])
        self.respostas.append([self.p2])
        self.respostas.append([self.p3])
        self.respostas.append([self.p4])
        hora_atual = datetime.now() #Registra o horário
        data_e_hora_atual = hora_atual.strftime('%d/%m/%Y %H:%M') #registra a data e implementa o horário da variável 'hora atual'.
        self.respostas.append(data_e_hora_atual)
        print(self.respostas)  #O self é usado para acessar os atributos e métodos da instância dentro da própria classe.
        
    def responder_pesquisa(self): #metodo criado para verificar a entrada do usuario
        while True:
            resposta = self.obter_resposta()
            if resposta == [00]:
                break
            self.respostas.append(resposta)
        print(self.respostas)                  
    
    def save_csv(self): #metodo criado para salvar o arquivo em csv
        return 
    

