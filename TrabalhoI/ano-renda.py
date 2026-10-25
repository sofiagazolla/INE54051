import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('dataset_final.xlsx')

eixo_x = data['Público acumulado']
eixo_y = data['Renda (R$) acumulada']

plt.scatter(eixo_x, eixo_y, color='orange', alpha=0.5)

plt.title('Relação entre Duração e Renda dos Filmes')
plt.xlabel('Duração (Minutos)')
plt.ylabel('Renda (Bilheteira)')

plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
