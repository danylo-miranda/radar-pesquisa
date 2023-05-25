# from funcoes import*

# idade = input('Digite a idade do entrevistado')

# idade_candidato(idade)


idade_dos_candidatos = []
genero_dos_candidatos = []
pergunta01 = []
pergunta02 = []
pergunta03 = []
pergunta04 = []


        
while True:
    idade_candidato = input('Qual a idade do candidato?')
    idade_dos_candidatos.append(idade_candidato)
    if idade_candidato == '00':
        break
    print('m = masculino e f = feminino')
    genero_candidato = input('Qual o gênero do candidato? ')
    genero_dos_candidatos.append(genero_candidato)
    print('Sim (1), Não (2), Não sei responder (3)?')
    pergunta_01 = input('Compraria um carro pela internet?')
    pergunta01.append(pergunta_01)
    print('Sim (1), Não (2), Não sei responder (3)?')
    pergunta_02 = input('Se o preço do carro fosse 15% abaixo do valor de mercado, você compraria?')
    pergunta02.append(pergunta_02)
    print('Sim (1), Não (2), Não sei responder (3)?')
    pergunta_03 = input('Tem intenção de comprar um carro nos próximos 6 meses?')
    pergunta03.append(pergunta_03)
    print('Sim (1), Não (2), Não sei responder (3)?')
    pergunta_04 = input('Gostaria do serviço de despachante na compra do seu carro?')
    pergunta04.append(pergunta_04)

print(idade_dos_candidatos,
      genero_dos_candidatos,
      pergunta01,
      pergunta02,
      pergunta03,
      pergunta04)

for item1, item2, item3, item4, item5, item6 in zip(idade_dos_candidatos,genero_dos_candidatos,pergunta01,pergunta02,pergunta03,pergunta04):
    print(f'{item1} {item2} {item3} {item4} {item5} {item6}')