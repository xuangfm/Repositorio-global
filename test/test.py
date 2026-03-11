import random
import random


def juego():
    # Línea 4: Pedimos el nombre
    entrada_nombre = input("¿Cómo te llamas? ").strip()

    # IMPORTANTE: Definimos la variable nombre aquí para que no de error luego
    nombre = entrada_nombre

    # Bloqueo para Juan
    if nombre.lower() == "juan":
        print("Lo siento juan no puedes jugar")
        print("Órdenes de arriba, no puedes jugar")
        return

    # Bucle principal para volver a jugar
    while True:
        numero_secreto = random.randint(1, 100)
        intentos = 0
        print(f"\nMuy bien, {nombre} pensé un número del 1 al 100. Intenta adivinarlo")

        # Bucle de la partida actual
        while True:
            try:
                intento = int(input(f"{nombre}, pon tu número: "))
                intentos += 1

                if intento < numero_secreto:
                    print(f"Es más alto ... Sigue intentándolo {nombre}.")
                elif intento > numero_secreto:
                    print(f"Es más bajo... Sigue intentándolo {nombre}.")
                else:
                    print(f"¡bien hecho! el número era {numero_secreto}.")
                    print(f"¡¡Qué Crack, solo te costó {intentos} intentos.!!")
                    break  # Este break detiene el bucle de adivinanza

            except ValueError:
                print("¡¡Gañán!! escribe un número que sea válido")

        # Pregunta para volver a jugar
        respuesta = input(f"¿otra vez?, Ánimo {nombre}, lo hiciste muy bien (s/n): ").lower()
        if respuesta != "s":
            print(f"¡Hasta luuueeeego {nombre}!")
            break  # Este break detiene el bucle principal y cierra el juego


if __name__ == "__main__":
    juego()