#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# dados.py
#
# Author: Leonardo GV
# License: MIT Licence
# It is forbidden to copy or reuse total or partial this code without permission.
#
# ## ###############################################################

import sys
import random

while True:
    print(" ")
    print("Bienvenido al simulador de dados:")
    print("El programa lanzará dos dados, te mostrará los resultados y la suma de estos.")
    while True:
        check = input("Para iniciar el programa escriba: start y para finalizarlo escriba: exit \n")
        lowcheck = check.lower()
        if lowcheck == "start" or lowcheck == "exit":
            break
        else:
            print("Opción no válida. Por favor, ingrese 'start' para iniciar el programa o 'exit' para salir.")

    if lowcheck == "start":
        dado1 = random.choice([1, 2, 3, 4, 5, 6])
        dado2 = random.choice([1, 2, 3, 4, 5, 6])
        print("El valor del dado 1 es: ", dado1)
        print("El valor del dado 2 es: ", dado2)
        suma = dado1 + dado2
        print("La suma de ambos dados es: ", suma)
    elif lowcheck == "exit":
        print("El programa ha finalizado.")
        sys.exit()

    # Preguntar al usuario si desea volver a lanzar los dados
    while True:
        replay = input("¿Desea volver a lanzar los dados? (yes/no): ")
        if replay.lower() == "yes" or replay.lower() == "no":
            break
        else:
            print("Respuesta no válida. Por favor, ingrese 'yes' para volver a lanzar o 'no' para salir.")
    
    if replay.lower() == "no":
        print("El programa ha finalizado.")
        sys.exit()
