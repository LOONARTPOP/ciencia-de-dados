HT = float(input("Horas trabalhadas no mês: "))
VH = float(input("Valor hora: "))
PD = float(input("Percentual de desconto: "))

salarioBruto = HT * VH #Multiplica o valor da hora trabalhada pelo valor da hora
totalDesconto = PD/100 #Valor da porcentagem do desconto
salarioLiquido = salarioBruto - totalDesconto #subtrai o desconto do salario bruto

print("Valor do salário bruto: ", salarioBruto)
print("Valor do salário líquido: ", salarioLiquido)