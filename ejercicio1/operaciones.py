def suma(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: Tipo de dato no valido")


def resta(a, b):
    try:
        return a - b
    except TypeError:
        print("Error: Tipo de dato no valido")


def multiplicacion(a, b):
    try:
        return a * b
    except TypeError:
        print("Error: Tipo de dato no valido")


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")