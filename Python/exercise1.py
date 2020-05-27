# -*- encoding: iso-8859-1 -*-
import os


def say_hello(name, last_name=""):
    print(f"Hola, {name} {last_name}")


def print_categories():
    print("Platzi cuenta con cursos de:")
    for categoria in [
        "Desarrollo e ingenieria", "Crecimiento Profesional",
        "Negocios y emprendimiento", "Diseño y UX",
        "Marketing", "Produccion Audiovisual"
    ]:
        print(categoria)


def sumar(n1, n2):
    res = float(n1) + float(n2)
    res = round(res, 2)
    print(f"{n1} + {n2} = {res}")


def suma_multiplica(n1, n2, n3):
    print(f"Datos de entrada: {n1}, {n2}, {n3}")
    resultado = (float(n1) + float(n2)) * float(n3)
    print(f"Resultado: {round(resultado, 2)}")


def explicar_pizza(rebanadas, consumidas):
    quedan = float(rebanadas) - float(consumidas)
    if quedan < 0:
        print(f"De las {rebanadas} rebanadas de pizza que trajeron, todas se consumieron! Ya no queda nada.")
    else:
        print(f"De las {rebanadas} rebanadas de pizza que trajeron, se comieron {consumidas}."
              f" Ahora quedan {quedan}. Provecho!")


def edades(name, age):
    print(f"Hola, {name}! Veo que el año pasado tenías {age - 1}"
          f" años y seguro el próximo año cumplirás {age + 1} años.")


def divide_cuenta():
    total_pagar = input("Ingresa el total a pagar: $ ")
    propina = input("Ahora, ingresa el porcentaje de propina (%): $ ")
    impuesto = input("¿Y el impuesto? (%) $ ")
    personas = input("¿Cuantas personas son ustedes? $ ")
    total = float(total_pagar) + (float(total_pagar) * (float(propina) / 100)) + \
        (float(total_pagar) * (float(impuesto) / 100))
    print(f"El total a pagar con impuestos y propina es: Q.{total}")
    print(f"Cada uno debe pagar: Q.{round(float(total) / float(personas), 2)}")


def calcula_tiempo(days):
    days = float(days)
    horas = days * 24
    minutos = horas * 60
    segundos = minutos * 60
    print(
        f"En {days} días, hay:"
        f"\n    {horas} horas;"
        f"\n    {minutos} minutos;"
        f"\n    {segundos} segundos"
    )


def convertir_kms(miles):
    factor = 1.609344  # km
    km = float(miles) * factor
    km = round(km, 2)
    print(f"Interesante... En {miles}mi, hay {km}Km")


def numero_en_otro(num_me_100, num_ma_1000):
    veces = num_ma_1000 // num_me_100
    print(f"En el número {num_ma_1000} hay aproximádamente {veces} veces el número {num_me_100}.")


if __name__ == "__main__":

    retos = [
        "1. Hola Mundo", 
        "2. Hola nombre y apellido",
        "3. Mensaje multilínea",
        "4. Suma de enteros",
        "5. Suma y multiplicacion",
        "6. Resta de pizzas",
        "7. Edad futura y pasada",
        "8. Divide la cuenta",
        "9. Calculando días",
        "10. Conversor de millas",
        "11. Cuantas veces un numero en otro"
        ]

    for reto in retos:
        print(reto)

    num_reto = input("Seleccione el reto $ ")
    num_reto = int(num_reto)
    os.system("clear")

    if num_reto == 1:
        nombre = input("Ingrese el nombre: $ ")
        say_hello(nombre)

    elif num_reto == 2:
        nombre = input("Ingrese el nombre: $ ")
        apellido = input("Ingrese el apellido: $ ")
        say_hello(nombre, apellido)

    elif num_reto == 3:
        print_categories()

    elif num_reto == 4:
        num1 = input("Ingrese numero 1: $ ")
        num2 = input("Ingrese numero 2: $ ")
        sumar(num1, num2)

    elif num_reto == 5:
        num1 = input("Ingrese numero 1: $ ")
        num2 = input("Ingrese numero 2: $ ")
        num3 = input("Ingrese numero 3: $ ")
        suma_multiplica(num1, num2, num3)

    elif num_reto == 6:
        rebanadas_pizza = input("Ingrese las rebanadas de pizza: $ ")
        rebanadas_consumidas = 5
        explicar_pizza(rebanadas_pizza, rebanadas_consumidas)
   
    elif num_reto == 7:
        nombre = input("Ingresa tu nombre: $ ")
        edad = float(input("Ingresa tu edad: $ "))
        edades(nombre, edad)

    elif num_reto == 8:
        divide_cuenta()

    elif num_reto == 9:
        dias = input("Ingresa la cantidad de días: $ ")
        calcula_tiempo(dias)

    elif num_reto == 10:
        millas = input("Ingresa los Kilómetros a convertir: $ ")
        convertir_kms(millas)

    elif num_reto == 11:
        num1 = float(input("Ingresa un número menor a 100: $ "))
        if num1 > 100:
            print("Número no válido. Ingresa un número MENOR A 100 por favor.")
            exit(1)
        
        num2 = float(input("Ingresa un número mayor a 1000: $ "))
        if num2 < 1000:
            print("Número no válido. Ingresa un número MAYOR A 1000 por favor.")
            exit(1)
        numero_en_otro(num1, num2)

    else:
        print("Cuak!")
