from datetime import datetime #importa a biblioteca responsavel por inserir data e hora

class Perguntas(): 
    def obter_resposta(self):  #método criado para fazer o questionamento das 6 perguntas e registrar data e hora
        self.respostas = []
        idade = input('Insira sua idade: ')        
        genero = input('Qual é o seu gênero? ')
        print('\n Para responder o questionário utilize : Sim (1), Não (2), Não sei responder (3)?')
        p1 = input('\nCompraria um carro pela internet? ')
        p2 = input('\nSe o preço do carro fosse 15% abaixo do valor de mercado, você compraria? ')
        p3 = input('\nTem intenção de comprar um carro nos próximos 6 meses? ')
        p4 = input('\nGostaria do serviço de despachante na compra do seu carro? ')        
        self.respostas.append([idade])
        self.respostas.append([genero]) 
        self.respostas.append([p1])
        self.respostas.append([p2])
        self.respostas.append([p3])
        self.respostas.append([p4])
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
    
questionario = Perguntas()
questionario.obter_resposta()
