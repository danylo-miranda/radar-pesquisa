from funcoes import*
import random



genero_lista = ['1', '2', '3']
opcoes_validas = ['1', '2', '3']
lista2 = []

    
for i in range(5):#DETERMINA A QUANTIDADE DE PESQUISAS QUE SERÃO FEITAS DE MANEIRA AUTOMATICA E ALEATÓRIA
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
    
    lista2.append(dados)
    print('\n')
    print("Obrigado por participar da pesquisa!")
    print('\n')
escreverCsv(lista2)   
