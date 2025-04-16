lista_peixes = []

print("Digite 8 peixes que você gosta de comer na semana santa:")

for i in range(8):
    peixe = input(f"Digite o nome do peixe {i + 1}: ")
    lista_peixes.append(peixe)
    print(peixe, "adicionado com sucesso!")

print("Lista final de peixes:", lista_peixes)

peixe_removido = input("Digite o nome do peixe que deseja remover: ")

if peixe_removido in lista_peixes:
    lista_peixes.remove(peixe_removido)
    print(peixe_removido, "removido com sucesso!")
else:       
    print(peixe_removido, "não encontrado na lista!")

print("Lista atualizada de peixes: ", lista_peixes)