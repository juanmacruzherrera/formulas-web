# 02 - Conexión con Supabase desde Python

> **Archivo(s) creado(s):** `backend/services/supabase_client.py`, `backend/__init__.py`, `backend/services/__init__.py`
> **Fecha:** 2025-12-29
> **Estado:** ✅ Completado

---

## 1. ¿QUÉ VAMOS A HACER?

Vamos a crear un archivo de Python que conecte nuestra aplicación con la base de datos de Supabase.

**Analogía:**
Imagina que Supabase es una biblioteca gigante donde guardamos nuestras fórmulas matemáticas. Este archivo que vamos a crear es como obtener una tarjeta de biblioteca que nos permite:
- Entrar a la biblioteca (conectarnos)
- Leer los libros (consultar las fórmulas)
- Añadir nuevos libros (guardar cálculos)

Para obtener la tarjeta, necesitamos dos cosas:
1. **La dirección de la biblioteca** (SUPABASE_URL)
2. **Nuestra credencial de acceso** (SUPABASE_KEY)

Estas dos cosas las tenemos guardadas de forma segura en el archivo `.env`.

---

## 2. ¿POR QUÉ LO NECESITAMOS?

### Problema que resuelve:

Sin esta conexión, nuestro backend de Python no tiene forma de:
- Leer las fórmulas que están en Supabase
- Guardar los cálculos que hagan los usuarios
- Recuperar el historial de cálculos

**Es el puente entre Python y la base de datos.**

### ¿Por qué no poner las credenciales directamente en el código?

```python
# ❌ MAL - Credenciales expuestas
supabase = create_client(
    "https://qfeatlcnilhqjcacniih.supabase.co",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
)
```

Problemas:
- Si subimos el código a GitHub, todos ven nuestras claves secretas
- Si cambiamos las claves, hay que editar el código
- Es inseguro

```python
# ✅ BIEN - Credenciales en archivo .env
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)
```

Ventajas:
- El archivo `.env` NO se sube a GitHub (está en `.gitignore`)
- Las claves están separadas del código
- Podemos cambiar credenciales sin tocar el código

---

## 3. ¿CÓMO ENCAJA EN EL PROYECTO?

```
┌──────────────────────────────────────────────────┐
│  ARQUITECTURA COMPLETA                            │
│                                                   │
│  ┌─────────────┐         ┌─────────────┐         │
│  │  Frontend   │         │   Backend   │         │
│  │  HTML + JS  │────────▶│   FastAPI   │         │
│  └─────────────┘  HTTP   └──────┬──────┘         │
│                                  │                │
│                                  │ Usa            │
│                            ┌─────▼──────┐        │
│                            │ ESTE ARCHIVO│        │
│                            │  supabase_  │        │
│                            │  client.py  │        │
│                            └─────┬──────┘        │
│                                  │                │
│                                  │ Conecta con    │
│                            ┌─────▼──────┐        │
│                            │  Supabase  │        │
│                            │ PostgreSQL │        │
│                            └────────────┘        │
└──────────────────────────────────────────────────┘

FLUJO:
1. Usuario pide "dame las fórmulas"
2. Frontend envía petición HTTP a Backend
3. Backend usa supabase_client.py para consultar
4. supabase_client.py se conecta a Supabase
5. Supabase devuelve las fórmulas
6. Backend las envía al Frontend
7. Frontend las muestra
```

**Posición en el proyecto:**
- Es el archivo MÁS BÁSICO del backend
- TODOS los demás archivos lo importarán para acceder a la BD
- Es la "puerta de entrada" a los datos

---

## 4. CONCEPTOS PREVIOS

### Concepto 1: Variables de entorno

- **Qué es:** Valores que existen fuera del código, en el sistema operativo

- **Analogía:** Son como post-its pegados en tu escritorio. No están dentro de tu cuaderno (código), pero puedes mirarlos cuando los necesites.

- **En Python:**
  ```python
  import os

  # Leer una variable de entorno
  valor = os.getenv("NOMBRE_VARIABLE")
  ```

- **Con python-dotenv:**
  ```python
  from dotenv import load_dotenv
  import os

  load_dotenv()  # Lee el archivo .env y carga las variables

  url = os.getenv("SUPABASE_URL")  # Ahora puede leerlas
  ```

### Concepto 2: Cliente de API

- **Qué es:** Un objeto/clase que sabe cómo comunicarse con un servicio externo (API)

- **Analogía:** Es como un traductor. Tú hablas en Python, el traductor (cliente) convierte tu petición al idioma que entiende Supabase (HTTP/REST), y te devuelve la respuesta traducida.

- **En nuestro caso:**
  ```python
  from supabase import create_client

  # Creamos el "traductor"
  supabase = create_client(url, key)

  # Usamos el traductor para pedir datos
  # (Internamente hace peticiones HTTP, pero nosotros no vemos eso)
  response = supabase.table("formulas").select("*").execute()
  ```

### Concepto 3: Singleton pattern (patrón de diseño)

- **Qué es:** Crear UN SOLO objeto que se reutiliza en toda la aplicación

- **Analogía:** En una oficina, hay UNA SOLA impresora que todos usan. No tiene sentido que cada persona tenga su propia impresora conectada a la misma red.

- **En este archivo:**
  ```python
  # Creamos UNA SOLA conexión con Supabase
  supabase: Client = create_client(url, key)

  # Otros archivos importan esta misma instancia
  from backend.services.supabase_client import supabase
  ```

### Concepto 4: Type hints en Python

- **Qué es:** Indicaciones opcionales sobre qué tipo de dato es una variable

- **Ejemplo:**
  ```python
  # Sin type hint
  nombre = "Juan"

  # Con type hint
  nombre: str = "Juan"

  # Para funciones
  def sumar(a: int, b: int) -> int:
      return a + b
  ```

- **Beneficio:** Los editores de código pueden ayudarte mejor (autocompletado, detectar errores)

### Concepto 5: `if __name__ == "__main__"`

- **Qué es:** Código que solo se ejecuta si ejecutas el archivo DIRECTAMENTE, no cuando lo importas

- **Analogía:** Es como una sección de "pruebas" en un manual de instrucciones. Solo la lees si quieres probar el dispositivo, no forma parte del uso normal.

- **Ejemplo:**
  ```python
  # supabase_client.py

  supabase = create_client(url, key)  # Esto SIEMPRE se ejecuta

  if __name__ == "__main__":
      # Esto SOLO se ejecuta si haces: python supabase_client.py
      test_conexion()  # Función de prueba
  ```

---

## 5. EL CÓDIGO

### Estructura de archivos a crear:

```
backend/
├── __init__.py           ← Archivo vacío (indica que backend es un módulo)
└── services/
    ├── __init__.py       ← Archivo vacío (indica que services es un módulo)
    └── supabase_client.py  ← ESTE es el archivo principal
```

### Archivo: `backend/services/supabase_client.py`

```python
# backend/services/supabase_client.py
# ============================================
# QUÉ HACE: Crea y exporta el cliente de Supabase
# CONSUME: Variables de entorno (.env)
# EXPONE: Objeto 'supabase' para usar en otros archivos
# RELACIONADO CON:
#   - Usado por: routes/formulas.py, routes/calculos.py
#   - Depende de: .env
# ============================================

import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener credenciales desde variables de entorno
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

# Validar que las credenciales existen
if not url or not key:
    raise ValueError(
        "❌ Error: Falta SUPABASE_URL o SUPABASE_KEY en el archivo .env\n"
        "Asegúrate de que el archivo .env existe y tiene estas variables."
    )

# Crear el cliente de Supabase (singleton)
supabase: Client = create_client(url, key)

# Función de prueba para verificar la conexión
def test_conexion():
    """
    Función de prueba que verifica la conexión con Supabase.
    Intenta obtener todas las fórmulas de la tabla 'formulas'.

    Returns:
        list: Lista de fórmulas si la conexión es exitosa

    Raises:
        Exception: Si hay error en la conexión
    """
    try:
        # Intentar leer la tabla 'formulas'
        response = supabase.table("formulas").select("*").execute()

        # Mostrar resultado
        print(f"✅ Conexión exitosa con Supabase")
        print(f"📊 Fórmulas encontradas: {len(response.data)}")

        # Mostrar las fórmulas encontradas
        if response.data:
            print("\n📋 Fórmulas en la base de datos:")
            for formula in response.data:
                print(f"   - ID: {formula['id']} | {formula['nombre']} | {formula['categoria']}")

        return response.data

    except Exception as e:
        print(f"❌ Error al conectar con Supabase: {str(e)}")
        raise

# Este bloque solo se ejecuta si ejecutamos este archivo directamente
# No se ejecuta cuando importamos el módulo en otros archivos
if __name__ == "__main__":
    print("🔍 Probando conexión con Supabase...")
    test_conexion()
```

### Explicación línea por línea:

| Líneas | Qué hacen | Por qué |
|--------|-----------|---------|
| 1-9 | Comentario de cabecera | Documenta qué hace el archivo, qué consume y qué expone |
| 11-13 | Importar librerías necesarias | `os` para variables de entorno, `dotenv` para leer .env, `supabase` para crear el cliente |
| 16 | `load_dotenv()` | Lee el archivo `.env` y carga sus variables en el entorno del sistema |
| 19-20 | Obtener credenciales | Lee SUPABASE_URL y SUPABASE_KEY del entorno (ahora disponibles gracias a load_dotenv) |
| 23-27 | Validación de credenciales | Si falta alguna credencial, lanza error claro en lugar de fallar después con mensaje confuso |
| 30 | Crear cliente de Supabase | Esta es la línea clave: crea el objeto que usaremos para todo |
| 30 (type hint) | `: Client` | Indica que `supabase` es del tipo Client (ayuda al editor de código) |
| 33-59 | Función test_conexion() | Función que prueba si la conexión funciona consultando la tabla formulas |
| 39 | `supabase.table("formulas")` | Selecciona la tabla "formulas" |
| 39 | `.select("*")` | Pide todos los campos (equivale a SELECT * en SQL) |
| 39 | `.execute()` | Ejecuta la consulta y devuelve el resultado |
| 42-52 | Mostrar resultado exitoso | Imprime mensaje de éxito y lista las fórmulas encontradas |
| 54-57 | Captura de errores | Si algo falla, muestra el error de forma clara |
| 62-64 | Bloque if __name__ | Solo ejecuta test_conexion() si ejecutamos este archivo directamente |

---

## 5.1 HISTORIAL DE CAMBIOS EN EL CÓDIGO

*(Se llenará cuando haya modificaciones posteriores)*

---

## 6. PROBANDO QUE FUNCIONA

### Comando para probar:
```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
python backend/services/supabase_client.py
```

**Qué hace cada línea:**
- `cd ...`: Nos movemos a la carpeta del proyecto
- `source venv/bin/activate`: Activamos el entorno virtual
- `python backend/services/supabase_client.py`: Ejecutamos el archivo directamente

### Resultado esperado:
```
🔍 Probando conexión con Supabase...
✅ Conexión exitosa con Supabase
📊 Fórmulas encontradas: 1

📋 Fórmulas en la base de datos:
   - ID: 1 | MRU (Movimiento Rectilíneo Uniforme) | Cinemática
```

### Resultado obtenido:
```
🔍 Probando conexión con Supabase...
✅ Conexión exitosa con Supabase
📊 Fórmulas encontradas: 1

📋 Fórmulas en la base de datos:
   - ID: 1 | MRU - Movimiento Rectilíneo Uniforme | fisica
```

**Nota:** Apareció un warning sobre urllib3/OpenSSL, pero es solo informativo y no afecta la funcionalidad. El warning indica que urllib3 v2 recomienda OpenSSL 1.1.1+, pero el sistema usa LibreSSL 2.8.3. Esto es común en macOS y no impide que la conexión funcione correctamente.

---

## 7. ¿FUNCIONÓ?

### ✅ Si funcionó:

**¡SÍ, FUNCIONÓ PERFECTAMENTE!**

- Confirmamos que:
  1. ✅ El archivo `.env` se leyó correctamente con las credenciales
  2. ✅ El cliente de Supabase se creó sin errores
  3. ✅ La conexión con la base de datos se estableció exitosamente
  4. ✅ Se pudieron leer los datos de la tabla `formulas`
  5. ✅ Se recuperó correctamente la fórmula MRU:
     - ID: 1
     - Nombre: "MRU - Movimiento Rectilíneo Uniforme"
     - Categoría: "fisica"

**Observaciones:**
- Apareció un warning sobre urllib3/OpenSSL que es informativo y no afecta la funcionalidad
- El código funcionó a la primera, sin errores
- La función `test_conexion()` demostró que la conexión es estable

**Qué validamos:**
- ✅ Las credenciales de `.env` son correctas
- ✅ La librería `supabase` está instalada y funciona
- ✅ La tabla `formulas` existe en Supabase
- ✅ Tenemos permisos para leer la tabla
- ✅ El patrón singleton funciona (un solo cliente reutilizable)

- Siguiente paso lógico:
  - **Tarea 1.2:** Crear el servidor FastAPI con endpoint `/health` para verificar que el servidor funciona

### ❌ Si falló:

#### El error:
```
[Se documentará si ocurre algún error]
```

#### ¿Por qué falló? (Diagnóstico)

**Posibles causas comunes:**

1. **Error: "No such file or directory: .env"**
   - Causa: El archivo .env no existe
   - Solución: Verificar que .env está en la raíz del proyecto

2. **Error: "Falta SUPABASE_URL o SUPABASE_KEY"**
   - Causa: El .env existe pero no tiene las variables
   - Solución: Verificar que .env tiene estas líneas:
     ```
     SUPABASE_URL=https://...
     SUPABASE_KEY=eyJhbG...
     ```

3. **Error de autenticación/permisos**
   - Causa: La SUPABASE_KEY no es correcta o no tiene permisos
   - Solución: Verificar la key en el dashboard de Supabase

4. **Error: "No module named 'supabase'"**
   - Causa: No se instaló la librería supabase
   - Solución: `pip install supabase`

#### ¿Cómo lo solucioné?
*(Se documentará el proceso si ocurre un error)*

#### Lección aprendida:
*¿Qué aprendimos de este error que nos servirá en el futuro?*

---

## 8. RESUMEN

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué construimos? | Un cliente de Supabase que conecta Python con la base de datos |
| ¿Para qué sirve? | Permite leer y escribir datos en Supabase desde nuestro backend |
| ¿Cómo se usa? | Otros archivos lo importan: `from backend.services.supabase_client import supabase` |
| ¿Con qué se conecta? | Lee credenciales de .env y se conecta a Supabase PostgreSQL |

---

## 9. CONEXIÓN CON EL SIGUIENTE PASO

Ahora que tenemos la conexión con Supabase lista, el siguiente paso (Tarea 1.2) es **crear el servidor FastAPI con un endpoint de prueba (health check)**.

**Por qué es el siguiente lógico:**
1. Ya tenemos la conexión a la BD ✅
2. Ahora necesitamos un servidor web que reciba peticiones HTTP
3. El endpoint /health nos permitirá verificar que el servidor funciona
4. Una vez que tengamos el servidor, podremos crear endpoints que usen `supabase_client` para devolver las fórmulas

**Analogía del proceso:**
1. ✅ **Acabamos de hacer:** Obtener la tarjeta de la biblioteca (conexión a Supabase)
2. ⏭️ **Siguiente:** Abrir la recepción de la biblioteca (servidor FastAPI)
3. Luego: Crear un mostrador donde la gente puede pedir libros (endpoint /api/formulas)

---

## 10. ACTUALIZACIONES POSTERIORES

*(Se añadirán actualizaciones aquí si hay cambios posteriores)*

---

*Documentación generada por Claude Code siguiendo el método socrático*
*NUNCA borrar contenido de este archivo - solo añadir*
