print ("hola compas")
opciones = ["piedra","papel","tijera"]


j1 = input("piedra,papel,tijera")
j2 = input("piedra,papel,tijera")

while j1 not in("piedra,papel,tijera"):
    print("ingresa las opciones que dice el juego")
    j1 = input("piedra,papel,tijera")
    print("Jugador1 a seleccionado:",opciones)
    j2 = input("piedra,papel,tijera")
    print("jugador2 a seleccionado:",opciones)


if j1 in opciones:
    if j1 == j2:
        print("EMPATE")
    else:
        if j1 == "papel" and j2 == "piedra":
            print("Gano j1")
        elif j1 == "piedra" and j2 == "tijera":
            print("Gano j1")
        elif j1 == "tijera" and j2 == "papel":
            print("Gano j1")

if j2 in opciones:
    if j2 == j1:
        print("EMPATE")
    else:
        if j2 == "papel" and j1 == "piedra":
            print("Gano j2")
        elif j2 == "piedra" and j1 == "tijera":
            print("Gano j2")
        elif j2 == "tijera" and j1 == "papel":
            print("Gano j2")





