import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('planilha-pronta.xlsx')

df = data['Ano de Lançamento'].value_counts().reset_index()
df.columns = ['Ano', 'Quantidade']

df = df.sort_values(by='Ano')

df['Frequência Relativa (%)'] = (
    df['Quantidade'] / df['Quantidade'].sum() * 100
).round(2)

print('\n Tabela de Frequência: Ano de Lançamento')
print(df.to_markdown(index=False))
df.to_excel('freq-table.xlsx', index=False)

anos = df['Ano'].astype(str)
quantidades = df['Quantidade']

# colunas
plt.figure(figsize=(12, 6))
plt.bar(anos, quantidades, color='skyblue')
plt.title('Filmes Lançados por Ano (Gráfico de Colunas)')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_colunas.png')
plt.show()

# barras
plt.figure(figsize=(10, 8))
plt.barh(anos, quantidades, color='lightgreen')
plt.title('Filmes Lançados por Ano (Gráfico de Barras)')
plt.xlabel('Quantidade')
plt.ylabel('Ano de Lançamento')
plt.tight_layout()
plt.savefig('grafico_barras.png')
plt.show()

# setores
plt.figure(figsize=(10, 10))
plt.pie(quantidades, labels=anos, autopct='%1.1f%%', startangle=90)
plt.title('Proporção de Filmes Lançados por Ano (Gráfico de Setores)')
plt.tight_layout()
plt.savefig('grafico_setores.png')
plt.show()
