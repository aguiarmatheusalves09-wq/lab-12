def converter_e_dividir(valor, divisor):
    return float(valor) / divisor

try:
    valor = input("Insira um numero: ")
    divisor = int(input("Insira o divisor: "))
    print(converter_e_dividir(valor, divisor))
except ValueError:
    print("Esse valor não consegue ser convertido para numero")
except ZeroDivisionError:
    print("Zero não consegue dividir")