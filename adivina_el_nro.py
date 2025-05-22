import random

nro_secreto= random.randint(1, 100)
adivinado = False
cant_intentos = 0
cant_intentos_max = 5

print("Bienvenido al juego de adivinar el número secreto")

while not adivinado:
  if not cant_intentos < cant_intentos_max:
    print("Has agotado tus intentos")
    break
  print(f"Intentos restantes: {cant_intentos_max - cant_intentos}")

  nro_usuario = int(input("Introduce  un número entre 1 y 99: "))
  if nro_usuario < nro_secreto:
    print("El número es mayor al ingresado")
  elif nro_usuario > nro_secreto:
    print("El número es menor al ingresado")
  else:
    print(f"¡Felicitaciones! Adivinaste el número es {nro_secreto}.")
    adivinado = True
  cant_intentos += 1
