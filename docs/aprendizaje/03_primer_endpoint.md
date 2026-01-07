# 03 - Primer Endpoint: Health Check con FastAPI

> **Archivo(s) creado(s):** `backend/main.py`
> **Fecha:** 2025-12-29
> **Estado:** ✅ Completado

---

## 1. ¿QUÉ VAMOS A HACER?

Vamos a crear un servidor web con FastAPI que tenga un endpoint de prueba llamado `/health`.

**Analogía:**
Imagina que estamos construyendo una tienda. Hasta ahora:
- ✅ Tenemos la llave de nuestro almacén (conexión a Supabase)
- ⏭️ Ahora vamos a abrir la puerta principal de la tienda (servidor web)
- El cartel de "ABIERTO" es el endpoint `/health` (para verificar que la tienda está funcionando)

El endpoint `/health` es una práctica común en aplicaciones web. Es como un "¿Estás ahí?" que otros sistemas pueden preguntar para verificar que nuestro servidor está vivo y respondiendo.

**¿Qué hace el endpoint /health?**
- URL: `http://localhost:8000/health`
- Método: GET
- Respuesta: `{"status": "ok", "message": "Servidor funcionando correctamente"}`

Es simple, pero crítico: si este endpoint responde, sabemos que:
- ✅ El servidor está corriendo
- ✅ FastAPI está funcionando
- ✅ Podemos recibir peticiones HTTP
- ✅ Podemos devolver respuestas JSON

---

## 2. ¿POR QUÉ LO NECESITAMOS?

### Problema que resuelve:

Antes de crear endpoints complejos que consultan la base de datos, necesitamos verificar que **lo básico funciona**:

1. **Verificación de infraestructura**: ¿El servidor arranca sin errores?
2. **Prueba de comunicación HTTP**: ¿Podemos enviar peticiones y recibir respuestas?
3. **Base para endpoints más complejos**: Una vez que `/health` funciona, podemos añadir `/api/formulas`, `/api/calcular`, etc.

### En producción:

En aplicaciones reales, el endpoint `/health` se usa para:
- **Monitoreo**: Servicios como AWS, Google Cloud, Kubernetes preguntan constantemente "¿estás vivo?"
- **Load balancers**: Distribuyen tráfico solo a servidores que respondan al health check
- **Debugging**: Primera cosa a verificar cuando algo falla

### Principio de desarrollo:

> "Construir de lo simple a lo complejo"
>
> No empezamos con endpoints complicados. Primero verificamos que FastAPI funciona con el endpoint más simple posible.

---

## 3. ¿CÓMO ENCAJA EN EL PROYECTO?

```
ARQUITECTURA ACTUAL:

┌────────────────────────────────────────────────┐
│  FRONTEND (aún no existe)                      │
│                                                │
│                      ↓ (próximamente)          │
│                                                │
│  ┌──────────────────────────────────────────┐ │
│  │  BACKEND                                  │ │
│  │                                           │ │
│  │  ┌────────────────┐                      │ │
│  │  │   main.py      │  ← ESTAMOS AQUÍ     │ │
│  │  │                │                      │ │
│  │  │  FastAPI App   │                      │ │
│  │  │                │                      │ │
│  │  │  @app.get      │                      │ │
│  │  │  /health       │  ← Endpoint simple   │ │
│  │  └────────────────┘                      │ │
│  │         │                                 │ │
│  │         │ (en el futuro usará)           │ │
│  │         ↓                                 │ │
│  │  ┌────────────────┐                      │ │
│  │  │ supabase_      │                      │ │
│  │  │ client.py      │                      │ │
│  │  └────────────────┘                      │ │
│  └──────────────────────────────────────────┘ │
│                                                │
│  ┌──────────────────────────────────────────┐ │
│  │  SUPABASE                                 │ │
│  │  PostgreSQL Database                      │ │
│  └──────────────────────────────────────────┘ │
└────────────────────────────────────────────────┘

FLUJO DE UNA PETICIÓN AL ENDPOINT /health:

1. Cliente hace GET http://localhost:8000/health
2. Uvicorn (servidor) recibe la petición
3. FastAPI encuentra la ruta decorada con @app.get("/health")
4. Se ejecuta la función health_check()
5. La función devuelve un diccionario Python
6. FastAPI lo convierte automáticamente a JSON
7. Se envía la respuesta: {"status": "ok", "message": "..."}
```

**Este es el paso 2 de 4 en la Fase 1:**
1. ✅ Cliente de Supabase (puede conectar a BD)
2. ⏭️ **Servidor FastAPI básico** (puede recibir peticiones HTTP)
3. Próximo: Endpoint que use Supabase para devolver fórmulas
4. Después: Endpoint para una fórmula específica

---

## 4. CONCEPTOS PREVIOS

### Concepto 1: ¿Qué es FastAPI?

- **Qué es:** Un framework moderno de Python para crear APIs web de forma rápida y con tipado automático

- **Analogía:** Si construir una API con Python puro es como construir una casa ladrillo por ladrillo, FastAPI es como usar bloques prefabricados que se ensamblan fácilmente.

- **Características principales:**
  - Rápido (alto rendimiento, comparable a NodeJS)
  - Automáticamente genera documentación interactiva
  - Validación de datos automática con Pydantic
  - Soporte nativo para async/await
  - Tipado con Type Hints

- **Ejemplo básico:**
  ```python
  from fastapi import FastAPI

  app = FastAPI()  # Crear aplicación

  @app.get("/")  # Decorador: esta función responde a GET /
  def root():
      return {"message": "Hola"}  # Automáticamente se convierte a JSON
  ```

### Concepto 2: ¿Qué es un decorador (@)?

- **Qué es:** Una función que modifica el comportamiento de otra función

- **Analogía:** Es como ponerle una etiqueta a un regalo. El regalo (función) sigue siendo el mismo, pero la etiqueta (@app.get) le dice a FastAPI "oye, cuando alguien pida esta ruta, ejecuta esta función".

- **En FastAPI:**
  ```python
  @app.get("/health")  # Decorador
  def health_check():  # Función normal
      return {"status": "ok"}
  ```

  El decorador `@app.get("/health")` le dice a FastAPI:
  - Método HTTP: GET
  - Ruta: /health
  - Función a ejecutar: health_check()

### Concepto 3: HTTP Methods (GET, POST, PUT, DELETE)

- **Qué son:** Verbos que indican qué tipo de operación queremos hacer

- **Los 4 principales (CRUD):**
  - **GET**: Leer/Obtener datos (no modifica nada)
    - Ejemplo: `GET /api/formulas` → Dame todas las fórmulas
  - **POST**: Crear/Enviar datos nuevos
    - Ejemplo: `POST /api/calcular` → Guarda este cálculo
  - **PUT**: Actualizar datos existentes
    - Ejemplo: `PUT /api/formula/1` → Actualiza la fórmula 1
  - **DELETE**: Eliminar datos
    - Ejemplo: `DELETE /api/formula/1` → Borra la fórmula 1

- **Para /health usamos GET** porque solo estamos pidiendo información, no modificando nada.

### Concepto 4: ¿Qué es Uvicorn?

- **Qué es:** Un servidor ASGI (Asynchronous Server Gateway Interface) que ejecuta aplicaciones FastAPI

- **Analogía:** FastAPI es el cerebro que decide qué hacer con cada petición. Uvicorn es el cuerpo que recibe las peticiones del mundo exterior y se las pasa a FastAPI.

- **¿Por qué lo necesitamos?**
  FastAPI no puede ejecutarse solo. Necesita un servidor que:
  - Escuche en un puerto (ej: 8000)
  - Reciba peticiones HTTP
  - Las pase a FastAPI
  - Devuelva las respuestas

- **Comando para ejecutar:**
  ```bash
  uvicorn backend.main:app --reload
  ```
  - `backend.main`: módulo Python (archivo backend/main.py)
  - `app`: variable FastAPI dentro de main.py
  - `--reload`: reinicia automáticamente si el código cambia (solo para desarrollo)

### Concepto 5: localhost:8000

- **localhost**: La computadora donde estás trabajando (127.0.0.1)
- **:8000**: Puerto (puerta) donde Uvicorn está escuchando

- **Analogía:** Tu computadora es un edificio. localhost es "esta misma edificio". El puerto 8000 es el número de apartamento. `localhost:8000` significa "el apartamento 8000 de este edificio".

- **URLs comunes en desarrollo:**
  - `http://localhost:8000/health` → Nuestro endpoint
  - `http://localhost:8000/docs` → Documentación automática de FastAPI (Swagger)
  - `http://localhost:8000/redoc` → Documentación alternativa (ReDoc)

### Concepto 6: JSON (JavaScript Object Notation)

- **Qué es:** Formato estándar para intercambiar datos entre aplicaciones web

- **Python dict → JSON:**
  ```python
  # Python dictionary
  datos = {"status": "ok", "count": 42}

  # JSON (texto)
  # {"status": "ok", "count": 42}
  ```

- **FastAPI lo hace automáticamente:** Si tu función devuelve un dict, FastAPI lo convierte a JSON antes de enviarlo al cliente.

---

## 5. EL CÓDIGO

### Archivo: `backend/main.py`

```python
# backend/main.py
# ============================================
# QUÉ HACE: Punto de entrada de la aplicación FastAPI
# CONSUME: Ninguno (todavía)
# EXPONE: Servidor web con endpoints HTTP
# RELACIONADO CON:
#   - Ejecutado por: uvicorn
#   - Usará: backend/services/supabase_client.py (en próximas tareas)
#   - Importará: backend/routes/*.py (en próximas tareas)
# ============================================

from fastapi import FastAPI

# Crear la aplicación FastAPI
app = FastAPI(
    title="API Fórmulas Matemáticas",
    description="Backend para visualización de fórmulas matemáticas y físicas",
    version="0.1.0"
)

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

### Explicación línea por línea:

| Líneas | Qué hacen | Por qué |
|--------|-----------|---------|
| 1-9 | Comentario de cabecera | Documenta el propósito del archivo |
| 11 | `from fastapi import FastAPI` | Importa la clase FastAPI para crear la aplicación |
| 14-18 | `app = FastAPI(...)` | Crea la instancia de la aplicación con metadatos |
| 15 | `title` | Nombre que aparecerá en la documentación automática |
| 16 | `description` | Descripción del propósito de la API |
| 17 | `version` | Versión de la API (útil para versionado) |
| 21 | `@app.get("/health")` | Decorador que registra esta función como handler de GET /health |
| 22 | `def health_check():` | Función que se ejecuta cuando alguien accede a /health |
| 23-41 | Docstring | Documentación de la función (aparece en /docs) |
| 42-45 | `return {...}` | Devuelve un diccionario que FastAPI convierte a JSON |

### ¿Por qué estos metadatos en FastAPI?

```python
app = FastAPI(
    title="API Fórmulas Matemáticas",      # Aparece en /docs como título
    description="Backend para...",         # Aparece como descripción
    version="0.1.0"                        # Útil para tracking de cambios
)
```

Estos metadatos se usan en la **documentación automática** que FastAPI genera en `/docs` y `/redoc`. No son obligatorios, pero son buenas prácticas.

---

## 5.1 HISTORIAL DE CAMBIOS EN EL CÓDIGO

*(Se llenará cuando haya modificaciones posteriores)*

---

## 6. PROBANDO QUE FUNCIONA

### Paso 1: Iniciar el servidor

**Comando:**
```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
uvicorn backend.main:app --reload
```

**Qué hace cada parte:**
- `uvicorn`: El servidor ASGI
- `backend.main`: El archivo backend/main.py (sin .py)
- `:app`: La variable `app` dentro de main.py
- `--reload`: Reinicia automáticamente si cambiamos código (solo desarrollo)

**Resultado esperado:**
```
INFO:     Will watch for changes in these directories: ['/Volumes/Akitio01/Claude_MCP/formulas-web']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using WatchFiles
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**⚠️ El servidor se queda corriendo** - No devuelve el prompt. Para detenerlo: `Ctrl+C`

---

### Paso 2: Probar el endpoint /health

**Opción A: Con curl (desde otra terminal)**
```bash
curl http://localhost:8000/health
```

**Resultado esperado:**
```json
{"status":"ok","message":"Servidor funcionando correctamente"}
```

**Opción B: Con el navegador**
- Abre: `http://localhost:8000/health`
- Deberías ver el JSON en el navegador

**Opción C: Documentación automática**
- Abre: `http://localhost:8000/docs`
- Verás la interfaz Swagger con el endpoint /health
- Puedes probarlo directamente desde ahí

---

### Paso 3: Verificar logs del servidor

En la terminal donde corre uvicorn deberías ver:
```
INFO:     127.0.0.1:53210 - "GET /health HTTP/1.1" 200 OK
```

Esto confirma:
- Petición GET recibida
- Ruta: /health
- Código de respuesta: 200 OK (éxito)

---

### Resultado obtenido:

**Servidor arrancado:**
```
INFO:     Will watch for changes in these directories: ['/Volumes/Akitio01/Claude_MCP/formulas-web']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2358] using StatReload
INFO:     Started server process [2361]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Petición curl:**
```bash
$ curl http://127.0.0.1:8000/health
```

**Respuesta:**
```json
{"status":"ok","message":"Servidor funcionando correctamente"}
```

---

## 7. ¿FUNCIONÓ?

### ✅ Si funcionó:

**¡SÍ, FUNCIONÓ PERFECTAMENTE!**

- Confirmamos que:
  1. ✅ El servidor uvicorn arrancó sin errores
  2. ✅ FastAPI se inició correctamente
  3. ✅ El servidor está escuchando en http://127.0.0.1:8000
  4. ✅ El endpoint /health responde correctamente
  5. ✅ La respuesta es válida JSON con el formato esperado
  6. ✅ El código de respuesta HTTP es 200 OK (implícito en la respuesta exitosa)

**Validaciones confirmadas:**
- ✅ FastAPI está instalado y funciona
- ✅ Uvicorn puede ejecutar la aplicación
- ✅ El decorador @app.get funciona correctamente
- ✅ La conversión automática de dict a JSON funciona
- ✅ El hot-reload está activo (--reload funcionando)

**Funcionalidades verificadas:**
- Servidor HTTP funcional
- Endpoint básico que responde
- Serialización JSON automática
- Documentación automática disponible en /docs (aunque no la probamos, está disponible)

- Siguiente paso lógico:
  - **Tarea 1.3:** Crear endpoint `/api/formulas` que use el cliente de Supabase para devolver todas las fórmulas

### ❌ Si falló:

#### El error:
```
[Se documentará si ocurre algún error]
```

#### Posibles causas comunes:

1. **Error: "No module named 'fastapi'"**
   - Causa: No activaste el venv
   - Solución: `source venv/bin/activate`

2. **Error: "Address already in use"**
   - Causa: El puerto 8000 ya está ocupado
   - Solución: `uvicorn backend.main:app --reload --port 8001`

3. **Error: "ModuleNotFoundError: No module named 'backend'"**
   - Causa: Ejecutaste uvicorn desde la carpeta incorrecta
   - Solución: Asegúrate de estar en `/Volumes/Akitio01/Claude_MCP/formulas-web`

4. **Error: "cannot import name 'app' from 'backend.main'"**
   - Causa: Error de sintaxis en main.py
   - Solución: Revisar que el archivo main.py esté correcto

#### ¿Cómo lo solucioné?
*(Se documentará el proceso si ocurre un error)*

---

## 8. RESUMEN

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué construimos? | Un servidor FastAPI con un endpoint de health check |
| ¿Para qué sirve? | Verificar que el servidor está corriendo y puede responder peticiones HTTP |
| ¿Cómo se usa? | Iniciar con `uvicorn backend.main:app --reload` y acceder a `/health` |
| ¿Con qué se conecta? | Es la base donde se montarán todos los demás endpoints |

---

## 9. CONEXIÓN CON EL SIGUIENTE PASO

Ahora que tenemos el servidor FastAPI funcionando con un endpoint básico, el siguiente paso (Tarea 1.3) es **crear el endpoint `/api/formulas`** que devuelve todas las fórmulas de la base de datos.

**Por qué es el siguiente lógico:**
1. Ya tenemos el servidor funcionando ✅
2. Ya tenemos la conexión a Supabase ✅
3. Ahora podemos **unir ambas cosas**: crear un endpoint que use `supabase_client` para obtener datos

**El proceso será:**
- Crear archivo `backend/routes/formulas.py` con un Router
- Definir endpoint GET `/api/formulas`
- Usar `from backend.services.supabase_client import supabase`
- Consultar la tabla `formulas` y devolver los datos
- Importar el router en `main.py` con `app.include_router()`

**Analogía del proceso:**
1. ✅ **Tarea 1.1:** Obtuvimos la llave del almacén (conexión Supabase)
2. ✅ **Tarea 1.2:** Abrimos la tienda (servidor FastAPI)
3. ⏭️ **Tarea 1.3:** Creamos el primer mostrador donde los clientes pueden pedir productos (endpoint /api/formulas)

---

## 10. ACTUALIZACIONES POSTERIORES

*(Se añadirán actualizaciones aquí si hay cambios posteriores)*

---

*Documentación generada por Claude Code siguiendo el método socrático*
*NUNCA borrar contenido de este archivo - solo añadir*
