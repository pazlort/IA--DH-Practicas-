import difflib
import random

opciones = ["PIEDRA", "PAPEL", "TIJERA"]
jugar_de_nuevo = True

name = input('Ingresa tu nombre: ').upper()

def entrada(name, game):

    game = game.strip().upper()
    
    if game in opciones:
        return game

    coincidencia = difflib.get_close_matches(game, opciones, n=1, cutoff=0.6)

    if coincidencia:
        eleccion_final = coincidencia[0]
        print(f"{name}, entendí que elegiste: {eleccion_final}")
        validacion = input('¿Es correcto? S(i)/N(o): ').lower()
        if validacion == 's':
            return eleccion_final

    game = input(f"{name}, no entendí tu entrada. ¿Qué elegís? ¿Piedra, papel o tijera? ").strip().upper()
    return entrada(name, game)

def eleccion_computadora():
    return random.choice(opciones)

def juego_nuevo(respuesta):
    if respuesta == 's':
        return True
    elif respuesta == 'n':
        print('¡Gracias, vuelvas pronto!')
        return False
    else:
        print("Respuesta no válida. Se asumirá que no querés jugar de nuevo.")
        return False

def resultado(user, compu):
    if user == compu:
        print("Empataron!")
    elif (user == 'TIJERA' and compu == 'PAPEL') or (user == 'PAPEL' and compu == 'PIEDRA') or (user == 'PIEDRA' and compu == 'TIJERA'):
        print("Ganaste! Te felicito!")
    else:
        print("Perdiste!")
    

while jugar_de_nuevo:
    game = input(f"{name}, ¿Que elegis? ¿Piedra, papel o tijera? ").strip().upper()
    user = entrada(name,game)
    compu = eleccion_computadora()

    print(f"{name} eligió: {user}")
    print(f"La computadora eligió: {compu}")

    resultado(user, compu)

    respuesta = input("\n¿Querés jugar de nuevo? S(i)/N(o): ").lower()
    jugar_de_nuevo = juego_nuevo(respuesta)