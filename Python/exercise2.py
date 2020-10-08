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


def rango_cambiante(n1, n2, n3) -> str:
    aviso = "El número {} {}"

    if n3 < n2:
        return aviso.format(n3, "está por debajo del rango")
    else:
        return en_rango(n1, n3)


def turtles(animalito):
    variantes = ['TORTUGA', 'TORTUGOTA', 'TORTUGUITA']
    if variantes.__contains__(animalito.upper()):
        return 'A mí también me gustan las tortugas'
    else:
        return 'Ese animal es genial, pero prefiero las tortugas'


def clima():
    print("¿Está lloviendo?")
    r: str = input("Respuesta: (si/no) $ ")
    if r.upper() == 'SI' or r.upper() == 'S':
        print("¿Está haciendo mucho viento?")
        r: str = input("Respuesta: (si/no) $ ")
        if r.upper() == 'SI' or r.upper() == 'S':
            print("Está haciendo mucho viento para salir con sombrilla")
        elif r.upper() == 'NO' or r.upper() == 'N':
            print("Recomiendo fuertemente llevar sombrilla al salir")
        else:
            print("Respuesta invalida. Hasta luego!")
    elif r.upper() == 'NO' or r.upper() == 'N':
        print("¡Que tengas un bonito día!")
    else:
        print("Respuesta invalida. Hasta luego!")


def edad_permitida(edad) -> str:
    if edad > 30:
        return "Nunca es tarde para aprender. ¿Qué curso tomaremos?"
    elif 29 >= edad >= 18:
        return "Es un momento excelente para impulsar tu carrera"
    else:
        return "¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte"


def mensajes_opcionales(opc) -> str:
    if opc < 1 or opc > 6:
        return "Por favor, ingrese un número entre 1 y 6"

    msjs = [
        "Hoy aprenderemos sobre prorgamación",
        "¿Qué tal tomar un curso de marketing digital?",
        "Hoy es un gran día para comenzar a aprender de diseño",
        "¿Y si aprendemos algo de negocios online?",
        "Veamos un par de clases sobre producción audiovisual",
        "Tal vez sea bueno desarrollar una habilidad blanda en Platzi"
    ]
    opcion = opc - 1

    return msjs[opcion]


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
        elif num_reto == 4:
            animal: str = input("Ingresar un animal: $ ")
            print(turtles(animal))
        elif num_reto == 5:
            clima()
        elif num_reto == 6:
            edad_usuario: int = int(input("Por favor, ingresa tu edad: $ "))
            print(edad_permitida(edad_usuario))
        elif num_reto == 7:
            numero: int = int(input("Ingrese un número entre 1 y 6: $ "))
            print(mensajes_opcionales(numero))
        else:
            print("Cuak Cuak!")

    except ValueError:
        print("Se ingresó un valor de tipo diferente al esperado")
