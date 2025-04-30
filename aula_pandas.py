import pandas as pd

vendas_df = pd.read_csv("Contoso - Vendas - 2017.csv", delimiter=";")
clientes_df = pd.read_csv("Contoso - Clientes.csv", delimiter=";", encoding='latin-1')
promocoes_df = pd.read_csv("Contoso - Promocoes.csv", sep=';', encoding='latin-1')
lojas_df = pd.read_csv("Contoso - Lojas.csv", sep=';', encoding='latin-1')
produtos_df = pd.read_csv("Contoso - Cadastro Produtos.csv", sep=';', encoding='latin-1')

#encoding='latin-1'
# clientes_df.rename({"ÿID Cliente" : "ID Cliente"})
novo_df = vendas_df.merge(clientes_df, on="ID Cliente")

print(novo_df)

# print(vendas_df.info())
# print(clientes_df.info())
# print(promocoes_df.info())
# print(lojas_df.info())
# print(produtos_df.info())


