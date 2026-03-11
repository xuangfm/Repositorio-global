import random
def pedir_numero():
    while True:
        try:
            numero = int(input("Tu intento:"))
            return numero
        except ValueError:
            print("Eso no es un número válido")

def jugar_partida():
    numero_secreto = random.randit(1,100)
    intentos = 0
    print("He pensado un número entre 1 y 100. ¿Lo adivinas?")

    while True:
        intento = pedir_numero()
        intentos += 1

        if intento < numero_secreto:

            print ("El número que buscas es más alto.")

        elif intento > numero_secreto:

            print ("El número que buscas es más bajo.")
        else:
            print(f"¡Correcto! Lo adivinaste en {intentos} intentos")
        return intentos

def main():
    seguir_jugando = "s"
    mejor_puntuacion = None

    while seguir_jugando == "s":
        resultados = jugar_partida

        if mejor_puntuacion is None or resultados < mejor_puntuacion:
            mejor_puntuacion = resultados
            print(f"Nuevo record:{mejor_puntuacion}")
        else:
            print ("Tu mejor record es: {mejor_puntuacion}")

        seguir_jugando = input("¿Quieres seguir jugando?(s/n):")