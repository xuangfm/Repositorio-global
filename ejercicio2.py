def clasificar_prestamo(dias):
    contador_a_tiempo = 0
    contador_retraso_leve = 0
    contador_retraso_grave = 0

    for valor in dias:
        total_penalizacion = 0
        if valor <= 21:
            estado="A tiempo"
            penalizacion=0
            contador_a_tiempo += 1

        elif valor <= 30:
            estado = "Retraso leve"
            dias_retraso= valor - 21
            penalizacion = dias_retraso * 0.50
            contador_retraso_leve += 1

        else:
            estado = "Retraso grave"
            dias_retraso = valor - 21
            penalizacion = dias_retraso * 1
            contador_retraso_grave += 1
        total_penalizacion += penalizacion

    return {
        "contador_a_tiempo":contador_a_tiempo,
        "contador_retraso_leve": contador_retraso_leve,
        "contador_retraso_grave": contador_retraso_grave,
        "total_penalizacion" : total_penalizacion
    }

# Datos de prueba
prestamos_dias = [15, 22, 18, 35, 25, 12, 40, 19, 28, 33]
resultado = clasificar_prestamo(prestamos_dias)

print(f"Los prestamos no retrasados son:{resultado['contador_a_tiempo']}")
print(f"Los prestamos con retrasado leve son:{resultado['contador_retraso_leve']}")
print(f"Los prestamos con retrasado grave son:{resultado['contador_retraso_grave']}")
print(f"La penalización total es de :{resultado['total_penalizacion']} €")