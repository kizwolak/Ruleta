import random
dinero = 1000
nextRound = False
betsArray = []

while True:
    if nextRound:
        print('######## Nueva ronda de apuestas ########')
        print("Usted tiene " + str(dinero) + " para usar.")

    else:
        print("##################  Bienvenido a la Ruleta  #####################")
        print("Usted tiene " + str(dinero) + " para usar.")

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

    if opcion == 3:
        print("Ha elegido apostar a un número")
        while True:
            numero_elegido = input("¿Qué número desea apostar? ")
            if numero_elegido.isdigit():
                numero_elegido = int(numero_elegido)
                if 0 < numero_elegido <= 36:
                    break
                else:
                    print("Ha ingresado mal, intente nuevamente.")
            else:
                print("Ha ingresado mal, intente nuevamente.")

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

    print("Usted tiene", dinero, "para apostar.")

    apuesta = input("Cuánto desea apostar? ")

    while apuesta.isdigit() == False or 0 >= float(apuesta) or float(apuesta) > dinero:

        print(
            "Ha ingresado un valor inválido o no tiene suficientes fondos, intente nuevamente."
        )

        apuesta = input("Cuánto desea apostar? ")

    apuesta = int(apuesta)

    dinero -= apuesta
    print("Ha apostado " + str(apuesta) +
          ". Le quedan " + str(dinero) + " para usar.")
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
        print('No tiene mas plata para apostar.')
        opcion_continuar = "0"
    else:
        opcion_continuar = input("Desea seguir apostando?\n1. Si\n0. No\n")
        while opcion_continuar not in ["0", "1"]:
            print("Ha ingresado mal, intente nuevamente.")
            opcion_continuar = input("Desea seguir apostando?\n1. Si\n0. No\n")

    if opcion_continuar == "0":
        numero_ganador = random.randint(0, 36)
        print("Ha salido", numero_ganador)

        while len(betsArray) > 0:
            currentBet = betsArray.pop()
            opcion = currentBet[0]
            apuesta = currentBet[1]

            if opcion == 1:
                ganancia = 0
                par_impar = currentBet[2]

                if par_impar == 1:
                    par_impar_desc = 'par'
                else:
                    par_impar_desc = 'impar'

                if numero_ganador % 2 == 0 and par_impar == 1 or numero_ganador % 2 == 1 and par_impar == 2:
                    ganancia = apuesta * 2
                    dinero += ganancia

                print("Como usted apostó " + str(apuesta) + " al " +
                      par_impar_desc + ", ganó " + str(ganancia) + ".")

            if opcion == 2:
                ganancia = 0
                columna = currentBet[2]

                if columna == 1:

                    if numero_ganador in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
                        ganancia = apuesta * 3
                        dinero += ganancia

                elif columna == 2:

                    if numero_ganador in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
                        ganancia = apuesta * 3
                        dinero += ganancia

                else:
                    if numero_ganador in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
                        ganancia = apuesta * 3
                        dinero += ganancia

                print("Como usted apostó " + str(apuesta) +
                      " al columna " + str(columna) + ", ganó " + str(ganancia) + ".")

            if opcion == 3:
                ganancia = 0
                numero_elegido = currentBet[2]
                if numero_ganador == numero_elegido:
                    ganancia = apuesta * 36
                    dinero += ganancia

                print("Como usted apostó " + str(apuesta) +
                      " al numero " + str(numero_elegido) + ", ganó " + str(ganancia) + ".")

            if opcion == 4:
                ganancia = 0
                color = currentBet[2]
                if color == 1:
                    color_desc = 'rojo'
                else:
                    color_desc = 'negro'
                if (numero_ganador in numeros_rojos and color == 1) or (numero_ganador in numeros_negros and color == 2):
                    ganancia = apuesta * 2
                    dinero += ganancia

                print("Como usted apostó " + str(apuesta) +
                      " al color " + color_desc + ", ganó " + str(ganancia) + ".")
        if dinero <= 0:
            print('Se ha quedado sin dinero.')
            print('Usted se retira de casino con ' + dinero + ".")
            break
        else:
            print('Desea seguir jugando?')
            print('1. Si')
            print('2. No')
            play_continue = input('')
            while play_continue != '1' and play_continue != '2':
                print("Ha ingresado mal, intente nuevamente.")
                play_continue = input('')
            if play_continue == '1':
                nextRound = True
                continue
            elif play_continue == '2':
                print('Usted se retira de casino con ' + dinero + ".")
                break

    elif opcion_continuar == "1":
        nextRound = True
        continue
