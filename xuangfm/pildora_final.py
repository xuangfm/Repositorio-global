import json
import os

def juego():
    nombre_archivo = "memoria_juego.json"
    
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            arbol = json.load(f)
    else:
        arbol = {
            "pregunta": "¿Es un animal?",
            "si": {"pregunta": "¿Ladra?", "si": "Perro", "no": "Gato"},
            "no": {
                "pregunta": "¿Es un vegetal?",
                "si": {"pregunta": "¿Es una fruta?", "si": "Manzana", "no": "Lechuga"},
                "no": {
                    "pregunta": "¿Es un mineral?",
                    "si": "Cobre",
                    "no": "Eso no existe, no inventes"
                }
            }
        }

    print("Bienvenido al juego de Animal, Vegetal o Mineral")
    print("Es sencillo, solo tienes que pensar en un animal, mineral o vegetal, y yo trataré de adivinarlo")
    
    
    while True:
        nodo_actual = arbol
        nodo_anterior = None
        rama_elegida = None

        # NAVEGACIÓN
        while isinstance(nodo_actual, dict):
            nodo_anterior = nodo_actual
            respuesta = input(f"{nodo_actual['pregunta']} (s/n): ").lower()
            rama_elegida = "si" if respuesta == 's' else "no"
            nodo_actual = nodo_actual[rama_elegida]

        # ADIVINANZA
        adivinanza = nodo_actual
        confirmar = input(f"¿Es un/a {adivinanza}? (s/n): ").lower()

        if confirmar == "s":
            print("¡La banca gana")
        else:
            # APRENDIZAJE: Aquí es donde el árbol crece
            print("¡Ufff! Me rindo, es muy difícil.")
            nuevo_objeto = input("¿En qué estabas pensando? ")
            nueva_preg = input(f"Escribe una pregunta que sea SÍ para '{nuevo_objeto}' y NO para '{adivinanza}': ")

            nuevo_bloque = {
                "pregunta": nueva_preg,
                "si": nuevo_objeto,
                "no": adivinanza
            }

            # Injertamos el nuevo conocimiento en la rama exacta que falló
            nodo_anterior[rama_elegida] = nuevo_bloque
            
            # Guardado automático
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                json.dump(arbol, f, indent=4, ensure_ascii=False)
            print(f"Entendido. Ahora sé qué es un {nuevo_objeto}.")
            print("¡Que divertido, me lo pasé muy bien, me gustaría seguir jugando contigo...")

        if input("\n¿Quieres jugar otra vez? (s/n): ").lower() != "s":
            break

    print("¡pues ale, arreando!")

juego()