# import pandas as pd
# import matplotlib.pyplot as plt

# # Ler o arquivo CSV e criar o DataFrame
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

# Definir as faixas etárias
faixas = [18, 30, 45, 100]  # Exemplo de faixas: 18-30, 30-45, 45+

# Definir os rótulos das faixas etárias
rotulos = ['18-30', '30-45', '45+']

# Agrupar as idades em faixas
df['Faixa Etária'] = pd.cut(df['Idade'], bins=faixas, labels=rotulos, right=False)

# Calcular as porcentagens de cada resposta em relação ao total de respostas para cada faixa etária
porcentagens = df.groupby('Faixa Etária')[pergunta].value_counts(normalize=True) * 100
porcentagens = porcentagens.unstack().fillna(0)

# Criar o gráfico de barras
ax = porcentagens.plot(kind='bar', stacked=True)

# Adicionar as porcentagens nas barras
for container in ax.containers:
    for bar in container:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(1, 3),
                    textcoords="offset points", ha='center', va='bottom')

# Definir os rótulos dos eixos
plt.xlabel('Faixa Etária')
plt.ylabel('Porcentagem')

# Definir o título do gráfico
plt.title(f'Relação entre Faixa Etária e Resposta para {pergunta}')

# Exibir o gráfico
plt.show()
