import random
dinero = 1000
nextRound = False
betsArray = []

while True:
    if nextRound:
        print('######## Nueva ronda de apuestas ########')
        print("Usted tiene ", dinero,  "para usar.")

    else:
        print("##################  Bienvenido a la Ruleta  #####################")
        print("Usted tiene", dinero, "para usar.")

    opcion = input(
        "A qué desea apostar?\n1. Par o Impar\n2. Columnas\n3. Número\n4. Color\n"
    )

    while opcion.isdigit() == False or 1 > int(opcion) or int(opcion) > 4:

        print("Ha ingresado mal, intente nuevamente")

        opcion = input(
            "A qué desea apostar?\n1. Par o Impar\n2. Columnas\n3. Número\n4. Color\n"
        )

    opcion = int(opcion)

    apuesta = 0
    # En este código se utiliza la variable apuesta para guardar el monto que el usuario quiere apostar.
    # Se pregunta al usuario si quiere apostar a par o impar utilizando la variable par_impar,
    # y se muestra el dinero que tiene disponible para apostar (dinero_disponible)
    # y se le pregunta cuánto de eso quiere apostar.

    # opcion 1 PAR O IMPAR
    if opcion == 1:

        print("Desea apostar a Par o Impar?")
        print("1. Par")
        print("2. Impar")
        par_impar = input()

        while par_impar.isnumeric() == False or int(par_impar) != 1 and int(par_impar) != 2:
            print("Ha ingresado mal, intente nuevamente")
            print("Desea apostar a Par o Impar?")
            print("1. Par")
            print("2. Impar")
            par_impar = input()

        par_impar = int(par_impar)

    # opcion 2 COLUMNA
    if opcion == 2:
        print("Ha elegido apostar a una columna")
        print("Columna 1: 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34")
        print("Columna 2: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35")
        print("Columna 3: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36")
        columna = (input("¿A qué columna desea apostar? "))

        while columna.isnumeric() == False or int(columna) != 1 and int(columna) != 2 and int(columna) != 3:
            print("Ha ingresado mal, intente nuevamente")
            print("¿A qué columna desea apostar? ")
            print("Columna 1: 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34")
            print("Columna 2: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35")
            print("Columna 3: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36")
            columna = input()

        columna = int(columna)

    # opcion 3 NUMERO

    if opcion == 3:
        print("Ha elegido apostar a un número")
        while True:
            numero_elegido = input("¿Qué número desea apostar? ")
            # la función isdigit() se usa para verificar si el valor ingresado por el usuario es un número válido.
            # Si es así, se convierte a un entero usando int(). Si no es un número válido,
            # se informa al usuario que ingresó un valor no válido y se solicita que ingrese un valor nuevamente.
            if numero_elegido.isdigit():
                numero_elegido = int(numero_elegido)
                if 0 < numero_elegido <= 36:
                    break
                else:
                    print("Ha ingresado mal, intente nuevamente.")
            else:
                print("Ha ingresado mal, intente nuevamente.")

# Opcion 4 color
    if opcion == 4:
        numeros_rojos = [1, 3, 5, 7, 9, 12, 14, 16,
                         18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        numeros_negros = [2, 4, 6, 8, 10, 11, 13, 15,
                          17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

        # pedir al jugador su apuesta
        print("Desea apostar a Rojo o Negro?")
        print("1. Rojo")
        print("2. Negro")
        color = input()

        while color.isnumeric() == False or int(color) != 1 and int(color) != 2:
            print("Ha ingresado mal, intente nuevamente")
            print("Desea apostar a Rojo o Negro?")
            print("1. Rojo")
            print("2. Negro")
            color = input()

        color = int(color)

     # primero le decimos cuanto dinero tiene para apostar

    print("Usted tiene", dinero, "para apostar.")

    # Pedir al usuario la cantidad que quiere apostar
    apuesta = input("Cuánto desea apostar? ")

    while apuesta.isdigit() == False or 0 >= float(apuesta) or float(apuesta) > dinero:

        print(
            "Ha ingresado un valor inválido o no tiene suficientes fondos, intente nuevamente."
        )

        apuesta = input("Cuánto desea apostar? ")

    apuesta = int(apuesta)

    # Repetir hasta que el usuario ingrese un monto válido

# IMPORTANTE

# ACTUALIZO DINERO

    # Actualizar la cantidad de dinero del usuario y mostrarla
    dinero -= apuesta
    print("Ha apostado " + str(apuesta) +
          ". Le quedan" + str(dinero) + "para usar.")
    # Preguntar al usuario si quiere seguir apostando
    if opcion == 1:
        betsArray.append([opcion, apuesta, par_impar])
    elif opcion == 2:
        betsArray.append([opcion, apuesta, columna])
    elif opcion == 3:
        betsArray.append([opcion, apuesta, numero_elegido])
    elif opcion == 4:
        betsArray.append([opcion, apuesta, color])
    else:
        print('Ha ingresado mal, intente nuevamente.')

    if dinero <= 0:
        print('No tiene mas plata para apostar')
        opcion_continuar = 0
    else:
        opcion_continuar = input("Desea seguir apostando?\n1. Si\n0. No\n")
    # Verificar que el usuario haya ingresado una opción válida (1 o 0)
        while opcion_continuar not in ["0", "1"]:
            print("Ha ingresado mal, intente nuevamente.")
            opcion_continuar = input("Desea seguir apostando?\n1. Si\n0. No\n")

    if opcion_continuar == "0":
        while len(betsArray) > 0:
            currentBet = betsArray.pop()
            opcion = currentBet[0]
            apuesta = currentBet[1]
            numero_ganador = random.randint(0, 36)

            if opcion == 1:
                par_impar = currentBet[2]
                print("Ha salido", numero_ganador)

                if numero_ganador % 2 == 0 and par_impar == 1 or numero_ganador % 2 == 1 and par_impar == 2:
                    ganancia = apuesta * 2
                    dinero += ganancia
                    print("Sus ganancias son " + str(ganancia) +
                          ", actualmente tiene " + str(dinero))
                else:
                    print("Sus ganancias son 0, actualmente tiene " + str(dinero))

            # como se define columnas
            if opcion == 2:
                columna = currentBet[2]
                print("Ha salido", numero_ganador)

                if columna == 1:

                    if numero_ganador in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
                        ganancia = apuesta * 3
                        dinero += ganancia
                        print("Sus ganancias son " + str(ganancia) +
                              ", actualmente tiene " + str(dinero))
                    else:
                        print("Sus ganancias son 0, actualmente tiene " + str(dinero))

                elif columna == 2:

                    if numero_ganador in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
                        ganancia = apuesta * 3
                        dinero += ganancia
                        print("Sus ganancias son " + str(ganancia) +
                              ", actualmente tiene " + str(dinero))
                    else:
                        print("Sus ganancias son 0, actualmente tiene " + str(dinero))

                else:
                    if numero_ganador in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
                        ganancia = apuesta * 3
                        dinero += ganancia
                        print("Sus ganancias son " + str(ganancia) +
                              ", actualmente tiene " + str(dinero))
                    else:
                        print("Sus ganancias son 0, actualmente tiene " + str(dinero))

            # COMO SE DEFINE NUMERO
            if opcion == 3:
                numero_elegido = currentBet[2]
                print("Ha salido", numero_ganador)
                if numero_ganador == numero_elegido:
                    ganancia = apuesta * 36
                    dinero += ganancia
                    print("Sus ganancias son " + str(ganancia) +
                          ", actualmente tiene " + str(dinero))
                else:
                    print("Sus ganancias son 0, actualmente tiene " + str(dinero))
            # SERE
            #

            # COMO SE DEFINE COLOR

            if opcion == 4:
                color = currentBet[2]
                print("El número es", numero_ganador)
                if (numero_ganador in numeros_rojos and color == 1) or (numero_ganador in numeros_negros and color == 2):
                    ganancia = apuesta * 2
                    dinero += ganancia
                    print("Sus ganancias son " + str(ganancia) +
                          ", actualmente tiene " + str(dinero))
                else:
                    print("Sus ganancias son 0, actualmente tiene " + str(dinero))
        print('Usted se retira de casino con ' + str(dinero) + ".")
        break
    elif opcion_continuar == "1":
        nextRound = True
        continue
        # Si el usuario elige 1, continuar apostando
     # Si el usuario elige 0, salir del ciclo
    # elif opcion_continuar == "1":
        # break;

# DESPUES DEL BREAK MENCIONO LOS GANADORES

# GANADOR PAR O INPAR

# if opcion == 1:
#     numero = random.randint(1, 36)
#     print("Ha salido", numero)

#     if numero % 2 == 0 and par_impar == "1" or numero % 2 == 1 and par_impar == "2":
#         dinero += apuesta * 2
#         ganancia = apuesta * 2

#         print("Sus ganancias son ", ganancia, ", actualmente tiene ", dinero)

#     else:

#         print("Sus ganancias son 0, actualmente tiene ", dinero)


# #como se define columnas
# if opcion == 2:
#     numero_ganador = random.randint(0, 36)

#     print("Ha salido", numero_ganador)

#     if columna == 1:

#         if numero_ganador in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
#             ganancias = apuesta * 3
#             dinero += ganancias
#             print("Ha ganado", ganancias, "actualmente tiene", dinero)
#         else:

#             print("Sus ganancias son 0, actualmente tiene ", dinero)

#     elif columna == 2:

#         if numero_ganador in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
#             ganancias = apuesta * 3
#             dinero += ganancias
#             print("Ha ganado", ganancias, "actualmente tiene", dinero)
#         else:
#             print("Sus ganancias son 0, actualmente tiene ", dinero)

#     else:
#         if numero_ganador in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
#             ganancias = apuesta * 3
#             dinero += ganancias
#             print("Ha ganado", ganancias, "actualmente tiene", dinero)
#         else:
#             print("Sus ganancias son 0, actualmente tiene ", dinero)


# #COMO SE DEFINE NUMERO
# if opcion == 3:
#     numero_ganador = random.randint(1, 36)
#     print("Ha salido", numero_ganador)
#     if numero_ganador == numero_elegido:
#         ganancias = apuesta * 36
#         dinero += ganancias
#         print("Ha ganado", ganancias, "actualmente tiene", dinero)
#     else:
#         print("Sus ganancias son 0, actualmente tiene", dinero)
# #SERE
# #


# # COMO SE DEFINE COLOR

# if opcion == 4:

#     numero = random.randint(1, 36)
#     print("El número es", numero)

#     if (numero in numeros_rojos and color == "rojo") or (numero in numeros_negros and color == "negro"):
#         ganancia = apuesta * 2
#         dinero += ganancia
#         print("Sus ganancias son ", ganancia, ", actualmente tiene ", dinero)
#     else:
#         print("Sus ganancias son 0, actualmente tiene ", dinero)
