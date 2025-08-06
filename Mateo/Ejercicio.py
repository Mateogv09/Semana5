import random
import string

def generar_contraseña(longitud, usar_mayusculas, usar_numeros, usar_simbolos):
    caracteres = string.ascii_lowercase
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "No se ha seleccionado ningún tipo de carácter."

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    print("=== Generador de Contraseñas Seguras ===")
    
    try:
        longitud = int(input("Longitud de la contraseña: "))
        usar_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
        usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
        usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

        password = generar_contraseña(longitud, usar_mayusculas, usar_numeros, usar_simbolos)
        print(f"\n🔐 Contraseña generada: {password}")
    
    except ValueError:
        print("Error: Ingresa un número válido para la longitud.")

if __name__ == "__main__":
    main()
