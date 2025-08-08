import random

def obtener_palabra():
    palabras = ['python', 'computadora', 'teclado', 'pantalla', 'programa', 'codigo', 'internet']
    return random.choice(palabras).lower()

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    mostrar = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            mostrar += letra + ' '
        else:
            mostrar += '_ '
    return mostrar.strip()

def juego_ahorcado():
    palabra = obtener_palabra()
    letras_adivinadas = []
    intentos_restantes = 6

    print("🎮 ¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra letra por letra.")
    
    while intentos_restantes > 0:
        print("\n" + mostrar_tablero(palabra, letras_adivinadas))
        print(f"Intentos restantes: {intentos_restantes}")
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue

        letras_adivinadas.append(letra)

        if letra not in palabra:
            intentos_restantes -= 1
            print("¡Incorrecto!")
        else:
            print("¡Correcto!")

        if all(l in letras_adivinadas for l in palabra):
            print(f"\n🎉 ¡Ganaste! La palabra era '{palabra}'.")
            break
    else:
        print(f"\n💀 Te has quedado sin intentos. La palabra era '{palabra}'.")

if __name__ == "__main__":
    juego_ahorcado()
