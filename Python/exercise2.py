# -*- encoding: iso-8859-1 -*-
import os


def mayor_menor(n1, n2) -> str:
    """
    :rtype: str
    """
    # Validaciones
    if type(n1) is not int or type(n2) is not int:
        return "Tipo invalido en alguno de los argumentos"

    # Variables
    frase = "El número (M) es mayor que (m) por (r)."

    # Proceso
    if n1 > n2:
        return frase.replace('(M)', str(n1)).replace('(m)', str(n2)).replace('(r)', str(n1 - n2))
    elif n2 > n1:
        return frase.replace('(M)', str(n2)).replace('(m)', str(n1)).replace('(r)', str(n2 - n1))
    else:
        return "Los números son iguales"


def en_rango(n1, n2) -> str:
    """
    :rtype: str
    """
    # Validaciones
    if type(n1) is not int or type(n2) is not int:
        return "Tipo invalido en alguno de los argumentos"

    # Variables
    frase = "El número {} {}"

    if n2 < n1:
        return frase.format(n2, "se encuentra en el rango, gracias")
    else:
        return frase.format(n2, "excede el límite permitido.")


def rango_cambiante(n1, n2, n3):
    aviso = "El número {} {}"

    if n3 < n2:
        return aviso.format(n3, "está por debajo del rango")
    else:
        return en_rango(n1, n3)


if __name__ == '__main__':
    retos: list = [
        "1. Número Mayor y menor",
        "2. En el rango, por favor",
        "3. Rangos cambiantes.",
        "4. 'I like turtles'",
        "5. ¿Cómo está el clima?",
        "6. Edad permitida",
        "7. Mensajes opcionales"
    ]
    for reto in retos:
        print(reto)

    try:
        num_reto: int = int(input("Seleccione el reto $ "))
        os.system("clear")
        os.system("cls")

        if num_reto == 1:
            num1: int = int(input("Ingresar primer número: $ "))
            num2: int = int(input("Ingresar segundo número: $ "))
            print(mayor_menor(num1, num2))
        elif num_reto == 2:
            num1: int = int(input("Ingresar primer número: $ "))
            num2: int = int(input("Ingresar segundo número: $ "))
            print(en_rango(num1, num2))
        elif num_reto == 3:
            num1: int = int(input("Ingresar número como limite superior: $ "))
            num2: int = int(input("Ingresar número como límite inferior: $ "))
            num3: int = int(input("Ingresar número a comparar: $ "))
            print(rango_cambiante(num1, num2, num3))
        else:
            print("Cuak Cuak!")

    except ValueError:
        print("Se ingresó un valor de tipo diferente al esperado")
