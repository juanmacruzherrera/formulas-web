# Guía Fundamental: Endpoints y API REST

> **Para quién es esto:** Para alguien que sabe Python pero no entiende por qué las webs se comunican así.
> **Objetivo:** Que nunca más olvides qué es un endpoint, por qué se separan, y cómo funciona REST.

---

## PARTE 1: ¿QUÉ PROBLEMA RESOLVEMOS?

### El problema básico

Tienes dos programas que necesitan hablar entre sí:

```
[Tu navegador]  ←???→  [Servidor con datos]
```

El navegador quiere datos. El servidor los tiene. **¿Cómo se entienden?**

Es como dos personas que hablan idiomas diferentes. Necesitan:
1. Un **idioma común** (HTTP)
2. Un **protocolo** de cómo pedir cosas (REST)
3. **Direcciones claras** de dónde pedir cada cosa (endpoints)

---

## PARTE 2: ¿QUÉ ES UN ENDPOINT?

### Definición simple

> **Endpoint = Dirección específica donde pedir algo específico**

Es como las ventanillas de un banco:

```
BANCO (Servidor)
┌─────────────────────────────────────────────┐
│                                             │
│  Ventanilla 1: DEPÓSITOS                    │  ← Solo para depositar
│  Ventanilla 2: RETIROS                      │  ← Solo para sacar dinero
│  Ventanilla 3: CONSULTAS                    │  ← Solo para preguntar saldo
│  Ventanilla 4: PRÉSTAMOS                    │  ← Solo para pedir préstamos
│                                             │
└─────────────────────────────────────────────┘
```

**No vas a la ventanilla de DEPÓSITOS a preguntar tu saldo.** Cada ventanilla tiene UN propósito.

### En código

```
SERVIDOR (http://localhost:8000)
┌─────────────────────────────────────────────┐
│                                             │
│  /api/formulas     → Lista de fórmulas      │
│  /api/formula/1    → Una fórmula específica │
│  /api/calcular     → Hacer un cálculo       │
│  /api/historial    → Ver cálculos pasados   │
│                                             │
└─────────────────────────────────────────────┘
```

Cada `/ruta` es un **endpoint**. Cada uno hace UNA cosa.

---

## PARTE 3: ¿POR QUÉ SEPARAR EN VARIOS ENDPOINTS?

### Analogía 1: El restaurante

#### Opción A: Un empleado hace todo (MAL)

```
RESTAURANTE CON 1 EMPLEADO
┌────────────────────────────────┐
│                                │
│  Juan hace TODO:               │
│  - Recibe clientes             │
│  - Toma pedidos                │
│  - Cocina                      │
│  - Sirve                       │
│  - Cobra                       │
│  - Limpia                      │
│                                │
│  → CAOS, LENTO, ERRORES        │
│                                │
└────────────────────────────────┘
```

#### Opción B: Cada persona hace una cosa (BIEN)

```
RESTAURANTE ORGANIZADO
┌────────────────────────────────┐
│                                │
│  Recepcionista → Recibe        │
│  Camarero      → Toma pedidos  │
│  Cocinero      → Cocina        │
│  Camarero      → Sirve         │
│  Cajero        → Cobra         │
│  Limpiador     → Limpia        │
│                                │
│  → RÁPIDO, CLARO, SIN ERRORES  │
│                                │
└────────────────────────────────┘
```

**Los endpoints son como los empleados especializados.**

---

### Analogía 2: Las puertas de tu casa

```
TU CASA
┌─────────────────────────────────────┐
│                                     │
│  Puerta principal → Entran visitas  │
│  Puerta garaje    → Entra el coche  │
│  Puerta jardín    → Sales al jardín │
│  Ventana          → Entra luz/aire  │
│                                     │
└─────────────────────────────────────┘
```

¿Meterías el coche por la puerta principal? No. Cada entrada tiene su propósito.

**Los endpoints son las "puertas" de tu servidor.** Cada una para algo específico.

---

### Analogía 3: Los cajeros del supermercado

```
SUPERMERCADO
┌─────────────────────────────────────┐
│                                     │
│  Cajero 1  → "Cesta rápida" (< 10)  │
│  Cajero 2  → Compras normales       │
│  Cajero 3  → Compras normales       │
│  Cajero 4  → Solo tarjeta           │
│  Cajero 5  → Devoluciones           │
│                                     │
└─────────────────────────────────────┘
```

Imagina UN solo cajero para todo. Colas infinitas.

**Los endpoints dividen el trabajo para ser eficientes.**

---

### Analogía 4: El teléfono de atención al cliente

Cuando llamas a una empresa:

```
"Pulse 1 para VENTAS"        → /api/ventas
"Pulse 2 para SOPORTE"       → /api/soporte
"Pulse 3 para FACTURAS"      → /api/facturas
"Pulse 4 para CANCELAR"      → /api/cancelar
```

¿Por qué no hablas directo con alguien que haga todo? Porque sería caótico y lento.

**Los endpoints son como las opciones del menú telefónico.**

---

## PARTE 4: ¿QUÉ ES HTTP?

### El idioma de la web

HTTP = **H**yper**T**ext **T**ransfer **P**rotocol

Es el "idioma" que usan navegadores y servidores para entenderse.

### Una conversación HTTP

```
NAVEGADOR: "Oye servidor, DAME la página /inicio"
SERVIDOR:  "Aquí tienes: <html>Bienvenido</html>"

NAVEGADOR: "Ahora GUARDA este formulario en /contacto"
SERVIDOR:  "Guardado. Todo OK."

NAVEGADOR: "BORRA el mensaje número 5"
SERVIDOR:  "Borrado."
```

Fíjate en las palabras clave: **DAME**, **GUARDA**, **BORRA**.

Esas son las **acciones** que puedes pedir. En HTTP se llaman **métodos**.

---

## PARTE 5: LOS MÉTODOS HTTP (GET, POST, PUT, DELETE)

### ¿Qué son?

Son las **acciones** que puedes hacer sobre un endpoint.

Es como los verbos en español:
- **Leer** un libro
- **Escribir** un libro
- **Modificar** un libro
- **Tirar** un libro

### Los 4 métodos principales

| Método | Acción | Analogía | ¿Cambia datos? |
|--------|--------|----------|----------------|
| **GET** | Obtener/Leer | "Dame el menú" | ❌ No |
| **POST** | Crear/Enviar | "Toma mi pedido" | ✅ Sí |
| **PUT** | Actualizar/Modificar | "Cambia mi pedido" | ✅ Sí |
| **DELETE** | Borrar/Eliminar | "Cancela mi pedido" | ✅ Sí |

---

### GET: Obtener información

```
GET = "Dame información, no cambies nada"
```

**Ejemplos de la vida real:**
- Mirar el menú de un restaurante (no pides nada, solo miras)
- Consultar el saldo en el cajero (no sacas dinero, solo miras)
- Leer un libro en la biblioteca (no te lo llevas, solo lees)

**Ejemplos en código:**
```
GET /api/formulas      → "Dame todas las fórmulas"
GET /api/formula/1     → "Dame la fórmula número 1"
GET /api/historial     → "Dame los cálculos anteriores"
```

**Característica clave:** Puedes hacer GET 100 veces y nada cambia. Solo lees.

---

### POST: Crear algo nuevo

```
POST = "Toma estos datos y CREA algo nuevo"
```

**Ejemplos de la vida real:**
- Hacer un pedido en un restaurante (creas un pedido nuevo)
- Enviar un formulario de contacto (creas un mensaje nuevo)
- Subir una foto a Instagram (creas una publicación nueva)

**Ejemplos en código:**
```
POST /api/calcular     → "Toma estos valores, calcula, y GUARDA el resultado"
POST /api/usuarios     → "Crea un usuario nuevo con estos datos"
POST /api/pedidos      → "Crea un pedido nuevo"
```

**Característica clave:** Cada POST crea algo nuevo. Si haces POST 3 veces, creas 3 cosas.

---

### PUT: Modificar algo existente

```
PUT = "Toma estos datos y REEMPLAZA lo que había"
```

**Ejemplos de la vida real:**
- Cambiar tu dirección en Amazon (modificas tu perfil)
- Editar un documento de Google Docs (modificas el documento)
- Actualizar tu foto de perfil (reemplazas la anterior)

**Ejemplos en código:**
```
PUT /api/formula/1     → "Modifica la fórmula 1 con estos nuevos datos"
PUT /api/usuario/5     → "Actualiza los datos del usuario 5"
```

**Característica clave:** No crea nada nuevo, modifica lo que ya existe.

---

### DELETE: Borrar algo

```
DELETE = "Elimina esto"
```

**Ejemplos de la vida real:**
- Borrar un email
- Cancelar una reserva
- Eliminar una foto

**Ejemplos en código:**
```
DELETE /api/calculo/3  → "Borra el cálculo número 3"
DELETE /api/usuario/5  → "Elimina el usuario 5"
```

**Característica clave:** Irreversible (normalmente). Una vez borrado, borrado está.

---

### Resumen visual de métodos

```
┌─────────────────────────────────────────────────────────────┐
│                         MÉTODOS HTTP                        │
├─────────┬───────────────┬───────────────┬───────────────────┤
│ MÉTODO  │    ACCIÓN     │   ANALOGÍA    │  ¿CAMBIA DATOS?   │
├─────────┼───────────────┼───────────────┼───────────────────┤
│   GET   │    Leer       │  Mirar menú   │       ❌ No       │
│  POST   │    Crear      │  Hacer pedido │       ✅ Sí       │
│   PUT   │  Modificar    │ Cambiar pedido│       ✅ Sí       │
│ DELETE  │   Borrar      │Cancelar pedido│       ✅ Sí       │
└─────────┴───────────────┴───────────────┴───────────────────┘
```

---

## PARTE 6: ¿QUÉ ES REST?

### Definición simple

REST = **RE**presentational **S**tate **T**ransfer

Es un **conjunto de reglas** para diseñar APIs de forma ordenada y predecible.

### Las reglas de REST (simplificadas)

#### Regla 1: Usa URLs que representen "cosas" (sustantivos)

```
✅ BIEN (sustantivos):
/api/formulas        → "las fórmulas"
/api/usuarios        → "los usuarios"
/api/calculos        → "los cálculos"

❌ MAL (verbos):
/api/obtenerFormulas
/api/crearUsuario
/api/hacerCalculo
```

El **verbo** (obtener, crear, hacer) lo dice el **método HTTP** (GET, POST), no la URL.

#### Regla 2: Usa el método HTTP correcto

```
Quiero LEER las fórmulas      → GET    /api/formulas
Quiero CREAR un cálculo       → POST   /api/calculos
Quiero MODIFICAR la fórmula 1 → PUT    /api/formulas/1
Quiero BORRAR el cálculo 3    → DELETE /api/calculos/3
```

#### Regla 3: Usa IDs para recursos específicos

```
/api/formulas      → TODAS las fórmulas
/api/formulas/1    → Solo la fórmula con ID 1
/api/formulas/5    → Solo la fórmula con ID 5
```

#### Regla 4: Devuelve respuestas consistentes

```python
# Siempre el mismo formato
{"data": ..., "error": None}      # Si todo bien
{"data": None, "error": "..."}    # Si hay error
```

---

### ¿Por qué seguir REST?

Porque es un **estándar mundial**. Cualquier programador del planeta entiende:

```
GET /api/usuarios/5
```

Significa: "Dame el usuario número 5". Sin explicaciones. Universal.

---

## PARTE 7: JUNTANDO TODO - NUESTRO PROYECTO

### Los endpoints de nuestra web de fórmulas

```
┌────────────────────────────────────────────────────────────────┐
│                    API DE FÓRMULAS MATEMÁTICAS                 │
├──────────┬─────────────────────┬───────────────────────────────┤
│  MÉTODO  │      ENDPOINT       │         QUÉ HACE              │
├──────────┼─────────────────────┼───────────────────────────────┤
│   GET    │  /health            │ ¿El servidor está vivo?       │
│   GET    │  /api/formulas      │ Dame TODAS las fórmulas       │
│   GET    │  /api/formula/1     │ Dame la fórmula número 1      │
│   POST   │  /api/calcular      │ Calcula esto y guárdalo       │
│   GET    │  /api/historial     │ Dame los cálculos anteriores  │
└──────────┴─────────────────────┴───────────────────────────────┘
```

### El flujo completo

```
USUARIO                         FRONTEND                        BACKEND                         SUPABASE
   │                               │                               │                               │
   │  "Quiero ver las fórmulas"    │                               │                               │
   │ ─────────────────────────────>│                               │                               │
   │                               │  GET /api/formulas            │                               │
   │                               │ ─────────────────────────────>│                               │
   │                               │                               │  SELECT * FROM formulas       │
   │                               │                               │ ─────────────────────────────>│
   │                               │                               │                               │
   │                               │                               │  [lista de fórmulas]          │
   │                               │                               │ <─────────────────────────────│
   │                               │  {"data": [...], "error": null}                               │
   │                               │ <─────────────────────────────│                               │
   │  [Muestra las fórmulas]       │                               │                               │
   │ <─────────────────────────────│                               │                               │
   │                               │                               │                               │
   │  "Calcula MRU con v=5"        │                               │                               │
   │ ─────────────────────────────>│                               │                               │
   │                               │  POST /api/calcular           │                               │
   │                               │  {formula_id: 1, valores: {}} │                               │
   │                               │ ─────────────────────────────>│                               │
   │                               │                               │  [Calcula con Python]         │
   │                               │                               │  INSERT INTO calculos         │
   │                               │                               │ ─────────────────────────────>│
   │                               │                               │                               │
   │                               │                               │  [OK, guardado]               │
   │                               │                               │ <─────────────────────────────│
   │                               │  {"data": {puntos}, "error": null}                            │
   │                               │ <─────────────────────────────│                               │
   │  [Muestra la gráfica]         │                               │                               │
   │ <─────────────────────────────│                               │                               │
```

---

## PARTE 8: EJERCICIOS MENTALES

### Ejercicio 1: ¿Qué método HTTP?

Para cada situación, di qué método usarías:

| Situación | Método |
|-----------|--------|
| Ver mi lista de tareas pendientes | ? |
| Añadir una tarea nueva | ? |
| Marcar una tarea como completada | ? |
| Eliminar una tarea | ? |
| Ver los detalles de la tarea 5 | ? |

<details>
<summary>Ver respuestas</summary>

| Situación | Método |
|-----------|--------|
| Ver mi lista de tareas pendientes | **GET** |
| Añadir una tarea nueva | **POST** |
| Marcar una tarea como completada | **PUT** |
| Eliminar una tarea | **DELETE** |
| Ver los detalles de la tarea 5 | **GET** |

</details>

---

### Ejercicio 2: Diseña los endpoints

Tienes una app de recetas de cocina. ¿Qué endpoints necesitas?

Pista: Piensa en qué "cosas" (sustantivos) maneja la app.

<details>
<summary>Ver respuestas</summary>

```
GET    /api/recetas          → Listar todas las recetas
GET    /api/recetas/1        → Ver receta número 1
POST   /api/recetas          → Crear receta nueva
PUT    /api/recetas/1        → Modificar receta 1
DELETE /api/recetas/1        → Borrar receta 1

GET    /api/ingredientes     → Listar ingredientes
GET    /api/categorias       → Listar categorías (postres, carnes, etc.)
```

</details>

---

### Ejercicio 3: ¿Está bien diseñado?

Evalúa estos endpoints. ¿Siguen REST correctamente?

```
1. POST /api/obtenerUsuarios
2. GET /api/usuarios
3. GET /api/borrarUsuario/5
4. DELETE /api/usuarios/5
5. POST /api/usuarios/crear
6. POST /api/usuarios
```

<details>
<summary>Ver respuestas</summary>

```
1. POST /api/obtenerUsuarios  → ❌ MAL (verbo en URL, debería ser GET)
2. GET /api/usuarios          → ✅ BIEN
3. GET /api/borrarUsuario/5   → ❌ MAL (verbo en URL, GET no borra)
4. DELETE /api/usuarios/5     → ✅ BIEN
5. POST /api/usuarios/crear   → ❌ MAL (verbo "crear" sobra)
6. POST /api/usuarios         → ✅ BIEN
```

</details>

---

### Ejercicio 4: Traduce a español

¿Qué significa cada petición HTTP?

```
1. GET /api/productos
2. GET /api/productos/42
3. POST /api/pedidos
4. PUT /api/usuarios/7
5. DELETE /api/comentarios/99
```

<details>
<summary>Ver respuestas</summary>

```
1. "Dame la lista de todos los productos"
2. "Dame el producto número 42"
3. "Crea un pedido nuevo (con los datos que te envío)"
4. "Actualiza el usuario número 7 (con los datos que te envío)"
5. "Borra el comentario número 99"
```

</details>

---

### Ejercicio 5: El test del camarero

Imagina que eres camarero. El cliente dice estas frases. ¿Qué método HTTP representa cada una?

1. "¿Me trae la carta?"
2. "Quiero pedir una pizza margarita"
3. "Perdone, cambie la pizza por una cuatro quesos"
4. "Cancele el postre, ya no lo quiero"
5. "¿Cuánto es la cuenta?"

<details>
<summary>Ver respuestas</summary>

1. "¿Me trae la carta?" → **GET** (solo quiere VER)
2. "Quiero pedir una pizza" → **POST** (CREA un pedido)
3. "Cambie la pizza" → **PUT** (MODIFICA el pedido)
4. "Cancele el postre" → **DELETE** (ELIMINA parte del pedido)
5. "¿Cuánto es la cuenta?" → **GET** (solo quiere VER)

</details>

---

## PARTE 9: ERRORES COMUNES Y LECCIONES

### Error 1: Poner verbos en la URL

```
❌ MAL:  POST /api/crearUsuario
✅ BIEN: POST /api/usuarios
```

**Lección:** El método HTTP (POST) ya dice "crear". No lo repitas en la URL.

---

### Error 2: Usar GET para modificar datos

```
❌ MAL:  GET /api/borrarUsuario/5
✅ BIEN: DELETE /api/usuarios/5
```

**Lección:** GET es solo para LEER. Si cambias algo, usa POST/PUT/DELETE.

---

### Error 3: No ser consistente con las respuestas

```
❌ MAL:
/api/usuarios → {"usuarios": [...]}
/api/productos → {"data": [...]}
/api/pedidos → {"items": [...]}

✅ BIEN:
/api/usuarios → {"data": [...], "error": null}
/api/productos → {"data": [...], "error": null}
/api/pedidos → {"data": [...], "error": null}
```

**Lección:** Siempre el mismo formato. El frontend no tiene que adivinar.

---

### Error 4: Olvidar el nombre exacto de las columnas

En nuestro proyecto, Claude Code escribió:

```python
❌ MAL:  "valores": datos.valores
✅ BIEN: "valores_entrada": datos.valores
```

**Lección:** La columna en Supabase se llama `valores_entrada`, no `valores`. 
Siempre verifica los nombres exactos de la base de datos.

---

## PARTE 10: RESUMEN FINAL

### Una imagen vale más que mil palabras

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   ENDPOINT = Dirección + Método                                     │
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                                                             │   │
│   │   GET    +  /api/formulas   =  "Dame las fórmulas"          │   │
│   │   POST   +  /api/calcular   =  "Guarda este cálculo"        │   │
│   │   DELETE +  /api/calculo/1  =  "Borra el cálculo 1"         │   │
│   │                                                             │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│   REST = Reglas para diseñar APIs ordenadas y predecibles           │
│                                                                     │
│   • URLs con sustantivos (/usuarios, /productos)                    │
│   • Verbos en el método HTTP (GET, POST, PUT, DELETE)               │
│   • IDs para recursos específicos (/usuarios/5)                     │
│   • Respuestas consistentes (siempre mismo formato)                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Frase para recordar

> **"Cada endpoint es una puerta. Cada método es una acción. REST es el manual de instrucciones."**

---

## PARTE 11: REFERENCIAS RÁPIDAS

### Métodos HTTP - Chuleta

```
GET    → Leer (no cambia nada)
POST   → Crear (añade algo nuevo)
PUT    → Modificar (cambia algo existente)
DELETE → Borrar (elimina algo)
```

### Analogías - Chuleta

```
Endpoints   = Ventanillas del banco / Puertas de casa / Cajeros del súper
Métodos     = Verbos (leer, crear, modificar, borrar)
REST        = Reglas de cómo organizar todo
URL         = Dirección
JSON        = Formato de los datos (como un diccionario Python)
```

### Nuestros endpoints - Chuleta

```
GET  /health           → ¿Servidor vivo?
GET  /api/formulas     → Lista fórmulas
GET  /api/formula/{id} → Una fórmula
POST /api/calcular     → Calcular y guardar
GET  /api/historial    → Ver cálculos pasados
```

---

*Documento creado: 29 diciembre 2024*
*Propósito: Que Juan nunca olvide cómo funcionan los endpoints y REST*
*Método: Explicación progresiva con múltiples analogías y ejercicios*
