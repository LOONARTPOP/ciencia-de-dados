import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

 # importando os dados
df = pd.read_csv('Faixa Etária do Declarante e Gênero.csv', delimiter=';')

# gerando gráfico com barras
plt.figure(figsize=(15, 9))
sns.barplot(data=df, x='Faixa Etária', y='Quantidade de Declarantes', hue='Gênero')

plt.ylim(0, 5000000) #limite do eixo y em 5 milhões
plt.title('Quantidade de Contribuintes do IRPF por Faixa Etária e Gênero') #definindo o título
plt.ylabel('Declarantes (milhões)') #gerando o eixo y e dando nome
plt.xlabel('Faixa Etária\n Fonte de dados: https://dados.gov.br/dados/conjuntos-dados/grandes-nmeros-do-imposto-de-renda-da-pessoa-fsica') #gerando o eixo x e dando nome
plt.legend(title='Gênero') #gera o titulo da legenda
plt.savefig("graf.jpeg")
plt.show()
