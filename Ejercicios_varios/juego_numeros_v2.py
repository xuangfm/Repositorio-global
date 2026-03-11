import random

def juego():
    nombre = input("¿Cómo te llamas? ").strip()
    
    if nombre.lower() in ["juan", "manolo"]:
        print(f"Lo siento {nombre}, de pequeño te caíste en una marmita llena de números...")
        print("Órdenes de arriba, no puedes jugar.")
        return

    while True:
        numero_secreto = random.randint(1, 100)
        intentos = 0
        limite_intentos = 20
        
        print(f"\nMuy bien, {nombre}. Pensé un número del 1 al 100.")
        print(f"Recuerda, solo tienes {limite_intentos} intentos.")

        while intentos < limite_intentos:
            try:
                intento = int(input(f"\n{nombre}, intento {intentos + 1}/{limite_intentos}. Pon tu número: "))
                intentos += 1

                if intento < numero_secreto:
                    print(f"Es más alto... Sigue intentándolo {nombre}.")
                elif intento > numero_secreto:
                    print(f"Es más bajo... Sigue intentándolo {nombre}.")
                else:
                    print(f"¡Bien hecho! El número era {numero_secreto}.")
                    print(f"¡¡Qué Crack, solo te costó {intentos} intentos!!")
                    break 
            
            except ValueError:
                print("¡¡Gañán!! Escribe un número que sea válido.")
        
       
        else:
            print(f"\nPerdiste {nombre}, te quedaste sin intentos matemáticu. El número era el {numero_secreto}.")

        while True:
            respuesta = input(f"¿{nombre}, ¿jugamos otra vez? (s/n): ").lower().strip()
            if respuesta in ["s", "n"]:
                break  
            else:
                print(f"Por favor, {nombre} escribe solo 's' para sí o 'n' para no, no la líes")
        
        if respuesta == "n":
            print(f"¡Hasta luegoooooooooooooo, {nombre}!")
            break 
if __name__ == "__main__":
    juego()