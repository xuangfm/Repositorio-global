# 🧠 Guía Universal: Cómo Resolver CUALQUIER Problema de Programación

## 🎯 Para qué sirve esta guía

Esta NO es una guía sobre Python, Java o ningún lenguaje específico.

**Es tu manual de supervivencia para cuando te enfrentes a un problema y pienses: "¿Y ahora qué hago?"**

Spoiler: La respuesta NO es "abrir StackOverflow y copiar código a lo loco". 🙃

---

## 🤔 La verdad incómoda sobre programar

**Programar NO es escribir código.**

Programar es:
- 🧩 **20% escribir código**
- 🧠 **80% pensar qué código escribir**

Si te lanzas directo a escribir código sin pensar, vas a:
- Escribir 100 líneas → No funciona
- Borrar todo → Frustración
- Empezar de nuevo → Más frustración
- Repetir hasta que abandones o llores (o ambas)

**Hay una forma mejor. Y es divertida. De verdad. 🎉**

---

## 🚀 El Método de los 7 Pasos (funciona SIEMPRE)

### Resumen visual rápido:

```
1️⃣ ENTENDER     → ¿Qué tengo que hacer?
2️⃣ DESCOMPONER  → Dividir en partes pequeñas
3️⃣ IDENTIFICAR  → ¿Qué herramientas necesito?
4️⃣ PSEUDOCÓDIGO → Escribir en lenguaje humano
5️⃣ TRADUCIR     → Convertir a código de verdad
6️⃣ PROBAR       → Ejecutar y ver qué explota
7️⃣ REFINAR      → Mejorar hasta que sea bonito
```

**Importante:** No puedes saltarte pasos. Es como armar un mueble de IKEA sin instrucciones. Técnicamente posible, pero te va a salir una mesa que parece silla.

---

## 1️⃣ PASO 1: Entender el problema (o "Lee la maldita letra pequeña")

### Antes de escribir UNA sola línea de código, responde:

**1.1. ¿Qué debe hacer mi programa?**

*El programa debe generar un número aleatortio del 1-100 y darnos pistas para solucionarlo*  

- Describe con tus palabras (como si se lo explicaras a tu abuela)
- Si no puedes explicarlo, NO lo entiendes todavía
- Si necesitas 10 minutos para explicarlo → es complicado → descomponlo

**1.2. ¿Qué recibe mi programa? (INPUT)**

*El programa primero recibe un nombre, si es el de juan, no lo deja avanzar porque lo rompería, siendo otro cualquiera, recibe un número y los consiguientes intentos.*  
- ¿Datos del usuario?
- ¿Un archivo?
- ¿Nada?

**1.3. ¿Qué debe entregar mi programa? (OUTPUT)**

*el programa debe devolver un "¡acertaste! si llegaste a dar con el número, y a continuación mostrar el conteo de intentos necesarios*
- ¿Un número?
- ¿Un mensaje?
- ¿Un archivo nuevo?
- ¿Un gráfico?

**1.4. ¿Cuándo termina?**

*se termina cuando se acierta el número que generó el ordenador.*
- ¿Cuando se cumple una condición?
- ¿Después de X repeticiones?
- ¿Cuando el usuario lo decide?

**1.5. ¿Qué puede salir mal?**
escribir mal los nombres de las variables, las tabulaciones (un horror, hay que estar muy pendiente), o cualquier otro error al intodicir los comandos

- Usuario escribe cosas raras → Validar
- El archivo no existe → Manejar error
- División por cero → Prevenir

### ✅ CHECKPOINT:

Si no puedes responder **TODAS** estas preguntas con claridad → **PARA. NO ESCRIBAS CÓDIGO.**

Vuelve a leer el problema. Pregunta. Investiga. Dibuja. Pero NO empieces a programar.

**Regla de oro:** 5 minutos aquí te ahorran 2 horas de frustración después.

---

## 2️⃣ PASO 2: Descomponer (o "Divide y vencerás, literalmente")

### El secreto mejor guardado de la programación:

**Los problemas grandes NO existen. Solo existen muchos problemas pequeños disfrazados de uno grande.**

### Cómo descomponer:

1. **Escribe el problema grande arriba**
2. **Pregunta: "¿Qué tengo que hacer primero?"**
3. **Anota esa tarea**
4. **Repite hasta que cada tarea sea simple**

### Ejemplo visual:

```
PROBLEMA: Hacer un análisis de ventas
│
├── TAREA 1: Leer el archivo de datos
│   ├── Subtarea 1.1: Abrir el archivo
│   ├── Subtarea 1.2: Leer línea por línea
│   └── Subtarea 1.3: Guardar en lista
│
├── TAREA 2: Limpiar los datos
│   ├── Subtarea 2.1: Eliminar filas vacías
│   ├── Subtarea 2.2: Convertir fechas
│   └── Subtarea 2.3: Validar números
│
├── TAREA 3: Calcular totales
│   ├── Subtarea 3.1: Sumar ventas por producto
│   └── Subtarea 3.2: Calcular promedio
│
└── TAREA 4: Mostrar resultados
    ├── Subtarea 4.1: Formatear números
    └── Subtarea 4.2: Imprimir reporte
```

### 🎯 Regla práctica:

**Si una tarea da miedo → Divídela más.**

Repite hasta que cada subtarea sea tan simple que pienses: "Eso sí lo puedo hacer".

### ⚠️ Señales de que necesitas descomponer más:

- "No sé ni por dónde empezar"
- La tarea tiene la palabra "y" más de 2 veces
- Te sientes abrumado/a solo de leerla

**Cada tarea debe ser completable en 10-30 minutos. Si no, divídela más.**

---

## 3️⃣ PASO 3: Identificar herramientas (o "¿Qué Pokemon elijo?")

Ahora que sabes QUÉ hacer, identifica CON QUÉ lo harás.

### 3.1. ¿Necesito repetir algo? → **BUCLES**

| Si... | Usa... | Ejemplo |
|-------|--------|---------|
| Sabes exactamente cuántas veces | `for` | "Repetir 10 veces" |
| No sabes cuántas veces | `while` | "Hasta que el usuario adivine" |
| Quieres aplicar algo a cada elemento de una lista | `for elemento in lista` | "Para cada archivo en la carpeta" |

**🎮 Analogía gamer:** Es como elegir entre un ataque que das X veces vs un ataque que repites hasta que el enemigo muera.

---

### 3.2. ¿Necesito tomar decisiones? → **CONDICIONALES**

| Si... | Usa... | Ejemplo |
|-------|--------|---------|
| Una decisión simple (sí/no) | `if / else` | "Si llueve, llevar paraguas" |
| Múltiples opciones | `if / elif / else` | "Si A → hacer X, si B → hacer Y, si no → hacer Z" |
| Decisión con muchas opciones | `match / case` (Python 3.10+) o diccionario | "Menú con 10 opciones" |

**🍕 Analogía pizza:** Es como elegir ingredientes. Si vegetariana → no carne. Si hawaiana → piña (controversial pero válido).

---

### 3.3. ¿Necesito guardar información? → **VARIABLES**

| Qué tipo de dato | Tipo de variable | Ejemplo |
|------------------|------------------|---------|
| Número entero | `int` | Edad, cantidad, contador |
| Número decimal | `float` | Precio, temperatura, promedio |
| Texto | `string` | Nombre, mensaje, dirección |
| Verdadero/Falso | `boolean` | ¿Está activo? ¿Terminó? |
| Colección de cosas | `list` | Lista de nombres, números, productos |
| Pares clave-valor | `dict` | Producto: precio, nombre: edad |

**🎒 Analogía mochila:** Variables son los bolsillos de tu mochila. Cada tipo de cosa va en el bolsillo correcto.

---

### 3.4. ¿Necesito reutilizar código? → **FUNCIONES**

Si vas a hacer lo mismo 3+ veces → crea una función.

```python
# ❌ MAL (código repetido)
print("="*50)
print("BIENVENIDA")
print("="*50)

# Más tarde...
print("="*50)
print("RESULTADOS")
print("="*50)

# ✅ BIEN (función reutilizable)
def mostrar_titulo(texto):
    print("="*50)
    print(texto)
    print("="*50)

mostrar_titulo("BIENVENIDA")
mostrar_titulo("RESULTADOS")
```

**🏭 Analogía fábrica:** Una función es una máquina. Le das materia prima (parámetros), hace su trabajo, te da resultado.

---

## 4️⃣ PASO 4: Pseudocódigo (o "Código para humanos")

### ¿Qué es pseudocódigo?

**Código escrito en tu idioma, no en lenguaje de programación.**

Es el borrador antes del código real. Como los apuntes antes del trabajo final.

### Por qué es importante:

- ✅ Verificas la lógica SIN preocuparte de la sintaxis
- ✅ Es más fácil compartir con alguien que no programa
- ✅ Si el pseudocódigo no funciona, el código TAMPOCO funcionará
- ✅ Ahorras tiempo (arreglar pseudocódigo es más rápido que arreglar código)

### Ejemplo: Calcular promedio de notas

#### ❌ Saltar directo al código (receta para el desastre):
```python
# Empiezas a escribir sin pensar...
def calc(n):
    t = 0
    # wait... ¿qué estaba haciendo?
    # *5 minutos de confusión*
```

#### ✅ Primero pseudocódigo:
```
FUNCIÓN calcular_promedio:
    1. Recibir lista de notas
    2. Inicializar suma en 0
    3. PARA CADA nota en la lista:
       3.1. Sumar nota al total
    4. Dividir suma entre cantidad de notas
    5. RETORNAR el promedio
```

#### ✅ Luego traducir a código:
```python
def calcular_promedio(notas):
    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma / len(notas)
    return promedio
```

**Ves la diferencia? El pseudocódigo es tu GPS. El código es el viaje.**

---

### Cómo escribir buen pseudocódigo:

**✅ HAZ esto:**
- Usa palabras simples ("SI", "MIENTRAS", "PARA CADA")
- Indenta para mostrar jerarquía
- Sé específico pero no técnico
- Numera los pasos

**❌ NO hagas esto:**
- No uses sintaxis real de Python (todavía no)
- No seas vago ("hacer cálculos" → ¿QUÉ cálculos?)
- No te saltes pasos porque "son obvios"

### ✅ CHECKPOINT:

Tu pseudocódigo está bien si:
- Una persona que NO programa puede entenderlo
- Puedes seguirlo paso por paso con papel y lápiz
- Cubre TODOS los casos (incluyendo errores)

---

## 5️⃣ PASO 5: Traducir a código (o "Del español al pythonés")

Ahora sí, hora de escribir código de verdad. Pero con trampa: ya sabes EXACTAMENTE qué escribir.

### Traducción directa: Diccionario Pseudocódigo → Python

| Pseudocódigo | Python | Otros lenguajes |
|--------------|--------|-----------------|
| SI... SINO... | `if... else...` | `if... else...` (casi universal) |
| PARA CADA X EN Y | `for x in y:` | `foreach`, `for (x in y)` |
| MIENTRAS X | `while x:` | `while (x)` |
| FUNCIÓN nombre | `def nombre():` | `function nombre()`, `def nombre` |
| RETORNAR X | `return x` | `return x` (universal) |
| MOSTRAR X | `print(x)` | `console.log(x)`, `echo $x`, `System.out.println(x)` |

### Ejemplo completo de traducción:

**Pseudocódigo:**
```
FUNCIÓN es_par(numero):
    SI numero dividido por 2 da resto 0:
        RETORNAR verdadero
    SINO:
        RETORNAR falso
```

**Python:**
```python
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
```

### 🎯 Estrategia de traducción:

1. **Lee una línea de pseudocódigo**
2. **Tradúcela a código**
3. **Ejecuta esa línea (si puedes)**
4. **Repite**

**No traduzcas todo de golpe. Línea por línea, como un traductor profesional.**

---

### ⚠️ Errores comunes al traducir:

**Error 1: Inventar la sintaxis**
```python
# ❌ MAL (inventado)
if numero is par:
    return "sí"

# ✅ BIEN (sintaxis real)
if numero % 2 == 0:
    return True
```

**Error 2: Olvidar los detalles**
```python
# ❌ MAL (sin dos puntos ni indentación)
if x > 5
print("grande")

# ✅ BIEN (sintaxis completa)
if x > 5:
    print("grande")
```

**Error 3: Traducir pero no entender**
```python
# ⚠️ CUIDADO (funciona pero no sabes por qué)
# Copiaste de internet sin entender
resultado = [x for x in range(10) if x % 2 == 0]

# ✅ MEJOR (escribes lo que entiendes)
resultado = []
for x in range(10):
    if x % 2 == 0:
        resultado.append(x)
```

**Regla: Si no puedes explicar qué hace cada línea, NO la uses.**

---

## 6️⃣ PASO 6: Probar (o "Romper tu código antes de que otros lo rompan")

### La verdad sobre los programas:

**El código que escribes por primera vez NUNCA funciona perfectamente.** 

Y está bien. Los bugs son normales. Son información, no fracasos.

### Estrategia de pruebas en 3 niveles:

**Nivel 1: Casos normales** 🟢
- Lo que esperas que pase
- Datos válidos y típicos
- Ejemplo: Si calculas promedio de [8, 9, 10] → debe dar 9

**Nivel 2: Casos límite** 🟡
- Situaciones al borde
- Ejemplo: Lista vacía, número 0, texto muy largo
- Aquí es donde los bugs aman esconderse

**Nivel 3: Casos malvados** 🔴
- Usuario haciendo cosas raras (a propósito o no)
- Ejemplo: Escribir "banana" donde esperas un número
- Ejemplo: Cargar archivo de 10GB cuando esperas 10KB

### Checklist de pruebas:

```
[ ] ¿Funciona con datos normales?
[ ] ¿Funciona con lista vacía?
[ ] ¿Funciona con un solo elemento?
[ ] ¿Funciona con números negativos?
[ ] ¿Funciona con texto en lugar de números?
[ ] ¿Funciona con datos muy grandes?
[ ] ¿Los mensajes de error son claros?
[ ] ¿El programa no se rompe nunca?
```

### 🐛 Cuando encuentres un bug:

**NO hagas esto:**
- ❌ Borrar todo y empezar de cero
- ❌ Cambiar 10 cosas a la vez
- ❌ Entrar en pánico

**HAZ esto:**
- ✅ Lee el mensaje de error COMPLETO
- ✅ Identifica EN QUÉ LÍNEA falla
- ✅ Usa `print()` para ver qué valores tienen las variables
- ✅ Cambia UNA cosa, prueba de nuevo
- ✅ Repite hasta arreglarlo

**🔍 Técnica del print() debugging:**
```python
def calcular_descuento(precio, porcentaje):
    print(f"DEBUG: precio = {precio}, porcentaje = {porcentaje}")  # ← Añade esto
    descuento = precio * (porcentaje / 100)
    print(f"DEBUG: descuento calculado = {descuento}")  # ← Y esto
    precio_final = precio - descuento
    print(f"DEBUG: precio_final = {precio_final}")  # ← Y esto
    return precio_final
```

Cuando funcione, quita los prints. Simple pero efectivo.

---

## 7️⃣ PASO 7: Refinar (o "De funcional a profesional")

Tu código funciona. ¡Felicidades! 🎉

Pero... ¿es **bueno**?

### Las 3 Rs del código profesional:

**R1: Readable (Legible)** 📖
- ¿Otra persona puede entenderlo?
- ¿TÚ lo entenderás en 6 meses?

**R2: Reusable (Reutilizable)** ♻️
- ¿Puedes usar partes en otros proyectos?
- ¿Hay funciones que puedas extraer?

**R3: Robust (Robusto)** 🛡️
- ¿Maneja errores?
- ¿Funciona con datos extraños?

---

### Checklist de refinamiento:

**✅ Nombres descriptivos:**
```python
# ❌ MAL
def f(x, y):
    return x * y / 100

# ✅ BIEN
def calcular_porcentaje(cantidad, porcentaje):
    return cantidad * porcentaje / 100
```

**✅ Comentarios útiles:**
```python
# ❌ MAL (obvio)
x = x + 1  # Incrementar x

# ✅ BIEN (explica el POR QUÉ)
x = x + 1  # Contamos desde 1 porque el índice 0 es el header
```

**✅ Funciones pequeñas:**
```python
# ❌ MAL (función de 200 líneas que hace TODO)
def procesar_datos_y_generar_reporte_y_enviar_email():
    # ... 200 líneas de código ...

# ✅ BIEN (varias funciones pequeñas)
def procesar_datos():
    # 20 líneas

def generar_reporte():
    # 30 líneas
    
def enviar_email():
    # 15 líneas
```

**✅ Manejo de errores:**
```python
# ❌ MAL (explota si el archivo no existe)
archivo = open("datos.txt")

# ✅ BIEN (maneja el error elegantemente)
try:
    archivo = open("datos.txt")
except FileNotFoundError:
    print("Error: No se encuentra el archivo datos.txt")
    return
```

---

### Versiones iterativas (de bueno a excelente):

**Versión 1: Funciona** ✅
- El código hace lo que debe hacer
- Mínimamente comentado

**Versión 2: Funciona bien** ✅✅
- Nombres descriptivos
- Maneja errores básicos
- Código organizado

**Versión 3: Funciona genial** ✅✅✅
- Funciones reutilizables
- Documentación completa
- Optimizado y elegante
- Otras personas quieren usar tu código

**No intentes hacer la versión 3 desde el principio. Itera. Mejora poco a poco.**

---

## 🎭 Mentalidad: De principiante a pro

### Mentalidad de principiante (lo que NO quieres):

- "Voy a escribir código hasta que funcione" → Método de fuerza bruta
- "No funciona, voy a cambiar cosas random" → Método del mono con teclado
- "Esto es muy difícil para mí" → Auto-sabotaje

### Mentalidad de pro (lo que SÍ quieres):

- "Voy a ENTENDER el problema antes de escribir código" → Método del científico
- "Tengo un plan, voy a seguirlo paso a paso" → Método del arquitecto
- "No sé cómo hacer esto... TODAVÍA" → Mentalidad de crecimiento

---

## 🚨 Situaciones de emergencia (troubleshooting emocional)

### "No sé ni por dónde empezar" 😰

**Solución:**
1. Ve al PASO 1 (Entender)
2. Escribe el problema en papel
3. Descomponlo en partes más pequeñas
4. Empieza por la parte más simple

**Mantra:** "No necesito resolver TODO. Solo necesito dar el primer paso."

---

### "Llevo 2 horas y no funciona" 😤

**Solución:**
1. **Para. Respira. Aléjate 10 minutos.**
2. Vuelve y lee tu código línea por línea
3. Explica tu código en voz alta (rubber duck debugging)
4. Si sigue sin funcionar: pide ayuda

**Regla de las 2 horas:** Si llevas 2+ horas atascado/a en lo mismo, es momento de pedir ayuda. No es debilidad, es eficiencia.

---

### "Mi código funciona pero no sé por qué" 😅

**Solución:**
1. Esto es una SEÑAL DE ALERTA
2. Línea por línea, escribe qué hace cada parte
3. Si no puedes explicarlo → bórralo y reescribe algo que SÍ entiendas

**Verdad dura:** Código que funciona por suerte, fallará por mala suerte. Tarde o temprano.

---

### "El de internet lo hace en 5 líneas, yo necesito 20" 🤔

**Solución:**
1. Está bien. Tu código funciona.
2. Código más largo NO es código peor (si es claro)
3. Prioridad 1: Que funcione
4. Prioridad 2: Que lo entiendas
5. Prioridad 3: Que sea elegante

**Verdad reconfortante:** Programadores senior escriben más código simple que código "clever". Clever = difícil de mantener.


### Las 5 verdades de la programación:

1. **Todos copiamos de internet.** La diferencia es que los pro entienden lo que copian.

2. **Los errores son tus amigos.** Cada error te enseña algo. Cero errores = cero aprendizaje.

3. **No existe "el programador nato".** Existe el programador que practica y el que no practica.

4. **El síndrome del impostor es mentira.** Si estás aprendiendo, estás exactamente donde debes estar.

5. **La mejor forma de aprender es haciendo.** Lee menos tutoriales, escribe más código.

---

## 🎮 Bonus: Técnicas ninja para debugging

### 1. **Rubber Duck Debugging** 🦆
Explica tu código línea por línea a un patito de goma (o a tu planta, o a tu gato).

**Por qué funciona:** Obligar a tu cerebro a verbalizar expone errores de lógica.

---

### 2. **Divide y comenta** 🔍
Comenta la mitad de tu código. Si funciona → el bug está en la mitad comentada.

```python
# def procesar_datos():
#     parte_1()
#     parte_2()
parte_3()  # Solo esta línea se ejecuta
parte_4()
```

---

### 3. **Regresa al último punto que funcionaba** ⏪
Si rompiste algo que funcionaba, vuelve atrás (gracias, Git).

**Sin Git:** Copia tu código que funciona ANTES de experimentar.

---

### 4. **Lee el error de ABAJO hacia ARRIBA** 📜
Los mensajes de error se leen al revés. La última línea suele ser la más útil.

---

## 📚 Recursos para seguir creciendo

### Cuando estés atascado/a:

1. **Lee el mensaje de error** (de verdad, léelo completo)
2. **Google: "python [tu error]"** (el 99% ya le pasó a alguien más)
3. **StackOverflow** (pero entiende la solución, no copies ciegamente)
4. **Documentación oficial** (aburrida pero precisa)
5. **Pregunta a un humano** (compañeras, formadoras, comunidad)

### Practica con:

- **Pequeños retos diarios** (mejor 15 min/día que 3 horas/sábado)
- **Proyectos personales** (algo que TE interese, no solo ejercicios)
- **Code reviews** (revisar código de otras personas te hace mejor)


### RECUERDA:

```python
while not_expert:
    practice()
    learn_from_mistakes()
    celebrate_small_wins()
    keep_going()

# Eventualmente...
return "Eres programadora ✨"
```

**Happy coding! 🚀💻**

---

*Material pedagógico elaborado para el Bootcamp Data Analyst*  
*Con cariño, humor y mucha experiencia en sufrir bugs 🐛*  
*Anaïs Rodríguez Villanueva - Febrero 2026*
