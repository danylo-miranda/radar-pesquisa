import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV e criar o DataFrame
pergunta = 'Pergunta1'
nome_arquivo = 'dados.csv'
df = pd.read_csv(nome_arquivo)
df = pd.DataFrame(df)

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












