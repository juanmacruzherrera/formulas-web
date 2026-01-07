# 08 - Endpoint GET /api/historial

> **Archivo(s) modificado(s):** `backend/routes/calculos.py`
> **Fecha:** 2025-12-29
> **Estado:** ✅ Completado (sin errores)

---

## 1. ¿QUÉ VAMOS A HACER?

Vamos a crear un endpoint que devuelva el **historial de cálculos** que el usuario ha realizado. Es como un "registro de actividad" que muestra qué fórmulas calculó, con qué valores, y cuándo.

**Analogía:** Es como el historial de tu navegador web. Puedes ver qué páginas visitaste antes, cuándo, y volver a visitarlas. En nuestro caso, el usuario podrá ver qué cálculos hizo, con qué valores, y potencialmente "rehacer" un cálculo anterior.

---

## 2. ¿POR QUÉ LO NECESITAMOS?

Ya tenemos:
- ✅ Endpoint para calcular y **guardar** resultados (POST /api/calcular)
- ✅ Tabla `calculos` en Supabase que almacena cada cálculo

Pero **falta poder consultar** esos datos guardados. Sin este endpoint:
- El usuario no puede ver qué cálculos hizo antes
- Los datos se guardan pero nunca se usan
- No hay forma de "rehacer" un cálculo con los mismos valores

Con este endpoint:
- El usuario ve su historial completo
- Puede recordar qué valores usó en cálculos anteriores
- El frontend puede mostrar una lista de "cálculos recientes"
- Se aprovecha la funcionalidad de guardado que ya implementamos

---

## 3. ¿CÓMO ENCAJA EN EL PROYECTO?

```
┌──────────────┐
│   FRONTEND   │
│ (HTML/JS)    │
└──────┬───────┘
       │
       │ GET /api/historial
       │ (sin parámetros)
       ▼
┌──────────────────────────────────┐
│        BACKEND (FastAPI)         │
│  ┌────────────────────────────┐  │
│  │  ESTA PIEZA:               │  │
│  │  routes/calculos.py        │  │
│  │  Endpoint GET /historial   │  │
│  └─────────────┬──────────────┘  │
│                │                 │
│                ▼                 │
│        ┌───────────────┐         │
│        │ supabase      │         │
│        │ _client       │         │
│        └───────┬───────┘         │
│                │                 │
└────────────────┼─────────────────┘
                 │
                 ▼
         ┌───────────────┐
         │   SUPABASE    │
         │  ┌─────────┐  │
         │  │calculos │  │
         │  │  (JOIN) │  │
         │  │formulas │  │
         │  └─────────┘  │
         └───────────────┘
```

**Flujo de datos:**
1. Frontend pide GET /api/historial
2. Endpoint consulta tabla `calculos` ordenada por fecha (más recientes primero)
3. Para cada cálculo, obtiene también la info de la fórmula asociada (JOIN o consulta adicional)
4. Limita a los últimos 10-20 registros
5. Devuelve array de cálculos con toda la información

---

## 4. CONCEPTOS PREVIOS

### Concepto 1: Historial y orden cronológico

- **Qué es:**
  Un historial muestra registros ordenados por tiempo, generalmente los más recientes primero.

- **Analogía:**
  - Historial del navegador: última página arriba
  - Feed de redes sociales: publicación más reciente arriba
  - Extracto bancario: movimiento más reciente primero

- **En SQL/Supabase:**
  ```sql
  ORDER BY created_at DESC
  LIMIT 20
  ```
  - `DESC` = descendente (del más nuevo al más viejo)
  - `LIMIT 20` = solo los primeros 20 resultados

### Concepto 2: JOIN entre tablas (relaciones)

- **Qué es:**
  JOIN combina datos de dos tablas relacionadas. En nuestro caso, cada `calculo` está relacionado con una `formula` (por el `formula_id`).

- **Analogía:**
  Tienes dos libretas:
  - **Libreta A (calculos):** "Hice cálculo #1 con fórmula_id=1"
  - **Libreta B (formulas):** "Fórmula id=1 se llama 'MRU'"

  JOIN = "Combina ambas libretas para que en lugar de ver solo 'formula_id=1', veas directamente 'MRU - Movimiento Rectilíneo...'"

- **Dos formas de hacer JOIN en Supabase:**

  **Opción A: JOIN automático (recomendado)**
  ```python
  response = supabase.table("calculos") \
      .select("*, formulas(*)") \
      .execute()
  ```
  Esto trae todos los campos de `calculos` **Y** todos los campos de la fórmula asociada.

  **Opción B: Consultar separado (menos eficiente)**
  ```python
  # Primero obtener cálculos
  calculos = supabase.table("calculos").select("*").execute()

  # Luego para cada cálculo, obtener su fórmula
  for calculo in calculos.data:
      formula = supabase.table("formulas").select("*").eq("id", calculo["formula_id"]).execute()
  ```
  Esto hace N+1 consultas (muy lento si hay muchos registros).

- **Por qué JOIN es mejor:**
  - 1 sola consulta a la base de datos (más rápido)
  - Supabase hace el trabajo pesado
  - Código más limpio

### Concepto 3: LIMIT y paginación

- **Qué es:**
  LIMIT restringe cuántos resultados devuelve la consulta. Es útil para no sobrecargar el frontend con miles de registros.

- **Analogía:**
  Netflix no te muestra todos los 10,000 títulos a la vez. Te muestra los primeros 20, y si quieres más, haces scroll y carga más.

- **En nuestro caso:**
  ```python
  .limit(20)  # Solo los primeros 20 cálculos
  ```

- **Paginación (para el futuro):**
  Si en el futuro queremos "página 2, 3, etc.", usaríamos:
  ```python
  .range(0, 19)    # Primeros 20 (página 1)
  .range(20, 39)   # Siguientes 20 (página 2)
  ```
  Por ahora solo implementaremos los últimos 20.

### Concepto 4: Campos calculados vs campos almacenados

- **Campo almacenado:** Existe físicamente en la base de datos
  - Ejemplo: `id`, `formula_id`, `valores_entrada`, `created_at`

- **Campo calculado:** No existe en la BD, se genera en el código
  - Ejemplo: formatear fecha, combinar campos, extraer resumen

- **En nuestro endpoint:**
  Podríamos querer devolver:
  - `created_at` → Tal cual (almacenado)
  - `fecha_legible` → "Hace 2 horas" (calculado en Python)

---

## 5. EL CÓDIGO

### Modificación en `backend/routes/calculos.py`

Vamos a **añadir** un nuevo endpoint al archivo existente:

```python
@router.get("/historial")
def obtener_historial(limite: int = 20):
    """
    Obtiene el historial de cálculos realizados, ordenados por más recientes primero.

    Args:
        limite (int, optional): Cantidad máxima de cálculos a devolver. Por defecto 20.

    Returns:
        dict: {
            "data": [
                {
                    "id": 1,
                    "formula_id": 1,
                    "valores_entrada": {...},
                    "resultado": {...},
                    "created_at": "2025-12-29T...",
                    "formula": {
                        "id": 1,
                        "nombre": "MRU - ...",
                        "categoria": "fisica"
                    }
                },
                ...
            ],
            "error": None
        }

    Example:
        GET http://localhost:8000/api/historial
        GET http://localhost:8000/api/historial?limite=10
    """
    try:
        # Consultar tabla calculos con JOIN a formulas
        # El asterisco (*) trae todos los campos de calculos
        # formulas(*) hace JOIN y trae todos los campos de la tabla formulas
        response = supabase.table("calculos") \
            .select("*, formulas(*)") \
            .order("created_at", desc=True) \
            .limit(limite) \
            .execute()

        # La respuesta viene con la fórmula anidada en cada cálculo
        # Ejemplo: calculo["formulas"] contiene {id, nombre, categoria, ...}

        return {
            "data": response.data,
            "error": None
        }

    except Exception as e:
        return {
            "data": None,
            "error": f"Error al obtener el historial: {str(e)}"
        }
```

### Explicación línea por línea:

| Líneas | Qué hacen | Por qué |
|--------|-----------|---------|
| `@router.get("/historial")` | Registra endpoint GET en /api/historial | GET porque solo consultamos, no modificamos |
| `def obtener_historial(limite: int = 20):` | Función con parámetro opcional `limite` | Permite al usuario pedir más o menos registros: /api/historial?limite=50 |
| `supabase.table("calculos")` | Selecciona la tabla de cálculos | Punto de partida de la consulta |
| `.select("*, formulas(*)")` | Trae todos campos de calculos + JOIN con formulas | `*` = todos los campos, `formulas(*)` = JOIN con tabla formulas |
| `.order("created_at", desc=True)` | Ordena por fecha de creación, descendente | desc=True → más recientes primero |
| `.limit(limite)` | Limita resultados al valor del parámetro | Evita devolver miles de registros, usa el valor del query param |
| `.execute()` | Ejecuta la consulta | Sin esto, la consulta no se envía a Supabase |
| `return {"data": response.data, ...}` | Devuelve formato estándar | Consistente con otros endpoints |

### Detalles importantes:

**1. Query parameter `limite`:**
```python
def obtener_historial(limite: int = 20):
```
FastAPI automáticamente reconoce esto como query parameter. El usuario puede llamar:
- `/api/historial` → usa límite=20 (por defecto)
- `/api/historial?limite=10` → usa límite=10
- `/api/historial?limite=50` → usa límite=50

**2. El JOIN en Supabase:**
```python
.select("*, formulas(*)")
```

Esto es equivalente a este SQL:
```sql
SELECT calculos.*, formulas.*
FROM calculos
LEFT JOIN formulas ON calculos.formula_id = formulas.id
ORDER BY calculos.created_at DESC
LIMIT 20
```

Pero la sintaxis de Supabase es más compacta. El resultado viene así:
```json
{
  "id": 1,
  "formula_id": 1,
  "valores_entrada": {...},
  "resultado": {...},
  "created_at": "...",
  "formulas": {        // ← Nombre en singular viene del foreign key
    "id": 1,
    "nombre": "MRU - ...",
    "categoria": "fisica"
  }
}
```

**Nota:** Supabase usa el nombre de la relación (foreign key) para anidar. Si la columna se llama `formula_id`, el objeto anidado podría llamarse `formulas` (plural) dependiendo de cómo esté configurada la BD.

---

## 5.1 HISTORIAL DE CAMBIOS EN EL CÓDIGO

### Cambio #1 - 2025-12-29 - Añadir endpoint GET /historial

**Archivo:** `backend/routes/calculos.py`

**Qué añadí:**
```diff
+ @router.get("/historial")
+ def obtener_historial(limite: int = 20):
+     """Obtiene el historial de cálculos realizados..."""
+     try:
+         response = supabase.table("calculos") \
+             .select("*, formulas(*)") \
+             .order("created_at", desc=True) \
+             .limit(limite) \
+             .execute()
+
+         return {
+             "data": response.data,
+             "error": None
+         }
+     except Exception as e:
+         return {
+             "data": None,
+             "error": f"Error al obtener el historial: {str(e)}"
+         }
```

**Por qué lo añadí:**
Para que el usuario pueda consultar los cálculos que ha realizado anteriormente.

**Resultado:**
*(Se completará después de probar)*

---

## 6. PROBANDO QUE FUNCIONA

### Paso 1: El servidor ya debe estar corriendo

Si no está corriendo:
```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
uvicorn backend.main:app --reload
```

### Paso 2: Probar endpoint sin parámetros (límite por defecto)

```bash
curl http://localhost:8000/api/historial
```

### Paso 3: Probar con límite personalizado

```bash
curl http://localhost:8000/api/historial?limite=5
```

### Resultado esperado:

```json
{
  "data": [
    {
      "id": 2,
      "formula_id": 1,
      "valores_entrada": {
        "x0": 0,
        "v": 5,
        "t_min": 0,
        "t_max": 10
      },
      "resultado": {
        "t": [0.0, 0.101..., ..., 10.0],
        "x": [0.0, 0.505..., ..., 50.0]
      },
      "created_at": "2025-12-29T...",
      "formulas": {
        "id": 1,
        "nombre": "MRU - Movimiento Rectilíneo Uniforme",
        "categoria": "fisica",
        "formula_latex": "x = x_0 + v \\cdot t"
      }
    },
    {
      "id": 1,
      "formula_id": 1,
      ...
    }
  ],
  "error": null
}
```

### Resultado obtenido:

**Prueba 1: GET /api/historial (sin parámetros, límite por defecto)**

```json
{
  "data": [
    {
      "id": 2,
      "formula_id": 1,
      "valores_entrada": {"v": 5, "x0": 0, "t_max": 10, "t_min": 0},
      "resultado": {
        "t": [0.0, 0.101..., ..., 10.0],
        "x": [0.0, 0.505..., ..., 50.0]
      },
      "created_at": "2025-12-29T18:16:31.796161+00:00",
      "formulas": {
        "id": 1,
        "nombre": "MRU - Movimiento Rectilíneo Uniforme",
        "categoria": "fisica",
        "formula_latex": "x = x_0 + v \\\\cdot t",
        "variable_rango": "t",
        "rango_min": 0,
        "rango_max": 10,
        "variables_usuario": {"v": 5, "x0": 0}
      }
    },
    {
      "id": 1,
      "formula_id": 1,
      "valores_entrada": null,
      "resultado": null,
      "created_at": "2025-12-29T18:15:59.178889+00:00",
      "formulas": { ... }
    }
  ],
  "error": null
}
```

**Observaciones:**
- ✅ Devuelve 2 registros (todos los cálculos en la BD)
- ✅ Ordenados por fecha DESC: id=2 (18:16:31) primero, id=1 (18:15:59) segundo
- ✅ JOIN exitoso: cada registro tiene objeto `formulas` anidado con toda la info
- ✅ El registro id=1 tiene `valores_entrada: null` (fue el insert de prueba)

**Prueba 2: GET /api/historial?limite=1**

```json
{
  "data": [
    {
      "id": 2,
      "formula_id": 1,
      "valores_entrada": {"v": 5, "x0": 0, "t_max": 10, "t_min": 0},
      "resultado": { ... },
      "created_at": "2025-12-29T18:16:31.796161+00:00",
      "formulas": { ... }
    }
  ],
  "error": null
}
```

**Observaciones:**
- ✅ Solo devuelve 1 registro (el más reciente)
- ✅ Query parameter `limite` funciona correctamente

---

## 7. ¿FUNCIONÓ?

### ✅ Sí, funcionó a la primera

**Validaciones exitosas:**

1. ✅ **Endpoint responde correctamente:**
   - GET /api/historial devuelve status 200
   - Formato JSON válido

2. ✅ **Orden cronológico correcto:**
   - Más recientes primero (DESC)
   - id=2 (18:16:31) antes que id=1 (18:15:59)

3. ✅ **JOIN automático funciona:**
   - Cada registro tiene objeto `formulas` anidado
   - Contiene todos los campos de la tabla formulas
   - 1 sola consulta a BD (eficiente)

4. ✅ **Parámetro `limite` funciona:**
   - Sin parámetro: devuelve todos (en este caso 2)
   - Con `?limite=1`: devuelve solo 1
   - FastAPI reconoce automáticamente el query parameter

5. ✅ **Formato de respuesta estándar:**
   - `{"data": [...], "error": null}`
   - Consistente con otros endpoints

6. ✅ **Información completa:**
   - valores_entrada del cálculo
   - resultado con arrays t y x
   - created_at (timestamp)
   - Info completa de la fórmula (nombre, latex, categoría, etc.)

**Sin errores en esta tarea** - El código funcionó correctamente a la primera. Esto es posible porque:
- Ya teníamos experiencia de las tareas anteriores
- La estructura de Supabase estaba clara
- El patrón de respuesta ya estaba establecido

**Siguiente paso:**

Esto completa la **FASE 2 - Lógica de cálculo** ✅

| Tarea | Estado |
|-------|--------|
| 2.1 - Función calcular_mru | ✅ |
| 2.2 - Endpoint POST /api/calcular | ✅ |
| 2.3 - Endpoint GET /api/historial | ✅ |

**Siguiente fase: FASE 3 - Frontend básico**
- Tarea 3.1: HTML estructura base
- Tarea 3.2: JavaScript para llamar al backend
- Tarea 3.3: Visualización con Plotly
- Tarea 3.4: Estilos CSS

---

## 8. RESUMEN

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué construimos? | Endpoint GET /api/historial que devuelve últimos cálculos con info de fórmulas |
| ¿Para qué sirve? | Permite al usuario ver su historial de cálculos realizados |
| ¿Cómo se usa? | GET a /api/historial (opcionalmente con ?limite=N) |
| ¿Con qué se conecta? | Supabase (tablas calculos y formulas) |

---

## 9. CONEXIÓN CON EL SIGUIENTE PASO

Ahora tenemos **completada la Fase 2 - Lógica de cálculo**:
- ✅ Función de cálculo (calcular_mru)
- ✅ Endpoint para ejecutar cálculos (POST /api/calcular)
- ✅ Endpoint para ver historial (GET /api/historial)

**Backend completo al 100%** (para la fórmula MRU).

**Siguiente fase (Fase 3):** Crear el frontend
- Tarea 3.1: HTML estructura base
- Tarea 3.2: JavaScript para llamar al backend
- Tarea 3.3: Visualización con Plotly (gráficos)
- Tarea 3.4: Estilos CSS

El frontend usará estos endpoints que acabamos de construir para:
1. Listar fórmulas disponibles (GET /api/formulas)
2. Permitir al usuario ingresar valores
3. Enviar el cálculo (POST /api/calcular)
4. Mostrar el gráfico con Plotly
5. Mostrar historial de cálculos (GET /api/historial)

---

*Documentación generada por Claude Code siguiendo el método socrático*
*NUNCA borrar contenido de este archivo - solo añadir*
