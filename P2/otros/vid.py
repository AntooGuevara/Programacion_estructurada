def saludar(n):
    if n == 0:
        return
    print("Hola")
    saludar(n - 1)


def factorial(n):
    if n == 0 or n == 1:
        return 1  # caso base
    else:
        return n * factorial(n - 1)  # llamada recursiva


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])


def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)
