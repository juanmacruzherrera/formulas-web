# 07 - Endpoint POST /api/calcular

> **Archivo(s) creado(s):** `backend/routes/calculos.py`
> **Archivo(s) modificado(s):** `backend/main.py`
> **Fecha:** 2025-12-29
> **Estado:** ✅ Completado (después de corregir 2 errores)

---

## 1. ¿QUÉ VAMOS A HACER?

Vamos a crear un endpoint que reciba los valores que el usuario quiere calcular (por ejemplo, velocidad y tiempo inicial), realice el cálculo usando la función `calcular_mru()` que ya construimos, guarde el resultado en la base de datos para tener un historial, y devuelva los puntos calculados para que el frontend pueda dibujar la gráfica.

**Analogía:** Es como un cajero automático. Tú llegas con tu tarjeta (formula_id) y le dices cuánto quieres retirar (valores). El cajero verifica tu cuenta (consulta la BD), hace el cálculo (usa calculadora.py), registra la transacción (guarda en tabla calculos), y te da el dinero (devuelve los puntos).

---

## 2. ¿POR QUÉ LO NECESITAMOS?

Hasta ahora tenemos:
- ✅ Función `calcular_mru()` que hace cálculos matemáticos
- ✅ Conexión a Supabase para leer fórmulas

Pero **falta el puente** que permita al usuario enviar sus valores desde el frontend, que el backend los procese, guarde el resultado, y devuelva los datos para graficar.

Sin este endpoint, la función de cálculo está "huérfana" - existe pero nadie puede usarla desde el navegador.

---

## 3. ¿CÓMO ENCAJA EN EL PROYECTO?

```
┌──────────────┐
│   FRONTEND   │
│ (HTML/JS)    │
└──────┬───────┘
       │
       │ POST /api/calcular
       │ {formula_id: 1, valores: {...}}
       ▼
┌──────────────────────────────────┐
│        BACKEND (FastAPI)         │
│  ┌────────────────────────────┐  │
│  │  ESTA PIEZA:               │  │
│  │  routes/calculos.py        │  │
│  │  Endpoint POST /calcular   │  │
│  └─────┬──────────────────┬───┘  │
│        │                  │      │
│        ▼                  ▼      │
│  ┌─────────┐      ┌──────────┐  │
│  │ supabase│      │calculadora│ │
│  │ _client │      │   .py     │  │
│  └─────┬───┘      └─────┬────┘  │
│        │                 │       │
└────────┼─────────────────┼───────┘
         │                 │
         ▼                 ▼
   ┌─────────┐       ┌─────────┐
   │ Supabase│       │  Numpy  │
   │   BD    │       │ Cálculos│
   └─────────┘       └─────────┘
```

**Flujo de datos:**
1. Frontend envía formula_id + valores
2. Endpoint consulta tabla `formulas` para saber qué tipo es
3. Endpoint llama a `calcular_mru()` con los valores
4. Endpoint guarda resultado en tabla `calculos`
5. Endpoint devuelve puntos al frontend
6. Frontend dibuja la gráfica con Plotly

---

## 4. CONCEPTOS PREVIOS

### Concepto 1: POST vs GET

- **Qué es:**
  - **GET**: Pedir datos (como leer un libro)
  - **POST**: Enviar datos para que se procesen (como rellenar un formulario)

- **Analogía:**
  - GET = "¿Me das la lista de fórmulas?" → El servidor te la da
  - POST = "Aquí tienes mis datos, calcúlame esto" → El servidor procesa y responde

- **Ejemplo simple:**
  ```
  GET  /api/formulas       → "Dame todas las fórmulas"
  POST /api/calcular       → "Calcula esto: {v: 5, t: 10}"
  ```

- **Diferencias técnicas:**
  - GET: Datos en la URL (`/api/formula/1`)
  - POST: Datos en el cuerpo (body) de la petición (no visibles en la URL)

### Concepto 2: Pydantic y BaseModel

- **Qué es:**
  Pydantic es una librería que **valida automáticamente** los datos que recibe el endpoint. BaseModel es como una "plantilla" que dice "estos son los datos que espero recibir y de qué tipo son".

- **Analogía:**
  Es como un guardia de seguridad en la puerta de un edificio. Tiene una lista de requisitos:
  - "Necesitas tu DNI (formula_id debe ser un número)"
  - "Necesitas rellenar este formulario (valores debe ser un diccionario)"

  Si vienes sin DNI, el guardia te rechaza antes de que entres.

- **Ejemplo simple:**
  ```python
  class DatosCalculo(BaseModel):
      formula_id: int      # Debe ser un número entero
      valores: dict        # Debe ser un diccionario
  ```

  Si alguien envía `formula_id: "hola"` (texto en vez de número), Pydantic **automáticamente rechaza** la petición con un error descriptivo.

- **Ventajas:**
  1. **Seguridad:** Evita que datos incorrectos lleguen a tu código
  2. **Documentación automática:** FastAPI usa estos modelos para generar documentación
  3. **Menos código:** No necesitas escribir `if tipo(formula_id) != int: error...`

### Concepto 3: Cuerpo de petición (Request Body)

- **Qué es:**
  Cuando haces POST, los datos no van en la URL sino en el "cuerpo" (body) de la petición HTTP. Es como un sobre cerrado con información dentro.

- **Analogía:**
  - GET es como gritar en la calle: "¡Dame la fórmula 1!" (todos pueden verlo en la URL)
  - POST es como meter una carta en un sobre: nadie ve qué hay dentro excepto el servidor

- **Formato (JSON):**
  ```json
  {
    "formula_id": 1,
    "valores": {
      "x0": 0,
      "v": 5,
      "t_min": 0,
      "t_max": 10
    }
  }
  ```

### Concepto 4: Tabla `calculos` en Supabase

Necesitamos una tabla para guardar el historial de cálculos. Estructura:

```
Tabla: calculos
┌────┬────────────┬─────────────────┬────────────────────┐
│ id │ formula_id │     valores     │ resultado (JSONB)  │
├────┼────────────┼─────────────────┼────────────────────┤
│ 1  │     1      │ {"v":5, "x0":0} │ {"t":[...], "x":[]}│
│ 2  │     1      │ {"v":3, "x0":2} │ {"t":[...], "x":[]}│
└────┴────────────┴─────────────────┴────────────────────┘
```

Esto nos permitirá:
- Ver historial de cálculos del usuario
- Analizar qué fórmulas se usan más
- Permitir "rehacer" un cálculo anterior

---

## 5. EL CÓDIGO

### Archivo: `backend/routes/calculos.py`

```python
# backend/routes/calculos.py
# ============================================
# QUÉ HACE: Endpoints para realizar cálculos de fórmulas
# CONSUME:
#   - Datos del usuario (formula_id + valores) vía POST
#   - Fórmulas de Supabase (tabla formulas)
# EXPONE:
#   - POST /api/calcular → Calcula, guarda y devuelve resultado
# RELACIONADO CON:
#   - Usa: backend/services/supabase_client.py (conexión BD)
#   - Usa: backend/services/calculadora.py (función calcular_mru)
#   - Usado por: frontend/js/api.js (próxima fase)
# ============================================

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from backend.services.supabase_client import supabase
from backend.services.calculadora import calcular_mru

# Crear router con prefijo /api y etiqueta "calculos"
router = APIRouter(
    prefix="/api",
    tags=["calculos"]
)

# Modelo Pydantic: define qué datos esperamos recibir
class DatosCalculo(BaseModel):
    """
    Modelo de datos para una petición de cálculo.

    Attributes:
        formula_id (int): ID de la fórmula a calcular
        valores (dict): Diccionario con los parámetros necesarios
                       Ejemplo para MRU: {"x0": 0, "v": 5, "t_min": 0, "t_max": 10}
    """
    formula_id: int
    valores: Dict[str, Any]  # Dict puede contener cualquier tipo de valor


@router.post("/calcular")
def calcular(datos: DatosCalculo):
    """
    Calcula una fórmula matemática, guarda el resultado en BD y lo devuelve.

    Flujo:
    1. Valida que la fórmula existe en la BD
    2. Según el tipo de fórmula, llama a la función de cálculo apropiada
    3. Guarda el cálculo en la tabla 'calculos' (historial)
    4. Devuelve los puntos calculados para que el frontend grafique

    Args:
        datos (DatosCalculo): Objeto validado por Pydantic con formula_id y valores

    Returns:
        dict: {
            "data": {
                "formula": {...},      # Info de la fórmula usada
                "valores": {...},      # Valores que se usaron
                "resultado": {...}     # Puntos calculados (t, x)
            },
            "error": None
        }

    Raises:
        HTTPException 404: Si la fórmula no existe
        HTTPException 400: Si faltan valores requeridos
        HTTPException 500: Si hay error en BD o cálculo
    """
    try:
        # PASO 1: Obtener la fórmula de la base de datos
        formula_response = supabase.table("formulas").select("*").eq("id", datos.formula_id).execute()

        if not formula_response.data:
            return {
                "data": None,
                "error": f"Fórmula con ID {datos.formula_id} no encontrada"
            }

        formula = formula_response.data[0]

        # PASO 2: Calcular según el tipo de fórmula
        # Por ahora solo soportamos MRU, pero la estructura permite añadir más fórmulas
        if formula["tipo"] == "MRU":
            # Verificar que tenemos todos los valores necesarios
            valores_requeridos = ["x0", "v", "t_min", "t_max"]
            for campo in valores_requeridos:
                if campo not in datos.valores:
                    return {
                        "data": None,
                        "error": f"Falta el valor requerido: {campo}"
                    }

            # Llamar a la función de cálculo
            resultado = calcular_mru(
                x0=datos.valores["x0"],
                v=datos.valores["v"],
                t_min=datos.valores["t_min"],
                t_max=datos.valores["t_max"],
                puntos=datos.valores.get("puntos", 100)  # Usar 100 por defecto
            )
        else:
            # Si el tipo de fórmula no está implementado
            return {
                "data": None,
                "error": f"Tipo de fórmula '{formula['tipo']}' no soportado aún"
            }

        # PASO 3: Guardar el cálculo en la tabla 'calculos' (historial)
        calculo_guardado = supabase.table("calculos").insert({
            "formula_id": datos.formula_id,
            "valores": datos.valores,
            "resultado": resultado
        }).execute()

        # PASO 4: Devolver el resultado
        return {
            "data": {
                "formula": {
                    "id": formula["id"],
                    "nombre": formula["nombre"],
                    "tipo": formula["tipo"]
                },
                "valores": datos.valores,
                "resultado": resultado,
                "calculo_id": calculo_guardado.data[0]["id"] if calculo_guardado.data else None
            },
            "error": None
        }

    except Exception as e:
        # Capturar cualquier error inesperado
        return {
            "data": None,
            "error": f"Error al procesar el cálculo: {str(e)}"
        }


# Bloque de prueba (solo se ejecuta si ejecutamos este archivo directamente)
if __name__ == "__main__":
    print("⚠️  Este archivo define rutas de FastAPI.")
    print("   Para probarlo, ejecuta:")
    print("   uvicorn backend.main:app --reload")
    print("   Luego usa curl o Postman para hacer POST a /api/calcular")
```

### Explicación línea por línea:

| Líneas | Qué hacen | Por qué |
|--------|-----------|---------|
| 1-12 | Comentario de cabecera | Documenta qué hace el archivo y cómo se relaciona con otros |
| 14-17 | Imports necesarios | FastAPI para routing, Pydantic para validación, servicios propios |
| 20-23 | Crear router APIRouter | Agrupa los endpoints relacionados con cálculos bajo /api |
| 26-35 | Clase DatosCalculo(BaseModel) | Define y valida automáticamente la estructura de datos que esperamos |
| 38-39 | Decorador @router.post | Registra la función como endpoint POST en /api/calcular |
| 40-75 | Docstring de la función | Documenta qué hace, qué recibe, qué devuelve, qué errores puede lanzar |
| 77 | try: | Captura cualquier error para manejarlo sin romper el servidor |
| 79-81 | Consultar tabla formulas | Obtiene los datos de la fórmula para saber qué tipo es (MRU, etc.) |
| 83-87 | Validar que existe | Si no existe, devolver error descriptivo |
| 92-100 | Validar valores requeridos | Verificar que el usuario envió x0, v, t_min, t_max |
| 103-109 | Llamar a calcular_mru() | Ejecutar el cálculo matemático con los valores del usuario |
| 111-115 | Tipo no soportado | Por si en el futuro hay fórmulas que aún no implementamos |
| 118-122 | Guardar en tabla calculos | Insertar el registro en BD para historial |
| 125-136 | Devolver resultado | Estructura estándar {data: {...}, error: None} |
| 138-142 | Capturar excepciones | Si algo falla, devolver error en formato estándar |

---

## 5.1 HISTORIAL DE CAMBIOS EN EL CÓDIGO

*(Espacio reservado para documentar modificaciones futuras. Por ahora está en su versión inicial.)*

---

## 6. PROBANDO QUE FUNCIONA

### Paso 1: Registrar el router en main.py

Primero necesitamos que FastAPI conozca este nuevo router.

**Modificar `backend/main.py`:**

```diff
 from fastapi import FastAPI
 from backend.routes.formulas import router as formulas_router
+from backend.routes.calculos import router as calculos_router

 app = FastAPI(
     title="API Fórmulas Matemáticas",
     description="Backend para visualización de fórmulas matemáticas y físicas",
     version="0.1.0"
 )

 app.include_router(formulas_router)
+app.include_router(calculos_router)

 @app.get("/health")
 def health_check():
```

### Paso 2: Iniciar el servidor

```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
uvicorn backend.main:app --reload
```

### Paso 3: Probar con curl

```bash
curl -X POST http://localhost:8000/api/calcular \
  -H "Content-Type: application/json" \
  -d '{
    "formula_id": 1,
    "valores": {
      "x0": 0,
      "v": 5,
      "t_min": 0,
      "t_max": 10
    }
  }'
```

### Resultado esperado:

```json
{
  "data": {
    "formula": {
      "id": 1,
      "nombre": "MRU - Movimiento Rectilíneo Uniforme",
      "tipo": "MRU"
    },
    "valores": {
      "x0": 0,
      "v": 5,
      "t_min": 0,
      "t_max": 10
    },
    "resultado": {
      "t": [0.0, 0.101..., 0.202..., ..., 10.0],
      "x": [0.0, 0.505..., 1.010..., ..., 50.0]
    },
    "calculo_id": 1
  },
  "error": null
}
```

### Resultado obtenido:

```json
{
  "data": {
    "formula": {
      "id": 1,
      "nombre": "MRU - Movimiento Rectilíneo Uniforme",
      "categoria": "fisica"
    },
    "valores": {"x0": 0, "v": 5, "t_min": 0, "t_max": 10},
    "resultado": {
      "t": [0.0, 0.101..., 0.202..., ..., 10.0],
      "x": [0.0, 0.505..., 1.010..., ..., 50.0]
    },
    "calculo_id": 2
  },
  "error": null
}
```

---

## 7. ¿FUNCIONÓ?

### ❌ Error #1 - Campo 'tipo' no existe (2025-12-29)

**Qué pasó:**
Primera prueba del endpoint devolvió:
```
{"data":null,"error":"Error al procesar el cálculo: 'tipo'"}
```

**Diagnóstico:**
El código asumía que la tabla `formulas` tenía un campo `tipo`:
```python
if formula["tipo"] == "MRU":  # ❌ Este campo no existe
```

Consulté la fórmula con `curl http://localhost:8000/api/formula/1` y vi que los campos son:
- `id`, `nombre`, `formula_latex`, `variable_rango`, `categoria`, etc.
- **NO hay campo `tipo`**

**Solución aplicada:**
Cambié el código para identificar el tipo de fórmula por su nombre:
```diff
- if formula["tipo"] == "MRU":
+ if "MRU" in formula["nombre"]:  # ✅ Usar el nombre que sí existe
```

También cambié el mensaje de error y la respuesta para usar `categoria` en lugar de `tipo`.

**Lección aprendida:**
- Nunca asumir la estructura de datos en la BD sin verificarla primero
- Consultar la estructura real antes de escribir código
- Es mejor ser flexible y adaptarse a lo que existe que forzar una estructura ideal

---

### ❌ Error #2 - Columna 'valores' no existe (2025-12-29)

**Qué pasó:**
Segunda prueba (después de corregir error #1) devolvió:
```
{"data":null,"error":"Error al procesar el cálculo: {'message': \"Could not find the 'valores' column of 'calculos' in the schema cache\", ...}"}
```

**Diagnóstico:**
El código intentaba insertar en una columna llamada `valores`:
```python
supabase.table("calculos").insert({
    "formula_id": datos.formula_id,
    "valores": datos.valores,  # ❌ Columna no existe
    "resultado": resultado
})
```

Ejecuté un test de inserción simple para ver qué columnas acepta la tabla:
```python
response = supabase.table('calculos').insert({'formula_id': 1}).execute()
print(list(response.data[0].keys()))
```

Resultado:
```
['id', 'formula_id', 'valores_entrada', 'resultado', 'created_at']
```

**La columna se llama `valores_entrada`, no `valores`.**

**Solución aplicada:**
```diff
  calculo_guardado = supabase.table("calculos").insert({
      "formula_id": datos.formula_id,
-     "valores": datos.valores,
+     "valores_entrada": datos.valores,  # ✅ Usar el nombre correcto
      "resultado": resultado
  }).execute()
```

**Lección aprendida:**
- Verificar nombres de columnas exactos en la BD
- Una tabla vacía no muestra su estructura, hacer insert de prueba ayuda
- Los nombres de columnas deben coincidir exactamente (case-sensitive)

---

### ✅ Tercera prueba: ¡ÉXITO!

**Comando ejecutado:**
```bash
curl -X POST http://localhost:8000/api/calcular \
  -H "Content-Type: application/json" \
  -d '{
    "formula_id": 1,
    "valores": {
      "x0": 0,
      "v": 5,
      "t_min": 0,
      "t_max": 10
    }
  }'
```

**Resultado completo:**
```json
{
  "data": {
    "formula": {
      "id": 1,
      "nombre": "MRU - Movimiento Rectilíneo Uniforme",
      "categoria": "fisica"
    },
    "valores": {
      "x0": 0,
      "v": 5,
      "t_min": 0,
      "t_max": 10
    },
    "resultado": {
      "t": [0.0, 0.101..., 0.202..., ..., 10.0],   // 100 puntos
      "x": [0.0, 0.505..., 1.010..., ..., 50.0]    // 100 puntos
    },
    "calculo_id": 2
  },
  "error": null
}
```

**Validaciones exitosas:**

1. ✅ **Cálculo matemático correcto:**
   - Fórmula MRU: x = x₀ + v·t
   - Con x₀=0, v=5, t_max=10: x_final = 0 + 5×10 = 50 ✓
   - Primer punto: t=0, x=0 ✓
   - Último punto: t=10, x=50 ✓

2. ✅ **Guardado en base de datos:**
   - Se creó registro con `calculo_id: 2`
   - Esto significa que el historial se está guardando

3. ✅ **Puntos para graficar:**
   - 100 puntos igualmente espaciados en t
   - 100 puntos calculados en x
   - Formato JSON listo para que el frontend use con Plotly

4. ✅ **Formato de respuesta estándar:**
   - `{"data": {...}, "error": null}`
   - Consistente con otros endpoints del proyecto

5. ✅ **Pydantic validó los datos:**
   - Si enviáramos `formula_id: "texto"` en lugar de número, rechazaría
   - Si faltara `x0`, devolvería error descriptivo

**Siguiente paso:** Tarea 2.3 - Endpoint GET /api/historial para ver cálculos anteriores

---

## 8. RESUMEN

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué construimos? | Endpoint POST /api/calcular que recibe valores, calcula, guarda y devuelve resultado |
| ¿Para qué sirve? | Permite al frontend enviar datos para calcular fórmulas y obtener puntos para graficar |
| ¿Cómo se usa? | POST a /api/calcular con JSON: {formula_id: 1, valores: {x0, v, t_min, t_max}} |
| ¿Con qué se conecta? | Supabase (tablas formulas y calculos) + calculadora.py (función calcular_mru) |

---

## 9. CONEXIÓN CON EL SIGUIENTE PASO

Ahora tenemos:
- ✅ Función de cálculo (calcular_mru)
- ✅ Endpoint para ejecutar cálculos y guardarlos

**Siguiente paso (Tarea 2.3):** Crear endpoint GET /api/historial para que el usuario pueda ver sus cálculos anteriores. Esto completará la Fase 2 del proyecto.

Después (Fase 3): Crear el frontend HTML/JS para que el usuario pueda usar estos endpoints desde el navegador.

---

*Documentación generada por Claude Code siguiendo el método socrático*
*NUNCA borrar contenido de este archivo - solo añadir*
