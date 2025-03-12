"""
Generador de contraseñas seguras.
Este script crea contraseñas aleatorias con letras, números y símbolos.
"""
import random
import string

# Definimos las constantes en mayúsculas según PEP 8
LETRAS_MAYUSCULAS = string.ascii_uppercase  # A-Z
LETRAS_MINUSCULAS = string.ascii_lowercase  # a-z
DIGITOS = string.digits                     # 0-9
SIMBOLOS = string.punctuation               # !@#$%^&* etc.

# Combinamos todos los caracteres en una sola lista
TODOS_CARACTERES = LETRAS_MAYUSCULAS + LETRAS_MINUSCULAS + DIGITOS + SIMBOLOS


def generate_password(password_length):
    """
    Genera una contraseña segura con la longitud especificada.

    Args:
        password_length (int): Longitud de la contraseña deseada.

    Returns:
        str: Contraseña generada, o None si la longitud es menor a 12.
    """
    if password_length < 12:
        print("¡Advertencia! Se recomienda una longitud mínima de 12 caracteres.")
        return None

    # Aseguramos al menos un carácter de cada tipo
    password = [
        random.choice(LETRAS_MAYUSCULAS),
        random.choice(LETRAS_MINUSCULAS),
        random.choice(DIGITOS),
        random.choice(SIMBOLOS)
    ]

    # Rellenamos el resto de la longitud con caracteres aleatorios
    for _ in range(password_length - 4):
        password.append(random.choice(TODOS_CARACTERES))

    # Mezclamos la contraseña
    random.shuffle(password)

    # Convertimos la lista en una cadena
    return ''.join(password)


# Bucle para generar contraseñas hasta que el usuario decida salir
while True:
    # Validación para asegurar que el usuario ingrese un número válido
    while True:
        try:
            length = int(
                input("¿Cuántos caracteres quieres en tu contraseña? (mínimo 12 recomendado): "))
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Generamos y mostramos la contraseña
    new_password = generate_password(length)
    if new_password:
        print(f"Tu contraseña segura es: {new_password}")

    # Preguntamos si quiere generar otra contraseña
    otra = input("¿Quieres generar otra contraseña? (sí/no): ").lower()
    if otra != "sí" and otra != "si":  # Si el usuario no dice "sí", salimos del bucle
        print("¡Gracias por usar el generador de contraseñas!")
        break
