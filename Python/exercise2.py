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


def en_rango(n1, n2) -> str:
    """
    :rtype: str
    """
    # Validaciones
    if type(n1) is not int or type(n2) is not int:
        return "Tipo invalido en alguno de los argumentos"

    # Variables
    frase = "El n�mero {} {}"

    if n2 < n1:
        return frase.format(n2, "se encuentra en el rango, gracias")
    else:
        return frase.format(n2, "excede el l�mite permitido.")


def rango_cambiante(n1, n2, n3) -> str:
    aviso = "El n�mero {} {}"

    if n3 < n2:
        return aviso.format(n3, "est� por debajo del rango")
    else:
        return en_rango(n1, n3)


def turtles(animalito):
    variantes = ['TORTUGA', 'TORTUGOTA', 'TORTUGUITA']
    if variantes.__contains__(animalito.upper()):
        return 'A m� tambi�n me gustan las tortugas'
    else:
        return 'Ese animal es genial, pero prefiero las tortugas'


def clima():
    print("�Est� lloviendo?")
    r: str = input("Respuesta: (si/no) $ ")
    if r.upper() == 'SI' or r.upper() == 'S':
        print("�Est� haciendo mucho viento?")
        r: str = input("Respuesta: (si/no) $ ")
        if r.upper() == 'SI' or r.upper() == 'S':
            print("Est� haciendo mucho viento para salir con sombrilla")
        elif r.upper() == 'NO' or r.upper() == 'N':
            print("Recomiendo fuertemente llevar sombrilla al salir")
        else:
            print("Respuesta invalida. Hasta luego!")
    elif r.upper() == 'NO' or r.upper() == 'N':
        print("�Que tengas un bonito d�a!")
    else:
        print("Respuesta invalida. Hasta luego!")


def edad_permitida(edad) -> str:
    if edad > 30:
        return "Nunca es tarde para aprender. �Qu� curso tomaremos?"
    elif 29 >= edad >= 18:
        return "Es un momento excelente para impulsar tu carrera"
    else:
        return "�Sabes hacia d�nde dirigir tu futuro? Seguro puedo ayudarte"


def mensajes_opcionales(opc) -> str:
    if opc < 1 or opc > 6:
        return "Por favor, ingrese un n�mero entre 1 y 6"

    msjs = [
        "Hoy aprenderemos sobre prorgamaci�n",
        "�Qu� tal tomar un curso de marketing digital?",
        "Hoy es un gran d�a para comenzar a aprender de dise�o",
        "�Y si aprendemos algo de negocios online?",
        "Veamos un par de clases sobre producci�n audiovisual",
        "Tal vez sea bueno desarrollar una habilidad blanda en Platzi"
    ]
    opcion = opc - 1

    return msjs[opcion]


if __name__ == '__main__':
    retos: list = [
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

    try:
        num_reto: int = int(input("Seleccione el reto $ "))
        os.system("clear")
        os.system("cls")

        if num_reto == 1:
            num1: int = int(input("Ingresar primer n�mero: $ "))
            num2: int = int(input("Ingresar segundo n�mero: $ "))
            print(mayor_menor(num1, num2))
        elif num_reto == 2:
            num1: int = int(input("Ingresar primer n�mero: $ "))
            num2: int = int(input("Ingresar segundo n�mero: $ "))
            print(en_rango(num1, num2))
        elif num_reto == 3:
            num1: int = int(input("Ingresar n�mero como limite superior: $ "))
            num2: int = int(input("Ingresar n�mero como l�mite inferior: $ "))
            num3: int = int(input("Ingresar n�mero a comparar: $ "))
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
            numero: int = int(input("Ingrese un n�mero entre 1 y 6: $ "))
            print(mensajes_opcionales(numero))
        else:
            print("Cuak Cuak!")

    except ValueError:
        print("Se ingres� un valor de tipo diferente al esperado")
