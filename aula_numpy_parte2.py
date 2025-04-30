import numpy as np

#Geração de numeros inteiros aleatorios
#Os parametros sao: valor mais baixo, valor mais alto e quantidade
#Guardar no array

array_qualquer = np.array(np.random.randint(4,10,10))
print(array_qualquer)

#Gerando uma matriz BI-Dimensional (2D)
print("--- Gerando Matrizes ---")
matriz_inteiros = np.array(np.random.randint(0, 2, size = (2,2)))
print(matriz_inteiros)

#verificando se um array contem valores vazios
print(np.isnan(array_qualquer))

#Conta os valores unicos e suas repetições
# valores_unicos, contagens = np.unique(array_exercicio)
# for valor, cont in zip(valores_unicos, contagens)
#     print(f"Valor {valor} - contagem: {cont}")