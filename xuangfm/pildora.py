import json
def juego():
    arbol = {
        "pregunta" : "¿Es un animal?",
        "si": {
            "pregunta": "¿Ladra?", 
            "si": "Perro", 
            "no": "Gato"
        },
        "no": {
            "pregunta": "¿Es un vegetal?",
            "si": {
                "pregunta": "¿Es rojo?", 
                "si": "Manzana", 
                "no": "Lechuga"
            },
            "no": {
                "pregunta" : "¿Es un mineral?",
                "si": "Cobre",
                "no": "Algo desconocido" 
            }
        }
    }

    print("Bienvenido al juego de Animal, Vegetal o Mineral")
    print("Es sencillo, solo tienes que pensar en un animal, mineral o vegetal, y yo trataré de adivinarlo")
    
    while True:
        nodo_actual = arbol
        ramas = None

        while isinstance(nodo_actual, dict):
            respuesta = input(f"{nodo_actual['pregunta']} (s/n): ").lower()
            
            if respuesta == 's':
                ramas = "si"
            else:
                ramas = "no"
            
            nodo_anterior = nodo_actual 
            nodo_actual = nodo_actual[ramas]

        adivinanza = nodo_actual
        confirmar = input(f"¿Es un/a {adivinanza}? (s/n): ").lower()

        if confirmar == "s":
            print("¡La banca gana! soy un crack")
        else:
            print("¡Ufff! Me rindo, es muy difícil.")
            nuevo_objeto = input("¿En qué estabas pensando? ")
            nueva_pregunta = input(f"Escribe una pregunta que sea SI para '{nuevo_objeto}' y NO para '{adivinanza}': ")

            nueva_rama = {
                "pregunta": nueva_pregunta,
                "si": nuevo_objeto,
                "no": adivinanza
            }

            nodo_anterior[ramas] = nueva_rama
            print("¡Que divertido, me lo pasé muy bien, me gustaría seguir jugando contigo...")

        if input("\n¿Quieres volver a jugar? (s/n): ").lower() != "s":
            break

    print("¡pues ale, arreando!")

juego()
