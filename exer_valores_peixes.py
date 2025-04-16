lista_peixes_valores = []

print("Digite 8 peixes que você gosta de comer na semana santa:")

for i in range(3):
    peixe = input(f"Digite o nome do peixe {i + 1}: ")
    valor = float(input(f"Digite o valor do peixe {peixe}: "))
    lista_peixes_valores.append((peixe, valor))
    print(peixe, "adicionado com sucesso!")

print("Peixes com seu valor: ", lista_peixes_valores)
print("O peixe com maior valor: ", max(lista_peixes_valores))
print("O peixe com menor valor: ", min(lista_peixes_valores))
print("Ultimo valor da lista:", lista_peixes_valores[2])