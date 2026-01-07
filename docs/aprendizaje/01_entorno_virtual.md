# 01 - Creación del Entorno Virtual e Instalación de Dependencias

> **Archivo(s) creado(s):** `venv/` (directorio), `requirements.txt`
> **Fecha:** 2025-12-29
> **Estado:** ✅ Completado

---

## 1. ¿QUÉ VAMOS A HACER?

Vamos a crear un "entorno virtual" de Python e instalar las librerías que necesitamos para que nuestra aplicación funcione.

Piensa en el entorno virtual como una caja de herramientas específica para este proyecto. Es como tener un maletín de carpintero donde guardas SOLO las herramientas que necesitas para construir una mesa, sin mezclarlas con las herramientas del electricista o del fontanero.

Luego, instalaremos 4 librerías esenciales:
- **FastAPI**: El marco para construir nuestra API (el "backend")
- **Uvicorn**: El servidor que ejecuta FastAPI
- **Supabase**: Para conectarnos a nuestra base de datos
- **Python-dotenv**: Para manejar credenciales de forma segura

---

## 2. ¿POR QUÉ LO NECESITAMOS?

### ¿Por qué un entorno virtual?

Imagina que tienes varios proyectos de Python en tu computadora:
- Proyecto A necesita la versión 1.0 de una librería
- Proyecto B necesita la versión 2.0 de la MISMA librería

Si instalas todo globalmente, tendrás conflictos. El entorno virtual resuelve esto creando un espacio aislado donde cada proyecto tiene sus propias versiones de librerías.

**Beneficios:**
1. **Aislamiento**: No afectas otros proyectos
2. **Reproducibilidad**: Puedes compartir exactamente qué versiones usas
3. **Limpieza**: Si algo sale mal, borras el venv y lo recreas

### ¿Por qué estas librerías?

- **FastAPI**: Necesitamos un framework moderno para crear endpoints HTTP que el frontend pueda llamar
- **Uvicorn**: FastAPI necesita un servidor ASGI para funcionar, Uvicorn es el más recomendado
- **Supabase**: Necesitamos comunicarnos con nuestra base de datos PostgreSQL en Supabase
- **Python-dotenv**: Para leer variables de entorno desde el archivo `.env` (claves secretas)

---

## 3. ¿CÓMO ENCAJA EN EL PROYECTO?

```
┌─────────────────────────────────────────────────┐
│  COMPUTADORA                                    │
│                                                 │
│  ┌───────────────────────────────────────────┐ │
│  │  ENTORNO VIRTUAL (venv/)                  │ │
│  │                                           │ │
│  │  ┌─────────────┐  ┌──────────────┐       │ │
│  │  │   FastAPI   │  │   Supabase   │       │ │
│  │  │   Uvicorn   │  │ python-dotenv│       │ │
│  │  └─────────────┘  └──────────────┘       │ │
│  │         ↓                ↓                │ │
│  │    ┌────────────────────────┐            │ │
│  │    │  Nuestro código Python │            │ │
│  │    │    (backend/)          │            │ │
│  │    └────────────────────────┘            │ │
│  └───────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

**Flujo:**
1. Creamos el entorno virtual → Es el contenedor aislado
2. Instalamos las librerías → Son las herramientas dentro del contenedor
3. Nuestro código usará estas herramientas → El proyecto funciona

**Este es el PRIMER PASO** porque sin estas herramientas instaladas, no podemos escribir código que funcione.

---

## 4. CONCEPTOS PREVIOS

### Concepto 1: Entorno Virtual (venv)

- **Qué es:** Un directorio que contiene una copia de Python y un espacio para instalar librerías de forma aislada.

- **Analogía:** Es como tener una cocina portátil con sus propios utensilios, separada de la cocina principal de la casa. Puedes experimentar ahí sin desordenar la cocina principal.

- **Ejemplo simple:**
  - Sin venv: Instalar librería X versión 1.0 afecta TODOS los proyectos Python
  - Con venv: Cada proyecto tiene su propia copia de la librería, sin interferir

### Concepto 2: pip (Package Installer for Python)

- **Qué es:** El programa que instala librerías de Python desde internet (PyPI - Python Package Index)

- **Analogía:** Es como una tienda de aplicaciones (App Store) pero para librerías de Python

- **Comandos básicos:**
  - `pip install nombre`: Instala una librería
  - `pip list`: Lista librerías instaladas
  - `pip freeze > requirements.txt`: Guarda la lista exacta de versiones

### Concepto 3: requirements.txt

- **Qué es:** Un archivo de texto que lista todas las librerías y sus versiones exactas

- **Analogía:** Es como una lista de ingredientes con cantidades exactas. Si compartes la receta (el proyecto), otros pueden obtener exactamente los mismos ingredientes.

- **Para qué sirve:**
  - Documentar qué necesita el proyecto
  - Permitir que otros instalen todo con un comando: `pip install -r requirements.txt`

### Concepto 4: Activar/Desactivar el entorno

- **Activar:** `source venv/bin/activate` (en Mac/Linux)
  - Indica al terminal "usa el Python y pip de ESTE proyecto"
  - Verás `(venv)` al inicio de la línea del terminal

- **Desactivar:** `deactivate`
  - Vuelve al Python del sistema

---

## 5. LOS COMANDOS

### Paso 1: Navegar al directorio del proyecto
```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
```

**Qué hace:** Nos movemos a la carpeta raíz del proyecto

---

### Paso 2: Crear el entorno virtual
```bash
python3 -m venv venv
```

**Qué hace:**
- `python3 -m venv`: Ejecuta el módulo "venv" de Python
- `venv`: Nombre del directorio donde se creará (por convención se llama "venv")

**Resultado esperado:** Se crea un directorio `venv/` con esta estructura:
```
venv/
├── bin/          ← Contiene python, pip, activate
├── include/      ← Headers de Python
├── lib/          ← Librerías instaladas
└── pyvenv.cfg    ← Configuración
```

---

### Paso 3: Activar el entorno
```bash
source venv/bin/activate
```

**Qué hace:** "Activa" el entorno virtual para que los comandos `python` y `pip` usen las versiones de este proyecto

**Resultado esperado:** El prompt cambia a:
```
(venv) usuario@computadora formulas-web %
```

---

### Paso 4: Instalar las librerías
```bash
pip install fastapi uvicorn supabase python-dotenv
```

**Qué hace:** Descarga e instala las 4 librerías desde PyPI

**Qué instala cada una:**
- `fastapi`: Framework para crear APIs REST modernas
- `uvicorn[standard]`: Servidor ASGI para ejecutar FastAPI
- `supabase`: Cliente de Python para Supabase
- `python-dotenv`: Lee variables de entorno desde archivo .env

**Nota:** `uvicorn` podría instalarse como `uvicorn[standard]` para incluir extras como websockets

---

### Paso 5: Crear requirements.txt
```bash
pip freeze > requirements.txt
```

**Qué hace:**
- `pip freeze`: Lista todas las librerías instaladas con sus versiones exactas
- `>`: Redirige la salida a un archivo
- `requirements.txt`: Nombre del archivo donde se guarda

**Resultado esperado:** Se crea un archivo `requirements.txt` con contenido similar a:
```
annotated-types==0.7.0
anyio==4.8.0
certifi==2024.12.14
click==8.1.8
deprecation==2.1.0
fastapi==0.115.6
gotrue==2.10.3
h11==0.14.0
httpcore==1.0.7
httpx==0.28.1
idna==3.10
packaging==24.2
postgrest==0.19.1
pydantic==2.10.5
pydantic_core==2.27.2
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
realtime==2.0.9
six==1.17.0
sniffio==1.3.1
starlette==0.41.3
storage3==0.9.1
StrEnum==0.4.15
supabase==2.11.1
supafunc==0.7.1
typing_extensions==4.12.2
uvicorn==0.34.0
websockets==14.1
```

---

### Paso 6: Verificar instalación
```bash
pip list | grep fastapi
```

**Qué hace:**
- `pip list`: Lista librerías instaladas
- `|`: Pipe, pasa el resultado al siguiente comando
- `grep fastapi`: Filtra solo líneas que contengan "fastapi"

**Resultado esperado:**
```
fastapi    0.115.6
```

---

## 5.1 HISTORIAL DE CAMBIOS EN EL CÓDIGO

*(Esta sección se llenará si hay modificaciones posteriores)*

---

## 6. PROBANDO QUE FUNCIONA

### Comando para probar:
```bash
# Verificar que venv está activo
which python
# Debe mostrar: /Volumes/Akitio01/Claude_MCP/formulas-web/venv/bin/python

# Verificar librerías instaladas
pip list | grep -E "fastapi|uvicorn|supabase|dotenv"
```

### Resultado esperado:
```
/Volumes/Akitio01/Claude_MCP/formulas-web/venv/bin/python

fastapi         0.115.6
python-dotenv   1.0.1
supabase        2.11.1
uvicorn         0.34.0
```

### Resultado obtenido:
```
/Volumes/Akitio01/Claude_MCP/formulas-web/venv/bin/python3

fastapi            0.128.0
python-dotenv      1.2.1
supabase           2.27.0
supabase-auth      2.27.0
supabase-functions 2.27.0
uvicorn            0.39.0
```

---

## 7. ¿FUNCIONÓ?

### ✅ Si funcionó:

**¡SÍ, TODO FUNCIONÓ CORRECTAMENTE!**

- Confirmamos que:
  1. ✅ El entorno virtual se creó correctamente en `venv/`
  2. ✅ Todas las librerías se instalaron sin errores:
     - fastapi 0.128.0 (versión más reciente que la esperada 0.115.6)
     - uvicorn 0.39.0 (versión más reciente que la esperada 0.34.0)
     - supabase 2.27.0 (versión más reciente que la esperada 2.11.1)
     - python-dotenv 1.2.1 (versión más reciente que la esperada 1.0.1)
  3. ✅ El archivo requirements.txt se generó con 58 dependencias (incluyendo las dependencias de las librerías)
  4. ✅ Python del venv está en la ruta correcta: `/Volumes/Akitio01/Claude_MCP/formulas-web/venv/bin/python3`

**Versiones más nuevas:**
Las versiones instaladas son más recientes que las especificadas en el plan original, lo cual es positivo porque incluyen mejoras y correcciones de seguridad.

- Siguiente paso lógico:
  - **Tarea 1.1:** Crear el cliente de Supabase usando estas librerías

### ❌ Si falló:

#### El error:
```
[Se documentará si ocurre algún error]
```

#### ¿Por qué falló? (Diagnóstico)
- Posible causa 1: ...
- Posible causa 2: ...

#### ¿Cómo lo solucioné?
1. Primero intenté: ... → No funcionó porque...
2. Luego probé: ... → Tampoco porque...
3. Finalmente: ... → ¡Funcionó!

#### Lección aprendida:
*¿Qué aprendimos de este error que nos servirá en el futuro?*

---

## 8. RESUMEN

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué construimos? | Un entorno virtual de Python con las librerías necesarias |
| ¿Para qué sirve? | Aislar las dependencias del proyecto y tener un entorno reproducible |
| ¿Cómo se usa? | Activar con `source venv/bin/activate` antes de trabajar |
| ¿Con qué se conecta? | Es la base para todo el código Python que escribiremos |

---

## 9. CONEXIÓN CON EL SIGUIENTE PASO

Ahora que tenemos nuestro entorno virtual listo con todas las herramientas instaladas, el siguiente paso (Tarea 1.1) es **crear el cliente de Supabase**.

Usaremos la librería `supabase` que acabamos de instalar para conectarnos a nuestra base de datos. Sin este paso previo, no podríamos ni siquiera importar `from supabase import create_client`.

**Analogía del proceso:**
1. ✅ **Acabamos de hacer:** Montar la caja de herramientas (venv + librerías)
2. ⏭️ **Siguiente:** Usar una de esas herramientas (supabase) para abrir la conexión con la base de datos

---

## 10. ACTUALIZACIONES POSTERIORES

*(Se añadirán actualizaciones aquí si hay cambios posteriores)*

---

*Documentación generada por Claude Code siguiendo el método socrático*
*NUNCA borrar contenido de este archivo - solo añadir*
