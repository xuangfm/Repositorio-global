import random

def obtener_nombre():
    entrada_nombre = input("¿Cómo te llamas? ").strip()
    nombre = entrada_nombre
    if nombre.lower() == "juan":
        print(f"Lo siento {nombre}, de pequeño te caiste en una marmita llena de números, y no se te permite jugar, prueba con otro nombre")
        print("Órdenes de arriba, no puedes jugar")
        return None
    return nombre

def jugar_ronda(nombre):
        numero_secreto = random.randint(1, 100)
        intentos = 0
        print(f"\nMuy bien, {nombre} pensé un número del 1 al 100. Intenta adivinarlo")

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
                    break

            except ValueError:
                print("¡¡Gañán!! escribe un número que sea válido")
def preguntar_reintento(nombre):
        respuesta = input(f"¿otra vez?, Ánimo {nombre}, lo hiciste muy bien (s/n): ").lower()
        if respuesta != "s":
            print(f"¡Hasta luuueeeego {nombre}!")
            
