# 04 - Endpoint para Listar Fórmulas

> **Archivo(s) creado(s):** `backend/routes/formulas.py`, `backend/routes/__init__.py`
> **Archivo(s) modificado(s):** `backend/main.py`
> **Fecha:** 2025-12-29
> **Estado:** ✅ Completado

---

## 1. ¿QUÉ VAMOS A HACER?

Vamos a crear un endpoint que devuelva todas las fórmulas matemáticas almacenadas en nuestra base de datos Supabase.

**Analogía:**
Siguiendo con la metáfora de la tienda:
- ✅ Tenemos la llave del almacén (cliente Supabase)
- ✅ Abrimos la puerta de la tienda (servidor FastAPI)
- ⏭️ Ahora creamos el **mostrador de productos** donde los clientes pueden ver el catálogo completo

El endpoint `/api/formulas` será como un catálogo: cuando alguien lo pide, vamos al almacén (Supabase), traemos todas las fórmulas, y las mostramos en formato JSON.

**¿Qué hace este endpoint?**
- URL: `http://localhost:8000/api/formulas`
- Método: GET
- Acción: Consulta la tabla `formulas` en Supabase
- Respuesta: JSON con todas las fórmulas

**Ejemplo de respuesta:**
```json
{
  "data": [
    {
      "id": 1,
      "nombre": "MRU - Movimiento Rectilíneo Uniforme",
      "categoria": "fisica",
      "formula_latex": "x = x_0 + v \\cdot t",
      ...
    }
  ],
  "error": null
}
```

---

## 2. ¿POR QUÉ LO NECESITAMOS?

### Problema que resuelve:

Este es el **primer endpoint real** de nuestra aplicación. Hasta ahora:
- `/health` solo verifica que el servidor funciona (no hace nada útil para el usuario)
- `/api/formulas` **resuelve un problema real**: el usuario necesita ver qué fórmulas hay disponibles

### Diferencia con /health:

| Característica | /health | /api/formulas |
|----------------|---------|---------------|
| Propósito | Técnico (monitoreo) | Funcional (dato real) |
| Usa BD | No | Sí ✅ |
| Usuario final | No lo ve | Sí lo usa |
| Complejidad | Muy simple | Moderada |

### En la aplicación final:

El frontend (HTML/JS) llamará a este endpoint para:
1. Mostrar la lista de fórmulas disponibles
2. Permitir que el usuario elija una fórmula
3. Cargar los datos de la fórmula seleccionada

---

## 3. ¿CÓMO ENCAJA EN EL PROYECTO?

```
FLUJO COMPLETO (ahora con /api/formulas):

┌────────────────────────────────────────────────┐
│  FRONTEND (futuro)                              │
│  Usuario hace click: "Ver fórmulas"            │
└──────────────┬─────────────────────────────────┘
               │
               │ GET /api/formulas
               ↓
┌────────────────────────────────────────────────┐
│  BACKEND - FastAPI (main.py)                   │
│                                                │
│  Recibe petición → Busca ruta /api/formulas   │
│         ↓                                      │
│  Delega a: formulas_router                    │
└──────────────┬─────────────────────────────────┘
               │
               ↓
┌────────────────────────────────────────────────┐
│  ROUTER - routes/formulas.py                   │
│                                                │
│  @router.get("/formulas")                     │
│  def listar_formulas():                       │
│      ↓                                         │
│  Importa: supabase (cliente)                  │
└──────────────┬─────────────────────────────────┘
               │
               │ supabase.table("formulas").select("*")
               ↓
┌────────────────────────────────────────────────┐
│  SUPABASE CLIENT - services/supabase_client.py│
│                                                │
│  Cliente hace petición HTTP a Supabase API    │
└──────────────┬─────────────────────────────────┘
               │
               │ REST API call
               ↓
┌────────────────────────────────────────────────┐
│  SUPABASE - PostgreSQL                         │
│                                                │
│  SELECT * FROM formulas;                       │
│  → Devuelve filas de la tabla                 │
└──────────────┬─────────────────────────────────┘
               │
               │ JSON con datos
               ↓
   (Viaje de regreso por el mismo camino)
               ↓
        Usuario recibe JSON
```

**Este endpoint une TODAS las piezas:**
1. ✅ Servidor FastAPI (main.py)
2. ✅ Cliente Supabase (supabase_client.py)
3. ✅ Base de datos (tabla formulas)
4. ⏭️ **NUEVO:** Router para organizar endpoints por funcionalidad

---

## 4. CONCEPTOS PREVIOS

### Concepto 1: APIRouter (Routers en FastAPI)

- **Qué es:** Una forma de organizar endpoints relacionados en archivos separados

- **Analogía:** En una tienda grande, no pones todo en un solo mostrador. Tienes secciones: ropa, electrónica, comida. Los routers son como esas secciones.

- **Sin routers (todo en main.py):**
  ```python
  # main.py - Se vuelve gigante
  @app.get("/api/formulas")
  def listar_formulas(): ...

  @app.get("/api/formula/{id}")
  def obtener_formula(): ...

  @app.post("/api/calcular")
  def calcular(): ...

  @app.get("/api/historial")
  def historial(): ...
  # ... 50 endpoints más
  ```

- **Con routers (organizado):**
  ```python
  # routes/formulas.py - Solo endpoints de fórmulas
  router = APIRouter(prefix="/api")

  @router.get("/formulas")
  def listar_formulas(): ...

  @router.get("/formula/{id}")
  def obtener_formula(): ...

  # routes/calculos.py - Solo endpoints de cálculos
  router = APIRouter(prefix="/api")

  @router.post("/calcular")
  def calcular(): ...

  # main.py - Solo importa y conecta
  from routes.formulas import router as formulas_router
  from routes.calculos import router as calculos_router

  app.include_router(formulas_router)
  app.include_router(calculos_router)
  ```

**Beneficios:**
- Código organizado por funcionalidad
- Archivos más pequeños y manejables
- Fácil encontrar y mantener endpoints
- Múltiples personas pueden trabajar en paralelo

### Concepto 2: Prefix en APIRouter

- **Qué es:** Un prefijo que se añade automáticamente a todas las rutas del router

- **Ejemplo:**
  ```python
  # Con prefix="/api"
  router = APIRouter(prefix="/api")

  @router.get("/formulas")  # Ruta real: /api/formulas
  @router.get("/calcular")  # Ruta real: /api/calcular
  ```

- **Ventaja:** No repetimos `/api` en cada endpoint

### Concepto 3: Tags en FastAPI

- **Qué es:** Etiquetas para agrupar endpoints en la documentación automática (/docs)

- **Ejemplo:**
  ```python
  router = APIRouter(prefix="/api", tags=["formulas"])
  ```

- **Resultado:** En /docs, todos los endpoints de este router aparecen bajo la sección "formulas"

### Concepto 4: Manejo de errores y respuestas estándar

- **Formato estándar de respuesta:**
  ```python
  # Éxito
  {"data": [...], "error": None}

  # Error
  {"data": None, "error": "Mensaje descriptivo"}
  ```

- **Por qué este formato:**
  - Consistente: el frontend siempre sabe qué esperar
  - Fácil verificar si hubo error: `if response.error`
  - Separa datos de metadatos

### Concepto 5: Importaciones relativas en Python

- **Qué son:** Importar módulos desde el mismo paquete

- **Ejemplo:**
  ```python
  # Desde routes/formulas.py importar backend/services/supabase_client.py

  # Opción 1: Absoluta (preferida)
  from backend.services.supabase_client import supabase

  # Opción 2: Relativa
  from ..services.supabase_client import supabase
  # .. = subir un nivel (desde routes a backend)
  ```

- **Usaremos importaciones absolutas** porque son más claras

---

## 5. EL CÓDIGO

### Estructura de archivos a crear:

```
backend/
├── __init__.py           ← Ya existe
├── main.py               ← Modificaremos
├── routes/               ← NUEVO directorio
│   ├── __init__.py       ← NUEVO
│   └── formulas.py       ← NUEVO (este archivo es el principal)
└── services/
    ├── __init__.py       ← Ya existe
    └── supabase_client.py ← Ya existe
```

---

### Archivo NUEVO: `backend/routes/__init__.py`

```python
# backend/routes/__init__.py
# Este archivo indica que 'routes' es un submódulo de 'backend'
# Contiene routers organizados por funcionalidad
```

---

### Archivo NUEVO: `backend/routes/formulas.py`

```python
# backend/routes/formulas.py
# ============================================
# QUÉ HACE: Endpoints relacionados con fórmulas
# CONSUME: backend.services.supabase_client (para consultar BD)
# EXPONE: Router con endpoints /api/formulas
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
```

---

### Archivo MODIFICADO: `backend/main.py`

```python
# backend/main.py
# ============================================
# QUÉ HACE: Punto de entrada de la aplicación FastAPI
# CONSUME: backend.routes.formulas (router de fórmulas)
# EXPONE: Servidor web con endpoints HTTP
# RELACIONADO CON:
#   - Ejecutado por: uvicorn
#   - Importa: backend/routes/formulas.py
# ============================================

from fastapi import FastAPI
from backend.routes.formulas import router as formulas_router

# Crear la aplicación FastAPI
app = FastAPI(
    title="API Fórmulas Matemáticas",
    description="Backend para visualización de fórmulas matemáticas y físicas",
    version="0.1.0"
)

# Incluir router de fórmulas
app.include_router(formulas_router)

# Endpoint de health check
@app.get("/health")
def health_check():
    """
    Endpoint de verificación de salud del servidor.

    Devuelve un mensaje simple indicando que el servidor está funcionando.
    Este endpoint se usa para:
    - Verificar que el servidor está corriendo
    - Monitoreo en producción
    - Tests automatizados

    Returns:
        dict: Diccionario con status y mensaje

    Example:
        GET http://localhost:8000/health

        Response:
        {
            "status": "ok",
            "message": "Servidor funcionando correctamente"
        }
    """
    return {
        "status": "ok",
        "message": "Servidor funcionando correctamente"
    }
```

---

### Explicación línea por línea de formulas.py:

| Líneas | Qué hacen | Por qué |
|--------|-----------|---------|
| 1-9 | Comentario de cabecera | Documenta el propósito del archivo |
| 11 | `from fastapi import APIRouter` | Importa la clase para crear routers |
| 12 | `from backend.services...` | Importa el cliente de Supabase que ya creamos |
| 15-18 | `router = APIRouter(...)` | Crea el router con prefijo /api y tag "formulas" |
| 20 | `@router.get("/formulas")` | Decorador: ruta completa será /api/formulas |
| 21 | `def listar_formulas():` | Función handler del endpoint |
| 22-51 | Docstring | Documentación completa con ejemplos |
| 52-54 | Bloque try | Maneja posibles errores de conexión |
| 54 | `supabase.table("formulas")` | Selecciona la tabla formulas |
| 54 | `.select("*")` | Pide todos los campos (SELECT *) |
| 54 | `.execute()` | Ejecuta la consulta |
| 57-60 | Return éxito | Devuelve datos con formato estándar |
| 62-67 | Except | Captura errores y devuelve formato estándar con error |

---

### Explicación de cambios en main.py:

| Línea | Qué cambió | Por qué |
|-------|------------|---------|
| 12 | `from backend.routes.formulas import router as formulas_router` | Importa el router que acabamos de crear |
| 20 | `app.include_router(formulas_router)` | Conecta el router con la app principal |

**¿Qué hace `include_router`?**
- Toma todos los endpoints del router (en este caso, `/api/formulas`)
- Los registra en la aplicación principal
- Ahora FastAPI sabe que cuando llega una petición a `/api/formulas`, debe llamar a `listar_formulas()`

---

## 5.1 HISTORIAL DE CAMBIOS EN EL CÓDIGO

*(Se llenará cuando haya modificaciones posteriores)*

---

## 6. PROBANDO QUE FUNCIONA

### Paso 1: Iniciar el servidor

```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
uvicorn backend.main:app --reload
```

### Paso 2: Probar el nuevo endpoint

**Opción A: Con curl**
```bash
curl http://localhost:8000/api/formulas
```

**Resultado esperado:**
```json
{
  "data": [
    {
      "id": 1,
      "nombre": "MRU - Movimiento Rectilíneo Uniforme",
      "categoria": "fisica",
      "formula_latex": "x = x_0 + v \\cdot t",
      "descripcion": "Describe el movimiento de un objeto que se mueve en línea recta a velocidad constante.",
      "variables": {
        "x": "Posición final",
        "x_0": "Posición inicial",
        "v": "Velocidad constante",
        "t": "Tiempo transcurrido"
      },
      "ejemplo": {
        "x_0": 0,
        "v": 5,
        "t_min": 0,
        "t_max": 10,
        "resultado": "x = 0 + 5*t"
      }
    }
  ],
  "error": null
}
```

**Opción B: Documentación interactiva**
- Abre: `http://localhost:8000/docs`
- Verás la sección "formulas" con el endpoint GET `/api/formulas`
- Click en "Try it out" → "Execute"
- Verás la respuesta directamente

### Paso 3: Verificar que /health sigue funcionando

```bash
curl http://localhost:8000/health
```

Debe seguir devolviendo:
```json
{"status":"ok","message":"Servidor funcionando correctamente"}
```

---

### Resultado obtenido:

**Petición:**
```bash
$ curl http://127.0.0.1:8000/api/formulas
```

**Respuesta:**
```json
{
  "data": [
    {
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
    }
  ],
  "error": null
}
```

**Verificación de /health:**
```bash
$ curl http://127.0.0.1:8000/health
{"status":"ok","message":"Servidor funcionando correctamente"}
```

---

## 7. ¿FUNCIONÓ?

### ✅ Si funcionó:

**¡SÍ, FUNCIONÓ PERFECTAMENTE!**

- Confirmamos que:
  1. ✅ El router se creó correctamente en `backend/routes/formulas.py`
  2. ✅ El router se incluyó exitosamente en `main.py` con `app.include_router()`
  3. ✅ El endpoint `/api/formulas` responde correctamente
  4. ✅ La consulta a Supabase se ejecutó sin errores
  5. ✅ Se recuperó la fórmula MRU de la base de datos
  6. ✅ La respuesta tiene el formato estándar: `{"data": [...], "error": null}`
  7. ✅ El endpoint `/health` sigue funcionando (no rompimos nada)

**Datos recuperados de la fórmula MRU:**
- ID: 1
- Nombre: "MRU - Movimiento Rectilíneo Uniforme"
- Categoría: "fisica"
- Fórmula LaTeX: "x = x_0 + v \\cdot t"
- Variable de rango: "t"
- Rango: 0 a 10
- Variables de usuario: v=5, x0=0
- Fecha de creación en BD: 2025-12-29

**Validaciones confirmadas:**
- ✅ APIRouter funciona correctamente
- ✅ Prefijo `/api` se aplica automáticamente
- ✅ Tag "formulas" aparecerá en la documentación
- ✅ Importación del cliente Supabase funciona
- ✅ Consulta `supabase.table("formulas").select("*")` ejecuta correctamente
- ✅ Manejo de errores con try/except implementado
- ✅ Organización del código en módulos (routes/) funciona

**Logro importante:**
- Este es el **primer endpoint que une FastAPI con Supabase**
- Demuestra que toda la arquitectura backend funciona correctamente
- El frontend podrá usar este endpoint para obtener el catálogo de fórmulas

- Siguiente paso lógico:
  - **Tarea 1.4:** Crear endpoint `/api/formula/{id}` para obtener una fórmula específica por su ID

### ❌ Si falló:

#### Posibles errores comunes:

1. **Error: "ModuleNotFoundError: No module named 'backend.routes'"**
   - Causa: Falta el archivo `__init__.py` en routes/
   - Solución: Crear archivo vacío `backend/routes/__init__.py`

2. **Error: "ModuleNotFoundError: No module named 'backend.services'"**
   - Causa: Ejecutaste uvicorn desde una carpeta incorrecta
   - Solución: Asegúrate de estar en `/Volumes/Akitio01/Claude_MCP/formulas-web`

3. **Error 500 al llamar /api/formulas**
   - Causa posible: Error de conexión con Supabase
   - Solución: Verificar que `.env` tiene las credenciales correctas
   - Debug: Ver logs de uvicorn para el error exacto

4. **Endpoint devuelve {"data": null, "error": "..."}**
   - Causa: El try/except capturó un error
   - Solución: Leer el mensaje de error en la respuesta
   - Debug: Ver logs del servidor para el traceback completo

---

## 8. RESUMEN

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué construimos? | Un endpoint que devuelve todas las fórmulas de la base de datos |
| ¿Para qué sirve? | Permitir al frontend obtener el catálogo completo de fórmulas disponibles |
| ¿Cómo se usa? | GET /api/formulas → Devuelve JSON con array de fórmulas |
| ¿Con qué se conecta? | Une FastAPI (main.py) con Supabase (supabase_client.py) |

**Logro importante:** Este es el **primer endpoint funcional** que consulta datos reales de la base de datos.

---

## 9. CONEXIÓN CON EL SIGUIENTE PASO

Ahora que tenemos un endpoint que devuelve **todas** las fórmulas, el siguiente paso (Tarea 1.4) es crear un endpoint que devuelva **una sola fórmula** por su ID.

**Por qué es el siguiente lógico:**
1. Ya sabemos cómo consultar Supabase ✅
2. Ya sabemos cómo crear endpoints con routers ✅
3. Ahora aprenderemos algo nuevo: **parámetros de ruta** (`/api/formula/{id}`)

**El proceso será:**
- Añadir endpoint GET `/api/formula/{formula_id}`
- Usar `.eq("id", formula_id)` para filtrar por ID
- Manejar el caso "fórmula no encontrada"

**Analogía del proceso:**
1. ✅ **Tarea 1.3:** Creamos el catálogo completo (mostrar todas las fórmulas)
2. ⏭️ **Tarea 1.4:** Permitimos buscar un producto específico (mostrar una fórmula por ID)

**Flujo de usuario completo (cuando terminemos):**
1. Usuario ve el catálogo → GET `/api/formulas`
2. Usuario elige una fórmula → GET `/api/formula/1`
3. Sistema carga los datos de esa fórmula específica

---

## 10. ACTUALIZACIONES POSTERIORES

*(Se añadirán actualizaciones aquí si hay cambios posteriores)*

---

*Documentación generada por Claude Code siguiendo el método socrático*
*NUNCA borrar contenido de este archivo - solo añadir*
