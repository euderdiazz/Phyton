#Questão 3m
nome=input("Informe o nome: ")
sexo=input("Informe o sexo (M ou F): ")
if sexo!=("m" or "M") and sexo!=("f" and "F"):
    print("Sexo inválido!")
elif sexo==("m" or "M"):
    print(f"Ilmo. Sr. {nome}")
    print("Ilmo. Sr. %s"%nome)
else:
    print(f"Ilma. Sra. {nome}")
    print("Ilma. Sra. %s"%nome)
