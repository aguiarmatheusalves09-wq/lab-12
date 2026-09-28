def verificar_idade(idade):
    
    if idade < 0: raise ValueError("Idade nãi pode ser negativa")
    elif 0 < idade < 18: raise ValueError("Idade mínima para tirar carteira é 18 anos")
    elif idade >= 18: print("Idade válida para tirar carteira")
    
idade = int(input("Digite sua idade: "))
print(verificar_idade(idade))