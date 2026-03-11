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
promedio_ventas = total_ventas / len(ventas_mensuales)
### Pistas

