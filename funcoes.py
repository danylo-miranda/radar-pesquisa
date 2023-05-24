def idade_candidato(idade_candidato):
    idade_dos_candidatos = [] #Lista para receber a idade dos candidatos 
    idade_candidato = input('Digite a idade do entrevistado')
    while idade_candidato.isnumeric()==False or int(idade_candidato) > 00:
        idade_candidato = input('Digite a idade do entrevistado')
        idade_dos_candidatos.append(idade_candidato)
        if idade_candidato.isnumeric == 00:
            print(idade_dos_candidatos)
            break
        
        
    