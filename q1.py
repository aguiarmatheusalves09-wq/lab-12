lista = ["Rato", "Cavalo", "Largatixa", "Macaco", "Gato"]
try:
    resposta = int(input("Digite um indice da lista: "))
    print(lista[resposta])
except IndexError:
    print("A lista tem só 5 elemento")
