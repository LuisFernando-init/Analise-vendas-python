import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('imagens', exist_ok=True)


# Carregar os dados
df = pd.read_csv('dados/SuperMarket Analysis.csv')

# Visualizar as primeiras linhas
print(df.head())

# Informações gerais
print("\nInformações da base:")
print(df.info())

# Estatísticas descritivas
print("\nEstatísticas:")
print(df.describe())

faturamento = df.groupby('Product line')['Sales'].sum()

print("\nFaturamento por categoria:")
print(faturamento.sort_values(ascending=False))

cidade_vendas = df.groupby('City')['Sales'].sum()

print("\nFaturamento por cidade:")
print(cidade_vendas.sort_values(ascending=False))

pagamentos = df['Payment'].value_counts()

print("\nFormas de pagamento:")
print(pagamentos)

faturamento = faturamento.sort_values()

plt.figure(figsize=(10,6))
faturamento.plot(kind='barh')

plt.title('Faturamento por Linha de Produto', fontsize=16)
plt.xlabel('Faturamento (US$)', fontsize=12)
plt.ylabel('Linha de Produto', fontsize=12)

plt.tight_layout()
plt.savefig('imagens/faturamento_categoria.png')
plt.show()

ax = faturamento.plot(kind='barh', figsize=(10,6))

for i, valor in enumerate(faturamento):
    ax.text(valor + 500, i, f'{valor:,.0f}')

plt.title('Faturamento por Linha de Produto')
plt.xlabel('Faturamento (US$)')
plt.tight_layout()
plt.show()

cidade_vendas = cidade_vendas.sort_values(ascending=False)

ax = cidade_vendas.plot(
    kind='bar',
    figsize=(8,6)
)

plt.title('Faturamento por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Faturamento (US$)')
plt.xticks(rotation=0)

for i, valor in enumerate(cidade_vendas):
    ax.text(i, valor + 1000, f'{valor:,.0f}', ha='center')

plt.tight_layout()
plt.savefig('imagens/faturamento_cidade.png')
plt.show()

pagamentos = df['Payment'].value_counts()

ax = pagamentos.plot(
    kind='pie',
    autopct='%1.1f%%',
    figsize=(8,8)
)

plt.title('Distribuição dos Métodos de Pagamento')
plt.ylabel('')

plt.tight_layout()
plt.savefig('imagens/metodos_pagamento.png')
plt.show()