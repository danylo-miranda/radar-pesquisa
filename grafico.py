# import pandas as pd
# import matplotlib.pyplot as plt

# # Ler o arquivo CSV e criar o dfFrame
# pergunta = 'Pergunta1'
# nome_arquivo = 'dados.csv'
# df = pd.read_csv(nome_arquivo)

# # Definir as faixas etárias
# faixas = [18, 30, 45, 100]  # Exemplo de faixas: 18-30, 30-45, 45+

# # Definir os rótulos das faixas etárias
# rotulos = ['18-30', '30-45', '45+']

# # Agrupar as idades em faixas
# df['Faixa Etária'] = pd.cut(df['Idade'], bins=faixas, labels=rotulos, right=False)

# # Calcular as porcentagens de "Sim" e "Não" para cada faixa etária
# porcentagens = df.groupby('Faixa Etária')[pergunta].value_counts(normalize=True) * 100
# porcentagens = porcentagens.unstack().fillna(0)

# # Criar o gráfico de barras
# ax = porcentagens.plot(kind='bar', stacked=True)

# # Adicionar as porcentagens nas barras
# for container in ax.containers:
#     ax.bar_label(container, fmt='%.1f%%', label_type='edge')

# # Definir os rótulos dos eixos
# plt.xlabel('Faixa Etária')
# plt.ylabel('Porcentagem')

# # Definir o título do gráfico
# plt.title(f'Relação entre Faixa Etária e Resposta para {pergunta}')

# # Exibir o gráfico
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV e criar o DataFrame
pergunta = 'Pergunta1'
nome_arquivo = 'dados.csv'
df = pd.read_csv(nome_arquivo)
df = pd.DataFrame(df)

# Agrupando as respostas da pergunta 1 em duas categorias
# df['Resposta'] = df['Pergunta1'].apply(lambda x: 'Sim' if x == 'Sim' else 'Não')

# # Agrupando as respostas da pergunta 1 por faixa etária
# counts = df.groupby('Idade')['Pergunta1'].value_counts().unstack()

# # Plotando o gráfico de barras
# counts.plot(kind='bar', stacked=True)

# # Adicionando rótulos e título ao gráfico
# plt.xlabel('Idade')
# plt.ylabel('Contagem')
# plt.title('Distribuição das Respostas à Pergunta 1 por Faixa Etária')

# # Exibindo o gráfico
# plt.show()


faixas_etarias = ['18-30', '30-40', '40-50', '50-60']

# Criar coluna de faixas etárias
df['Faixa Etária'] = pd.cut(df['Idade'], bins=[18, 30, 40, 50, 60], labels=faixas_etarias)

# Contar as respostas por faixa etária e pergunta1
counts = df.groupby(['Faixa Etária', 'Pergunta1']).size().unstack(fill_value=0)

# Plotar o gráfico de barras
counts.plot(kind='bar', stacked=True)

# Personalizar o gráfico
plt.xlabel('Faixa Etária')
plt.ylabel('Quantidade')
plt.title('Respostas por Faixa Etária')
plt.legend(title='Pergunta 1')

# Mostrar o gráfico
plt.show()












