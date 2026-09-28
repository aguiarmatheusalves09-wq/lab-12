def somar_valores(a, b):
    return a + b

try:
    a = input("Digite um numero: ")
    b = int(input("Digite outro numero: "))
    print(somar_valores(a, b))
except TypeError as tipo:
    print("Os valores não são compativeis")
    print(type(tipo))