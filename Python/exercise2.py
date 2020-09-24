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
    frase = "El n�mero (M) es mayor que (m) por (r)."

    # Proceso
    if n1 > n2:
        return frase.replace('(M)', str(n1)).replace('(m)', str(n2)).replace('(r)', str(n1 - n2))
    elif n2 > n1:
        return frase.replace('(M)', str(n2)).replace('(m)', str(n1)).replace('(r)', str(n2 - n1))
    else:
        return "Los n�meros son iguales"


if __name__ == '__main__':
    retos = [
        "1. N�mero Mayor y menor",
        "2. En el rango, por favor",
        "3. Rangos cambiantes.",
        "4. 'I like turtles'",
        "5. �C�mo est� el clima?",
        "6. Edad permitida",
        "7. Mensajes opcionales"
    ]

    for reto in retos:
        print(reto)

    num_reto = input("Seleccione el reto $ ")
    num_reto = int(num_reto)
    os.system("clear")
    os.system("cls")

    if num_reto == 1:
        num1: int = int(input("Ingresar primer n�mero: $ "))
        num2: int = int(input("Ingresar segundo n�mero: $ "))
        print(mayor_menor(num1, num2))