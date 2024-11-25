import random

num_secreto = random.randint(0,100)
adivinado = False
cant_intentos = 0
cant_max_intento = 5


print("Bienvenido al juego de adivinar el numero secreto!")

while not adivinado:
    if not cant_intentos < cant_max_intento:
        print("GAME OVER! No has podido adivinar en 5 intentos")
        break
    numero = int(input("Introduce un numero del 1 al 99: ")) # To do: Pendiente

    if numero == num_secreto:
        print("Felicitaciones por adivinar el numero secreto!")
        adivinado = True
    elif numero < num_secreto:
        print("El numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")

    cant_intentos +=1

