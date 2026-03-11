# Datos
enero = 4500
febrero = 5200
marzo = 4800
abril = 3900
mayo = 5100
junio = 4200
julio = 4700
agosto = 4900
septiembre = 4300
octubre = 5500
noviembre = 5800
diciembre = 6100
# ... completa los demás meses

# Tu código aquí
ventas_mensuales = {
    "Enero": enero, "Febrero": febrero, "Marzo": marzo, "Abril": abril,
    "Mayo": mayo, "Junio": junio, "Julio": julio, "Agosto": agosto,
    "Septiembre": septiembre, "Octubre": octubre, "Noviembre": noviembre, "Diciembre": diciembre
}

total_ventas = sum(ventas_mensuales.values())
promedio_ventas = total_ventas/12
mes_maximo = max(ventas_mensuales, key=ventas_mensuales.get)
valor_maximo = ventas_mensuales[mes_maximo]
meta_anual = 50000
alcanzo_meta = total_ventas >= meta_anual
print(f"--- Reporte de Ventas Anual ---")
print(f"Total de ventas: €{total_ventas}")
print(f"Promedio mensual: €{promedio_ventas:.2f}")
print(f"Mes con más ventas: {mes_maximo} (${valor_maximo})")
print(f"¿Se alcanzó la meta de €{meta_anual}?: {'Sí' if alcanzo_meta else 'No'}")



### Ejercicio 2: Clasificador de préstamos

def clasificar_prestamo(dias):
    # Tu código aquí
    pass

# Datos de prueba
prestamos_dias = [15, 22, 18, 35, 25, 12, 40, 19, 28, 33]

#