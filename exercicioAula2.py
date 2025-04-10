maria = float(input("Digite a altura de Maria: "))
juana = float(input("Digite a altura de Juana: "))
pedro = float(input("Digite a altura de Pedro: "))

media  = (maria + juana + pedro)/3
media2 = (float(maria + juana + pedro)).mean()
print("a média entre as alturas de Maria, Juana e Pedro é de: " +str(media))
print(media2)