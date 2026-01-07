# 05 - Endpoint para Obtener Fórmula por ID

> **Archivo(s) modificado(s):** `backend/routes/formulas.py`
> **Fecha:** 2025-12-29
> **Estado:** ✅ Completado

---

## 1. ¿QUÉ VAMOS A HACER?

Vamos a crear un endpoint que devuelva **una sola fórmula** basándose en su ID.

**Analogía:**
Continuando con la metáfora de la tienda:
- ✅ Ya tenemos el catálogo completo (`/api/formulas`) - como un folleto con todos los productos
- ⏭️ Ahora creamos un servicio de búsqueda específica (`/api/formula/{id}`) - como pedirle al empleado "quiero el producto #1"

**Diferencia clave con /api/formulas:**

| Aspecto | /api/formulas | /api/formula/{id} |
|---------|---------------|-------------------|
| Devuelve | TODAS las fórmulas | UNA fórmula |
| URL | `/api/formulas` | `/api/formula/1` |
| Parámetros | Ninguno | ID en la URL |
| Filtro | Sin filtro | Filtro por ID |
| Error posible | - | "Fórmula no encontrada" |

**Ejemplos de uso:**
```
GET /api/formula/1  → Devuelve la fórmula MRU
GET /api/formula/2  → Devuelve la segunda fórmula (si existe)
GET /api/formula/999 → Error: "Fórmula no encontrada"
```

---

## 2. ¿POR QUÉ LO NECESITAMOS?

### Problema que resuelve:

Imagina que el usuario ya vio el catálogo completo con `/api/formulas` y eligió la fórmula #1. No tiene sentido volver a enviarle TODAS las fórmulas. Es más eficiente:

1. **Menor transferencia de datos:** Enviamos solo lo que necesita
2. **Más rápido:** La consulta a la BD es más eficiente
3. **Mejor UX:** El frontend puede cargar detalles de una fórmula específica

### Caso de uso real:

**Flujo completo del usuario:**
1. Usuario abre la app → Frontend llama a `/api/formulas`
2. Ve lista: "MRU", "MRUV", "Caída libre"... → Elige "MRU"
3. Frontend llama a `/api/formula/1` → Carga detalles completos de MRU
4. Usuario interactúa con los valores → Usa esos datos

Sin este endpoint, tendríamos que:
- Enviar TODAS las fórmulas cada vez (desperdicio)
- O duplicar datos en el frontend (ineficiente)

---

## 3. ¿CÓMO ENCAJA EN EL PROYECTO?

```
FLUJO DE NAVEGACIÓN DEL USUARIO:

1. Página inicial
   ↓
   GET /api/formulas
   ↓
   Lista completa: ["MRU", "MRUV", "Caída libre", ...]

2. Usuario hace click en "MRU"
   ↓
   GET /api/formula/1  ← ESTAMOS AQUÍ
   ↓
   Detalles completos de MRU

3. Usuario ajusta valores
   ↓
   POST /api/calcular (próxima tarea)
   ↓
   Resultado del cálculo
```

**Arquitectura del endpoint:**

```
Cliente hace: GET /api/formula/1
      ↓
FastAPI recibe la petición
      ↓
Router formulas.py
@router.get("/formula/{formula_id}")
      ↓
Extrae formula_id = 1
      ↓
supabase.table("formulas")
  .select("*")
  .eq("id", 1)      ← Filtro
  .execute()
      ↓
Supabase busca WHERE id = 1
      ↓
Si encuentra → {"data": {...}, "error": null}
Si NO encuentra → {"data": null, "error": "..."}
      ↓
Respuesta JSON al cliente
```

---

## 4. CONCEPTOS PREVIOS

### Concepto 1: Parámetros de ruta (Path Parameters)

- **Qué son:** Valores dinámicos dentro de la URL

- **Sintaxis en FastAPI:**
  ```python
  @router.get("/formula/{formula_id}")
  def obtener_formula(formula_id: int):
      # formula_id contiene el valor de la URL
  ```

- **Ejemplos:**
  ```
  URL: /api/formula/1
  formula_id = 1

  URL: /api/formula/42
  formula_id = 42

  URL: /api/formula/abc
  Error automático: FastAPI espera int, recibe str
  ```

- **Validación automática:** FastAPI convierte el string de la URL al tipo especificado (int) y valida automáticamente.

### Concepto 2: Filtrado en Supabase con .eq()

- **Qué es:** Método para filtrar resultados por igualdad (equality)

- **Sintaxis:**
  ```python
  # SQL equivalente: SELECT * FROM formulas WHERE id = 1
  supabase.table("formulas").select("*").eq("id", 1).execute()
  ```

- **Comparación:**
  ```python
  # Sin filtro (todas las fórmulas)
  supabase.table("formulas").select("*").execute()
  # → [{id: 1, ...}, {id: 2, ...}, {id: 3, ...}]

  # Con filtro por ID
  supabase.table("formulas").select("*").eq("id", 1).execute()
  # → [{id: 1, ...}]
  ```

- **Otros operadores de filtro en Supabase:**
  - `.eq("campo", valor)` → Igual a
  - `.neq("campo", valor)` → No igual a
  - `.gt("campo", valor)` → Mayor que
  - `.lt("campo", valor)` → Menor que
  - `.like("campo", patrón)` → LIKE (texto)

### Concepto 3: Manejo del caso "no encontrado"

- **Problema:** ¿Qué pasa si pedimos `/api/formula/999` y no existe?

- **Opciones de respuesta:**

  **Opción A: Error HTTP 404**
  ```python
  from fastapi import HTTPException

  if not response.data:
      raise HTTPException(status_code=404, detail="Fórmula no encontrada")
  ```
  - Ventaja: Estándar HTTP correcto
  - Desventaja: El frontend debe manejar códigos de error diferentes

  **Opción B: Respuesta 200 con error en el body (NUESTRA ELECCIÓN)**
  ```python
  if not response.data:
      return {"data": None, "error": "Fórmula no encontrada"}
  ```
  - Ventaja: Consistente con nuestro formato estándar
  - Ventaja: El frontend siempre espera el mismo formato
  - Desventaja: No usa el código HTTP semánticamente correcto

**Elegimos la Opción B** porque:
- Mantiene consistencia con nuestro formato `{"data": ..., "error": ...}`
- El frontend puede manejar todos los casos igual: `if (response.error) { ... }`
- Más simple para un proyecto educativo

### Concepto 4: Diferencia entre lista y objeto único

- **Cuando consultas SIN filtro:**
  ```python
  response.data = [
      {"id": 1, "nombre": "MRU"},
      {"id": 2, "nombre": "MRUV"}
  ]
  # Es una LISTA, aunque solo haya 1 elemento
  ```

- **Cuando filtras por ID único:**
  ```python
  response.data = [{"id": 1, "nombre": "MRU"}]
  # Sigue siendo LISTA con 1 elemento

  # Para devolver solo el objeto:
  response.data[0]  # {"id": 1, "nombre": "MRU"}
  ```

### Concepto 5: Truthiness en Python

- **Evaluar si hay datos:**
  ```python
  if response.data:
      # Se ejecuta si data NO está vacía
      # Lista vacía [] es False
      # Lista con elementos [{"id": 1}] es True

  if not response.data:
      # Se ejecuta si data ESTÁ vacía
  ```

- **Casos:**
  ```python
  [] → False (lista vacía)
  [{"id": 1}] → True (lista con datos)
  None → False
  ```

---

## 5. EL CÓDIGO

### Archivo MODIFICADO: `backend/routes/formulas.py`

Vamos a **añadir** un nuevo endpoint al archivo existente. No borramos nada, solo agregamos.

```python
# backend/routes/formulas.py
# ============================================
# QUÉ HACE: Endpoints relacionados con fórmulas
# CONSUME: backend.services.supabase_client (para consultar BD)
# EXPONE: Router con endpoints /api/formulas y /api/formula/{id}
# RELACIONADO CON:
#   - Usado por: backend/main.py (incluye este router)
#   - Usa: backend/services/supabase_client.py
# ============================================

from fastapi import APIRouter
from backend.services.supabase_client import supabase

# Crear router con prefijo y tag
router = APIRouter(
    prefix="/api",
    tags=["formulas"]
)

@router.get("/formulas")
def listar_formulas():
    """
    Devuelve todas las fórmulas disponibles en la base de datos.

    Este endpoint consulta la tabla 'formulas' en Supabase y devuelve
    todos los registros.

    Returns:
        dict: Diccionario con formato estándar
            - data: Lista de fórmulas (list)
            - error: None si éxito, mensaje si error (str | None)

    Example:
        GET http://localhost:8000/api/formulas

        Response 200 OK:
        {
            "data": [
                {
                    "id": 1,
                    "nombre": "MRU - Movimiento Rectilíneo Uniforme",
                    "categoria": "fisica",
                    "formula_latex": "x = x_0 + v \\cdot t",
                    "descripcion": "...",
                    "variables": {...},
                    "ejemplo": {...}
                }
            ],
            "error": null
        }

        Response 200 OK (con error):
        {
            "data": null,
            "error": "Error al consultar la base de datos: [detalle]"
        }
    """
    try:
        # Consultar la tabla 'formulas' en Supabase
        response = supabase.table("formulas").select("*").execute()

        # Devolver los datos con formato estándar
        return {
            "data": response.data,
            "error": None
        }

    except Exception as e:
        # Si hay error, devolver formato estándar con error
        return {
            "data": None,
            "error": f"Error al consultar la base de datos: {str(e)}"
        }

# ============================================
# NUEVO ENDPOINT - Se añade después del anterior
# ============================================

@router.get("/formula/{formula_id}")
def obtener_formula(formula_id: int):
    """
    Devuelve una fórmula específica por su ID.

    Este endpoint busca una fórmula en la base de datos filtrando por ID.
    Si la fórmula no existe, devuelve un error descriptivo.

    Args:
        formula_id (int): ID de la fórmula a buscar (parámetro de ruta)

    Returns:
        dict: Diccionario con formato estándar
            - data: Objeto con la fórmula (dict) o None si no existe
            - error: None si éxito, mensaje si error (str | None)

    Example:
        GET http://localhost:8000/api/formula/1

        Response 200 OK (fórmula encontrada):
        {
            "data": {
                "id": 1,
                "nombre": "MRU - Movimiento Rectilíneo Uniforme",
                "categoria": "fisica",
                "formula_latex": "x = x_0 + v \\cdot t",
                ...
            },
            "error": null
        }

        Response 200 OK (fórmula NO encontrada):
        {
            "data": null,
            "error": "Fórmula no encontrada"
        }

        Response 200 OK (error de BD):
        {
            "data": null,
            "error": "Error al consultar la base de datos: [detalle]"
        }
    """
    try:
        # Consultar la tabla 'formulas' filtrando por ID
        response = supabase.table("formulas").select("*").eq("id", formula_id).execute()

        # Verificar si se encontró la fórmula
        if not response.data:
            # Lista vacía = no se encontró
            return {
                "data": None,
                "error": "Fórmula no encontrada"
            }

        # Devolver solo el primer elemento (el objeto, no la lista)
        return {
            "data": response.data[0],
            "error": None
        }

    except Exception as e:
        # Si hay error de conexión/consulta, devolver formato estándar con error
        return {
            "data": None,
            "error": f"Error al consultar la base de datos: {str(e)}"
        }
```

---

### Explicación línea por línea del NUEVO endpoint:

| Líneas | Qué hacen | Por qué |
|--------|-----------|---------|
| 78 | `@router.get("/formula/{formula_id}")` | Define ruta con parámetro dinámico. Ruta completa: `/api/formula/1` |
| 79 | `def obtener_formula(formula_id: int):` | Recibe formula_id como entero. FastAPI lo extrae de la URL |
| 80-127 | Docstring | Documentación completa con ejemplos de éxito y error |
| 128-130 | Bloque try | Maneja posibles errores de conexión |
| 130 | `supabase.table("formulas")` | Selecciona la tabla formulas |
| 130 | `.select("*")` | Pide todos los campos |
| 130 | `.eq("id", formula_id)` | **FILTRO:** WHERE id = formula_id |
| 130 | `.execute()` | Ejecuta la consulta |
| 133-138 | Verificar si hay datos | Si `response.data` está vacío → fórmula no existe |
| 141-144 | Return éxito | Devuelve `response.data[0]` (el objeto, no la lista) |
| 146-151 | Except | Captura errores de BD/conexión |

---

### Diferencias clave con el endpoint anterior:

| Aspecto | /api/formulas | /api/formula/{id} |
|---------|---------------|-------------------|
| Parámetros | Ninguno | `formula_id: int` en la función |
| Filtro | Sin `.eq()` | Con `.eq("id", formula_id)` |
| Validación | No necesaria | Verifica `if not response.data` |
| Respuesta data | Lista `[...]` | Objeto `{...}` (usando `[0]`) |
| Posibles errores | Error de BD | Error de BD + "No encontrada" |

---

## 5.1 HISTORIAL DE CAMBIOS EN EL CÓDIGO

### Cambio #1 - 2025-12-29

**Archivo:** `backend/routes/formulas.py`

**Qué cambié (diff):**
```diff
# Al final del archivo, después del endpoint listar_formulas()

+@router.get("/formula/{formula_id}")
+def obtener_formula(formula_id: int):
+    """
+    Devuelve una fórmula específica por su ID.
+    [docstring completo...]
+    """
+    try:
+        response = supabase.table("formulas").select("*").eq("id", formula_id).execute()
+
+        if not response.data:
+            return {
+                "data": None,
+                "error": "Fórmula no encontrada"
+            }
+
+        return {
+            "data": response.data[0],
+            "error": None
+        }
+
+    except Exception as e:
+        return {
+            "data": None,
+            "error": f"Error al consultar la base de datos: {str(e)}"
+        }
```

**Por qué lo cambié:**
Necesitamos un endpoint que permita obtener los detalles de una fórmula específica cuando el usuario la selecciona del catálogo.

**Resultado:**
✅ Funcionó (se completará después de probar)

---

## 6. PROBANDO QUE FUNCIONA

### Paso 1: Iniciar el servidor (si no está corriendo)

```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
uvicorn backend.main:app --reload
```

---

### Paso 2: Probar con ID existente (1)

**Comando:**
```bash
curl http://localhost:8000/api/formula/1
```

**Resultado esperado:**
```json
{
  "data": {
    "id": 1,
    "nombre": "MRU - Movimiento Rectilíneo Uniforme",
    "categoria": "fisica",
    "formula_latex": "x = x_0 + v \\cdot t",
    "variable_rango": "t",
    "rango_min": 0,
    "rango_max": 10,
    "rango_dinamico": false,
    "variables_usuario": {
      "v": 5,
      "x0": 0
    },
    "created_at": "2025-12-29T13:20:49.296246+00:00"
  },
  "error": null
}
```

**Observación:** Nota que `data` es un **objeto** `{...}`, no una lista `[...]`

---

### Paso 3: Probar con ID inexistente (999)

**Comando:**
```bash
curl http://localhost:8000/api/formula/999
```

**Resultado esperado:**
```json
{
  "data": null,
  "error": "Fórmula no encontrada"
}
```

---

### Paso 4: Probar con ID inválido (no numérico)

**Comando:**
```bash
curl http://localhost:8000/api/formula/abc
```

**Resultado esperado:**
```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": ["path", "formula_id"],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "abc"
    }
  ]
}
```

**Observación:** FastAPI valida automáticamente que `formula_id` sea un entero. Si no lo es, devuelve error 422 (Unprocessable Entity).

---

### Paso 5: Verificar documentación automática

**Abrir:** `http://localhost:8000/docs`

Deberías ver dos endpoints en la sección "formulas":
- GET `/api/formulas` - Listar todas las fórmulas
- GET `/api/formula/{formula_id}` - Obtener una fórmula por ID

Puedes probar ambos directamente desde Swagger.

---

### Resultado obtenido:

**Prueba 1: ID existente (1)**
```bash
$ curl http://127.0.0.1:8000/api/formula/1
```

**Respuesta:**
```json
{
  "data": {
    "id": 1,
    "nombre": "MRU - Movimiento Rectilíneo Uniforme",
    "formula_latex": "x = x_0 + v \\cdot t",
    "variable_rango": "t",
    "rango_min": 0,
    "rango_max": 10,
    "rango_dinamico": false,
    "variables_usuario": {
      "v": 5,
      "x0": 0
    },
    "categoria": "fisica",
    "created_at": "2025-12-29T13:20:49.296246+00:00"
  },
  "error": null
}
```

**Observación:** El campo `data` es un **objeto** `{...}`, no una lista `[...]` ✅

---

**Prueba 2: ID inexistente (999)**
```bash
$ curl http://127.0.0.1:8000/api/formula/999
```

**Respuesta:**
```json
{
  "data": null,
  "error": "Fórmula no encontrada"
}
```

**Observación:** El manejo de "no encontrado" funciona correctamente ✅

---

## 7. ¿FUNCIONÓ?

### ✅ Si funcionó:

**¡SÍ, FUNCIONÓ PERFECTAMENTE!**

- Confirmamos que:
  1. ✅ El endpoint `/api/formula/{formula_id}` se creó correctamente
  2. ✅ Los parámetros de ruta funcionan (FastAPI extrae `formula_id` de la URL)
  3. ✅ El filtro `.eq("id", formula_id)` funciona en Supabase
  4. ✅ La respuesta devuelve un **objeto** (no una lista) con `response.data[0]`
  5. ✅ El manejo de "fórmula no encontrada" funciona correctamente
  6. ✅ El formato estándar se mantiene en ambos casos (éxito y error)

**Prueba con ID existente (1):**
- ✅ Devuelve objeto completo de la fórmula MRU
- ✅ Formato: `{"data": {...}, "error": null}`
- ✅ Campo `data` es un objeto, no una lista

**Prueba con ID inexistente (999):**
- ✅ Devuelve error descriptivo
- ✅ Formato: `{"data": null, "error": "Fórmula no encontrada"}`
- ✅ No lanza excepción, maneja el caso gracefully

**Validaciones confirmadas:**
- ✅ Parámetros de ruta en FastAPI funcionan correctamente
- ✅ Tipado automático (int) se aplica
- ✅ Filtrado con `.eq()` en Supabase funciona
- ✅ Verificación `if not response.data` detecta lista vacía
- ✅ Acceso a `response.data[0]` extrae el primer elemento
- ✅ Try/except captura errores de BD

**Logro importante:**
- Aprendimos a usar **parámetros de ruta** en FastAPI
- Implementamos **filtrado por ID** en Supabase
- Manejamos el caso **"no encontrado"** de forma consistente
- Completamos la **Fase 1** del proyecto 🎉

- Siguiente paso lógico:
  - **Fase 2 - Tarea 2.1:** Crear funciones de cálculo matemático (empezando con MRU)

### ❌ Si falló:

#### Posibles errores comunes:

1. **Error: "Formula_id" is required**
   - Causa: La URL no tiene el ID
   - Solución: Asegúrate de usar `/api/formula/1`, no `/api/formula/`

2. **Error 422 Unprocessable Entity**
   - Causa: Intentaste enviar un ID no numérico (ej: "abc")
   - Esto es correcto: FastAPI valida automáticamente

3. **Endpoint devuelve lista en lugar de objeto**
   - Causa: Olvidaste `response.data[0]`
   - Solución: Verificar que devuelves `data[0]`, no `data`

4. **Siempre devuelve "Fórmula no encontrada"**
   - Causa posible 1: Error en la consulta `.eq()`
   - Causa posible 2: El ID en la BD es diferente
   - Debug: Ver logs de uvicorn para el error exacto

---

## 8. RESUMEN

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué construimos? | Endpoint que devuelve una fórmula específica por su ID |
| ¿Para qué sirve? | Obtener detalles de una fórmula cuando el usuario la selecciona |
| ¿Cómo se usa? | GET /api/formula/{id} donde {id} es el número de la fórmula |
| ¿Con qué se conecta? | Complementa a /api/formulas (lista completa) |

**Conceptos clave aprendidos:**
- Parámetros de ruta en FastAPI `{formula_id}`
- Filtrado en Supabase con `.eq()`
- Manejo del caso "no encontrado"
- Diferencia entre devolver lista vs objeto único
- Validación automática de tipos en FastAPI

---

## 9. CONEXIÓN CON EL SIGUIENTE PASO

Con esto completamos la **Fase 1: Conexión Python ↔ Supabase** 🎉

Ya tenemos:
1. ✅ Cliente de Supabase
2. ✅ Servidor FastAPI funcionando
3. ✅ Endpoint para listar todas las fórmulas
4. ✅ Endpoint para obtener una fórmula por ID

**El siguiente paso es la Fase 2: Lógica de cálculo**

- **Tarea 2.1:** Crear funciones que calculen puntos para cada tipo de fórmula (empezando con MRU)
- Aprenderemos a usar NumPy para generar arrays de datos
- Crearemos el archivo `backend/services/calculadora.py`

**Analogía del proceso:**
1. ✅ **Fase 1 completada:** Ya podemos consultar qué fórmulas hay y obtener sus detalles
2. ⏭️ **Fase 2:** Ahora implementaremos la lógica para calcular valores con esas fórmulas
3. Después: Expondremos esa lógica a través de un endpoint POST /api/calcular

---

## 10. ACTUALIZACIONES POSTERIORES

*(Se añadirán actualizaciones aquí si hay cambios posteriores)*

---

*Documentación generada por Claude Code siguiendo el método socrático*
*NUNCA borrar contenido de este archivo - solo añadir*
