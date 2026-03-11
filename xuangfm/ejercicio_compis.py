import json
def juego():
    arbol = {
        "pregunta" : "¿Es un animal?",
        "si": {
                "pregunta" : "¿ladra?",
                "si" : "Perro",
                "no" : "Gato"
        },
        "no" : {
            "pregunta" : "¿Es un vegetal?",
        "si" : {
            "pregunta" : "¿es rojo?",
            "si" : "Manzana",
            "no" : "Lechuga"
        },
        "no" : {
            "pregunta" : "¿Es un mineral?",
            "si" : "cobre",
            "no" : "Algo desconocido"
        }            
    }
}
    print("Bienvenidos al juego del Animal, vegetal o mineral")
    print("Es sencillo, solo tienes que pensar en un animal, vegetal o mineral y yo trataté de adivinarlo")

    while True:
        nodo_actual = arbol
        ramas = None
        
        while isinstance(nodo_actual, dict):
            respuesta = input(f"{nodo_actual['pregunta']} (s/n)").lower()
            if respuesta == "s":
                ramas = "si"
            else:
                ramas = "no"

            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual[ramas]

        adivinanza = nodo_actual
        confirmar =   input(f"¿Es un {adivinanza} (s/n)").lower()

        if confirmar == "s":
            print("Gané")
        else:
            print("me rindo, es muy dificil")
            nuevo_objeto = input("¿en qué estás pensando? ")
            nueva_pregunta = input(f"Escribe una pregunta que sea SI para el {nuevo_objeto}y NO para {adivinanza} ")

            nueva_rama = {
                "pregunta" : nueva_pregunta,
                "si" : nuevo_objeto,
                "no" : adivinanza
            }
            nodo_anterior[ramas] = nueva_rama
            print("¡que divertido, me lo pasé muyy bien, me gustaría seguir jugando contigo...")
        if input("\n¿Quieres volver a jugar? (s/n)").lower() !="s":
            break
    print("Adios")

juego()