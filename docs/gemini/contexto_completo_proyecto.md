# Contexto Completo del Proyecto - Formulas Web
**Generado:** 2026-01-08 20:18:01
**Para:** Google AI Studio (Gemini 2.0)
**Proyecto:** Visualizador de Fórmulas Matemáticas y Físicas

---

## 📋 INFORMACIÓN DEL PROYECTO

**Stack Tecnológico:**
- **Backend:** Python (FastAPI) + Supabase (PostgreSQL)
- **Frontend:** HTML + CSS + JavaScript Vanilla
- **Gráficos:** Plotly.js
- **Hosting:** Railway (Backend) + Cloudflare Pages (Frontend)

**URLs:**
- Frontend: https://formulas-web.pages.dev
- Backend: https://web-production-daa0.up.railway.app
- GitHub: https://github.com/juanmacruzherrera/formulas-web

**Estado actual:**
- ✅ FASES 6.1, 6.2, 6.3 completas
- ✅ Backend FASE 6.4 completo (4 fórmulas 3D)
- ❌ Frontend FASE 6.4 incompleto (5 problemas críticos)

**Documentación de problemas actuales:**
`docs/contexto_opus/20260108_estado_fase_6_4_problemas.md`

---

## 🗂️ ESTRUCTURA DEL PROYECTO

```
formulas-web/
├── backend/
│   ├── main.py                 # Entry point FastAPI
│   ├── services/
│   │   ├── supabase_client.py  # Conexión Supabase
│   │   └── calculadora.py      # Funciones matemáticas
│   ├── routes/
│   │   ├── formulas.py         # Endpoints /api/formulas
│   │   └── calculos.py         # Endpoints /api/calcular
│   └── scripts/                # Scripts de utilidad
├── frontend/
│   ├── index.html              # HTML principal
│   ├── js/
│   │   ├── api.js              # Llamadas al backend
│   │   ├── app.js              # Lógica principal
│   │   ├── graficos.js         # Renderizado Plotly
│   │   └── animacion.js        # Animaciones 2D/3D
│   └── css/
│       └── styles.css          # Estilos custom
└── docs/                       # Documentación
    ├── contexto_opus/          # Contexto para Opus
    └── aprendizaje/            # Registro de cambios
```

---

## 📄 ARCHIVOS RAÍZ

### Archivo: CLAUDE.md

```markdown
# CLAUDE.md - Instrucciones para Claude Code

## 📋 TAREA ACTUAL: REDISEÑO COMPLETO v2.0

**FASE 6: REDISEÑO + BUGS + 3D + ANIMACIONES**

**📖 DOCUMENTOS CLAVE:**
1. **PLAN ORIGINAL (Opus):** `docs/REDISENO_COMPLETO_V2.md`
2. **ESTADO ACTUAL (8 Enero 2026):** `docs/contexto_opus/20260108_estado_fase_6_4_problemas.md` ⭐
3. **REGISTRO DE CAMBIOS:** `docs/aprendizaje/17_rediseno_v2.md`

**⚠️ LEER PRIMERO:** `docs/contexto_opus/20260108_estado_fase_6_4_problemas.md`
Este documento contiene:
- ✅ Lo que está completo (FASES 6.1, 6.2, 6.3, Backend 6.4)
- ❌ 5 problemas críticos del frontend con soluciones detalladas
- 📍 Ubicación exacta de cada error (archivo + líneas)
- 💻 Código faltante con ejemplos completos
- 📋 Checklist de tareas pendientes con prioridades

**🎯 OBJETIVOS PRINCIPALES:**
1. **Inputs limpios** - Sin spinners, escribir números directamente
2. **Separar 2D y 3D** - Tabs para cada sección
3. **Animación temporal** - Ver cómo se construye la gráfica
4. **Gráfico protagonista** - 70-80% de la pantalla
5. **Responsive** - Adaptarse a móvil → monitor 27"
6. **Nuevas fórmulas 3D** - Hélice, Lorenz, Toro, Ondas

**URLs de producción:**
- Frontend: https://formulas-web.pages.dev
- Backend: https://web-production-daa0.up.railway.app
- GitHub: https://github.com/juanmacruzherrera/formulas-web

---

## ⛔ REGLA CRÍTICA: NO SOBREESCRIBIR DOCUMENTACIÓN

> **ACTUALIZAR ≠ SOBREESCRIBIR**
>
> - ❌ PROHIBIDO: Borrar contenido existente y poner contenido nuevo
> - ❌ PROHIBIDO: Reemplazar un archivo de documentación completo
> - ❌ PROHIBIDO: Eliminar errores, intentos fallidos o procesos anteriores
>
> - ✅ CORRECTO: Añadir nuevo contenido AL FINAL del archivo
> - ✅ CORRECTO: Mantener TODO el historial de errores y soluciones
> - ✅ CORRECTO: Usar secciones con fecha para nuevas entradas

### ¿Por qué esta regla?

Juan aprende del PROCESO, no solo del resultado final. 

- Los errores enseñan más que los éxitos
- Ver los intentos fallidos ayuda a entender el "por qué"
- El historial completo permite repasar cómo se llegó a la solución

### Ejemplo INCORRECTO:
```
# Archivo existente tiene 50 líneas de documentación
# Claude Code lo reemplaza completamente con 30 líneas nuevas
# Se perdió todo el historial → MAL
```

### Ejemplo CORRECTO:
```markdown
# El archivo existente se mantiene intacto
# Claude Code añade al final:

---

## Actualización 2024-12-30

### Cambio realizado:
[descripción]

### Por qué:
[explicación]
```

### Archivos donde NUNCA se sobreescribe:
- `docs/aprendizaje/*.md` → Solo añadir, nunca borrar
- `docs/bitacora.md` → Nuevas entradas ARRIBA, nunca borrar antiguas
- Cualquier archivo `.md` de documentación

### Archivos donde SÍ se puede sobreescribir:
- Código fuente (`.py`, `.js`, `.html`, `.css`) → Normal editarlos
- `PLAN.md` → Solo para marcar tareas ✅, no borrar contenido

### ⚠️ PERO: Documentar cada cambio de código

Cuando modifiques código, documenta el DIFF (qué cambió) en el archivo de aprendizaje:

```markdown
### Cambio en `archivo.py` - 2024-12-30

**Qué cambié:**
```diff
- linea_antigua = "esto estaba antes"
+ linea_nueva = "esto puse ahora"
```

**Por qué lo cambié:**
Porque [explicación clara del motivo]

**Resultado:**
Ahora funciona porque [explicación]
```

Así Juan puede:
- Ver exactamente qué líneas cambiaron (rojo = antes, verde = después)
- Entender POR QUÉ se hizo el cambio
- Seguir la evolución del código paso a paso

---

## ⛔ REGLA CRÍTICA: VERIFICAR DESTINO ANTES DE ESCRIBIR CÓDIGO

> **SIEMPRE verifica qué ESPERA el destino ANTES de escribir código que envía datos.**

### El principio:

```
Cualquier conexión:  A → B

ANTES de escribir A, pregunta: "¿Qué espera B?"
```

### Aplica a TODAS las conexiones:

| Origen (A) | Destino (B) | Qué verificar ANTES |
|------------|-------------|---------------------|
| Python | Supabase | ¿Qué columnas tiene la tabla? ¿Qué formato tienen los datos existentes? |
| JavaScript | Python API | ¿Qué endpoints existen? ¿Qué parámetros esperan? ¿Qué formato de respuesta devuelven? |
| Función X | Función Y | ¿Qué parámetros espera Y? ¿Qué tipo de datos? |
| Frontend | Backend | ¿El endpoint existe? ¿Qué JSON espera? |
| Script | Base de datos | ¿La tabla existe? ¿Qué campos son requeridos? |

### El error recurrente:

Claude Code escribe código que PRODUCE datos sin verificar qué ESPERA el destino:

```
❌ MAL:  Escribo "valores" porque me parece lógico
✅ BIEN: Verifico que Supabase tiene "valores_entrada" → uso ese nombre

❌ MAL:  Añado campo "descripcion" porque lo necesito
✅ BIEN: Verifico que la tabla NO tiene esa columna → o la creo en Supabase, o no la uso

❌ MAL:  Llamo a /api/calcular con {"params": {...}}
✅ BIEN: Verifico en calculos.py que espera {"formula_id": int, "valores": dict}
```

### Metodología obligatoria:

```
1. IDENTIFICAR: ¿Mi código envía datos a dónde?
2. VERIFICAR:  ¿Qué estructura/formato espera ese destino?
3. ADAPTAR:   Escribir mi código para que coincida con lo esperado
4. SI NO EXISTE: Crear primero en el destino, LUEGO escribir el origen
```

### Ejemplos prácticos:

**Antes de insertar en Supabase:**
```python
# Verifico qué tiene la tabla
response = supabase.table("formulas").select("*").limit(1).execute()
print("Columnas:", list(response.data[0].keys()))
# Ahora sé exactamente qué campos usar
```

**Antes de llamar a un endpoint desde JS:**
```javascript
// Verifico en el archivo Python qué espera el endpoint
// Leo backend/routes/calculos.py → veo que espera {formula_id, valores}
// Ahora escribo mi fetch con ese formato exacto
```

**Antes de llamar a una función:**
```python
# Verifico la firma de la función
# def calcular_mru(x0, v, t_min, t_max, puntos=100)
# Ahora sé qué parámetros pasar
```

### Checklist universal:

- [ ] ¿Identifiqué a dónde van los datos que estoy escribiendo?
- [ ] ¿Verifiqué qué estructura/formato espera ese destino?
- [ ] ¿Los nombres coinciden EXACTAMENTE con lo que existe?
- [ ] ¿Si algo no existe en el destino, lo creo PRIMERO?

**Esta verificación toma 30 segundos y evita 30 minutos de debugging.**

---

## INFORMACIÓN DEL PROYECTO

**Nombre:** Web de Fórmulas Matemáticas
**Propósito:** Aplicación web educativa para visualizar fórmulas matemáticas y físicas
**Usuario:** Juan Manuel (51 años, estudiante de Ciencia de Datos)
**Objetivo PRINCIPAL:** Que Juan ENTIENDA cómo se construye, no solo que funcione

---

## ⚠️ REGLA FUNDAMENTAL

> **Este proyecto es EDUCATIVO. Cada línea de código debe poder explicarse.**
> 
> Juan quiere aprender cómo se construye una aplicación web completa.
> Tu trabajo no es solo escribir código que funcione, sino DOCUMENTAR 
> el proceso de forma que alguien pueda entenderlo desde cero.

---

## STACK TECNOLÓGICO

| Capa | Tecnología | Versión |
|------|------------|---------|
| Backend | Python + FastAPI | 3.11+ / 0.104+ |
| Base de datos | Supabase (PostgreSQL) | - |
| Frontend | HTML + Vanilla JS | ES6+ |
| Gráficos | Plotly.js | Última |
| Estilos | CSS puro | - |

---

## ESTRUCTURA DEL PROYECTO

```
formulas-web/
├── CLAUDE.md              ← ESTE ARCHIVO (léelo siempre primero)
├── PLAN.md                ← Lista de tareas (actualízalo)
├── .env                   ← Credenciales (NUNCA tocar/mostrar)
├── .env.example           ← Plantilla de credenciales
├── .gitignore             ← Archivos a ignorar en Git
│
├── backend/
│   ├── main.py            ← Punto de entrada FastAPI
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── formulas.py    ← Endpoints de fórmulas
│   │   └── calculos.py    ← Endpoints de cálculos
│   └── services/
│       ├── __init__.py
│       ├── supabase_client.py  ← Conexión a BD
│       └── calculadora.py      ← Lógica de cálculo
│
├── frontend/
│   ├── index.html         ← Página principal
│   ├── css/
│   │   └── styles.css
│   └── js/
│       ├── api.js         ← Comunicación con backend
│       └── graficos.js    ← Renderizado con Plotly
│
├── docs/
│   ├── MAESTRO.md         ← Documento completo del proyecto
│   ├── bitacora.md        ← Registro de cambios
│   ├── aprendizaje/       ← DOCUMENTACIÓN SOCRÁTICA
│   │   ├── 00_PLANTILLA.md
│   │   ├── 01_conexion_supabase.md
│   │   ├── 02_primer_endpoint.md
│   │   └── ...
│   └── chats_register/    ← 💾 CHATS COMPLETOS GUARDADOS
│       └── *.txt          ← Historial antes de compactar
│
└── _local_info/           ← Info de referencia (no se sube a Git)
    └── tutorial_supabase.md
```

### 💾 IMPORTANTE: Carpeta chats_register

En `docs/chats_register/` están guardados los chats COMPLETOS de sesiones anteriores.

**Si necesitas contexto de lo que se hizo antes:**
1. Lee los archivos `.txt` en esa carpeta
2. Contienen TODO el historial de comandos, errores y soluciones
3. Es útil si se compactó y perdiste contexto

**NO modifiques estos archivos** - son registro histórico.

---

## METODOLOGÍA DE TRABAJO

### PASO 1: Antes de escribir código

1. **Lee PLAN.md** → Identifica la tarea actual
2. **Verifica dependencias** → ¿Las tareas anteriores están ✅?
3. **Crea el archivo de documentación** ANTES del código
   - Copia la plantilla de `docs/aprendizaje/00_PLANTILLA.md`
   - Rellena secciones 1-4 (Qué, Por qué, Cómo encaja, Conceptos)

### PASO 2: Escribir el código

4. **Escribe el código** con comentarios claros
5. **Cada archivo debe tener** un comentario de cabecera:

```python
# archivo.py
# ============================================
# QUÉ HACE: Breve descripción
# CONSUME: De dónde obtiene datos
# EXPONE: Qué ofrece a otros archivos
# RELACIONADO CON: Otros archivos que usa o que lo usan
# ============================================
```

### PASO 3: Probar y documentar resultado

6. **Prueba que funciona** → Ejecuta el código
7. **Documenta el resultado** en el archivo de aprendizaje:
   - Si funcionó → Sección 7 con ✅
   - Si falló → Sección 7 con ❌ + diagnóstico + solución

### PASO 4: Actualizar registros

8. **Actualiza PLAN.md** → Marca la tarea como ✅
9. **Actualiza bitacora.md** → Añade entrada con fecha
10. **Completa el archivo de aprendizaje** → Secciones 8 y 9

---

## FORMATO DE DOCUMENTACIÓN SOCRÁTICA

Cada archivo en `docs/aprendizaje/` debe responder:

| Pregunta | Sección |
|----------|---------|
| ¿Qué vamos a hacer? | Explicación simple, sin tecnicismos |
| ¿Por qué lo necesitamos? | Problema que resuelve |
| ¿Cómo encaja en el proyecto? | Diagrama de arquitectura |
| ¿Qué conceptos necesito entender? | Explicación previa |
| ¿Cómo es el código? | Código + explicación línea por línea |
| ¿Funcionó? | Resultado de la prueba |
| ¿Qué aprendimos? | Resumen y lecciones |
| ¿Qué viene después? | Conexión con siguiente paso |

---

## MANEJO DE ERRORES (MUY IMPORTANTE)

> **Los errores son OPORTUNIDADES de aprendizaje. NUNCA los ocultes.**
>
> **⚠️ RECORDATORIO: Los errores NUNCA se borran de la documentación.**
> Aunque ya estén solucionados, el historial de fallos + diagnóstico + solución
> es el contenido MÁS VALIOSO para el aprendizaje.

Cuando algo falle:

### 1. Documenta el error completo
```
Error: [mensaje exacto]
Archivo: [dónde ocurrió]
Línea: [número]
```

### 2. Diagnostica (piensa en voz alta)
- "Creo que falló porque..."
- "Voy a verificar si..."
- "Otra posibilidad es..."

### 3. Documenta los intentos de solución
```
Intento 1: Cambié X por Y
Resultado: Sigue fallando, pero ahora dice Z

Intento 2: Revisé la documentación y vi que...
Resultado: ¡Funcionó!
```

### 4. Extrae la lección
- "Para la próxima vez, recordar que..."
- "Este error es común cuando..."

---

## REGLAS DE CÓDIGO

### Python (Backend)

```python
# ✅ CORRECTO: Nombres descriptivos, comentarios útiles
def obtener_formulas():
    """
    Obtiene todas las fórmulas de la base de datos.
    
    Returns:
        list: Lista de diccionarios con los datos de cada fórmula
    """
    # Conectamos con Supabase usando el cliente configurado
    response = supabase.table("formulas").select("*").execute()
    return response.data

# ❌ INCORRECTO: Sin comentarios, nombres crípticos
def get_f():
    r = sb.table("formulas").select("*").execute()
    return r.data
```

### Respuestas JSON estandarizadas

```python
# Éxito
{"data": {...}, "error": None}

# Error
{"data": None, "error": "Mensaje descriptivo del error"}
```

### JavaScript (Frontend)

```javascript
// ✅ CORRECTO
async function obtenerFormulas() {
    // Llamamos al backend para obtener la lista de fórmulas
    const respuesta = await fetch('/api/formulas');
    const datos = await respuesta.json();
    return datos;
}
```

---

## ARCHIVOS QUE NUNCA DEBES MODIFICAR

- ❌ `.env` (contiene secretos reales)
- ❌ `.gitignore` (ya está configurado)
- ❌ `_local_info/*` (es referencia personal de Juan)

---

## ARCHIVOS QUE DEBES ACTUALIZAR SIEMPRE

- ✅ `PLAN.md` → Marcar tareas completadas
- ✅ `docs/bitacora.md` → Registrar cada cambio
- ✅ `docs/aprendizaje/XX_nombre.md` → Documentación socrática

---

## CREDENCIALES (SUPABASE)

Las credenciales están en `.env`. Para usarlas:

```python
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
```

**Proyecto Supabase configurado:**
- URL: Configurada en .env
- Tabla `formulas`: Existe con 1 fórmula de prueba (MRU)
- Tabla `calculos`: Existe, vacía

---

## ENDPOINTS A IMPLEMENTAR

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/health` | Verificar que el servidor funciona |
| GET | `/api/formulas` | Listar todas las fórmulas |
| GET | `/api/formula/{id}` | Obtener una fórmula por ID |
| POST | `/api/calcular` | Calcular y guardar resultado |
| GET | `/api/historial` | Obtener cálculos anteriores |

---

## FLUJO DE DATOS

```
┌─────────────┐     HTTP      ┌─────────────┐    Supabase    ┌─────────────┐
│  FRONTEND   │ ──────────→   │   BACKEND   │  ──────────→   │  SUPABASE   │
│  (HTML/JS)  │ ←──────────   │  (FastAPI)  │  ←──────────   │ (PostgreSQL)│
└─────────────┘    JSON       └─────────────┘     JSON       └─────────────┘
```

---

## CHECKLIST ANTES DE CADA COMMIT

- [ ] ¿El código tiene comentarios explicativos?
- [ ] ¿Creé/actualicé el archivo de aprendizaje?
- [ ] ¿Actualicé PLAN.md?
- [ ] ¿Actualicé bitacora.md?
- [ ] ¿Probé que funciona?
- [ ] ¿Documenté errores si los hubo?

---

## CÓMO EMPEZAR

1. Lee `PLAN.md` para ver la lista de tareas
2. Busca la primera tarea con estado ⏳
3. Sigue la metodología de trabajo (pasos 1-4)
4. Pasa a la siguiente tarea

---

*Última actualización: 29 diciembre 2024*

```


---

# 🐍 BACKEND (Python + FastAPI)


## Carpeta: backend/services


### Archivo: backend/services/__init__.py

```python
# backend/services/__init__.py
# Módulo de servicios externos (Supabase, etc.)

```


### Archivo: backend/services/calculadora.py

```python
# backend/services/calculadora.py
# ============================================
# QUÉ HACE: Funciones de cálculo matemático para fórmulas
# CONSUME: Valores numéricos de entrada (parámetros de fórmulas)
# EXPONE: Funciones de cálculo que devuelven arrays de puntos
# RELACIONADO CON:
#   - Usado por: backend/routes/calculos.py (próxima tarea)
#   - No depende de BD ni HTTP
# ============================================

import numpy as np

def calcular_mru(x0: float, v: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """
    Calcula posición en Movimiento Rectilíneo Uniforme (MRU).

    Fórmula: x = x₀ + v·t

    Esta función genera un array de valores de tiempo entre t_min y t_max,
    y calcula la posición correspondiente para cada tiempo usando la fórmula MRU.

    Args:
        x0 (float): Posición inicial (en metros)
        v (float): Velocidad constante (en m/s)
        t_min (float): Tiempo inicial (en segundos)
        t_max (float): Tiempo final (en segundos)
        puntos (int, optional): Cantidad de puntos a calcular. Por defecto 100.

    Returns:
        dict: Diccionario con dos claves:
            - "t": Lista de valores de tiempo (list[float])
            - "x": Lista de valores de posición (list[float])

    Example:
        >>> resultado = calcular_mru(x0=0, v=5, t_min=0, t_max=10, puntos=5)
        >>> print(resultado)
        {
            "t": [0.0, 2.5, 5.0, 7.5, 10.0],
            "x": [0.0, 12.5, 25.0, 37.5, 50.0]
        }

        # Con valores por defecto de puntos (100)
        >>> resultado = calcular_mru(0, 5, 0, 10)
        >>> len(resultado["t"])
        100

    Mathematical Background:
        En MRU, la velocidad es constante, por lo que:
        - Si v > 0: el objeto se mueve hacia adelante
        - Si v < 0: el objeto se mueve hacia atrás
        - Si v = 0: el objeto está en reposo (x siempre es x₀)

        La posición aumenta linealmente con el tiempo.
    """
    # Generar array de tiempos igualmente espaciados
    # linspace(inicio, fin, cantidad) incluye ambos extremos
    t = np.linspace(t_min, t_max, puntos)

    # Calcular posición para cada tiempo
    # Operación vectorizada: v*t multiplica v por cada elemento de t
    x = x0 + v * t

    # Convertir NumPy arrays a listas Python (para JSON)
    # .tolist() es necesario porque NumPy arrays no son JSON-serializables
    return {
        "t": t.tolist(),
        "x": x.tolist()
    }


def calcular_mrua(x0: float, v0: float, a: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """MRUA: x = x0 + v0*t + 0.5*a*t²"""
    t = np.linspace(t_min, t_max, puntos)
    x = x0 + v0 * t + 0.5 * a * t**2
    return {"t": t.tolist(), "x": x.tolist()}


def calcular_caida_libre(y0: float, g: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """Caída libre: y = y0 - 0.5*g*t²"""
    t = np.linspace(t_min, t_max, puntos)
    y = y0 - 0.5 * g * t**2
    y = np.maximum(y, 0)  # No puede bajar de 0
    return {"t": t.tolist(), "y": y.tolist()}


def calcular_tiro_parabolico(v0: float, theta: float, g: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """Tiro parabólico: calcula x e y"""
    theta_rad = np.radians(theta)
    t = np.linspace(t_min, t_max, puntos)
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    y = np.maximum(y, 0)
    return {"t": t.tolist(), "x": x.tolist(), "y": y.tolist()}


def calcular_armonico_simple(A: float, omega: float, phi: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """MAS: x = A*cos(ω*t + φ)"""
    t = np.linspace(t_min, t_max, puntos)
    x = A * np.cos(omega * t + phi)
    return {"t": t.tolist(), "x": x.tolist()}


def calcular_onda_sinusoidal(A: float, k: float, omega: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Onda: y = A*sin(k*x - ω*t) en t=0"""
    x = np.linspace(x_min, x_max, puntos)
    y = A * np.sin(k * x)  # t=0
    return {"x": x.tolist(), "y": y.tolist()}


def calcular_parabola(a: float, b: float, c: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Parábola: y = ax² + bx + c"""
    x = np.linspace(x_min, x_max, puntos)
    y = a * x**2 + b * x + c
    return {"x": x.tolist(), "y": y.tolist()}


def calcular_exponencial(a: float, b: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Exponencial: y = a*e^(bx)"""
    x = np.linspace(x_min, x_max, puntos)
    y = a * np.exp(b * x)
    return {"x": x.tolist(), "y": y.tolist()}


def calcular_logaritmica(a: float, b: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Logarítmica: y = a*ln(x) + b"""
    x = np.linspace(max(x_min, 0.001), x_max, puntos)  # Evitar ln(0)
    y = a * np.log(x) + b
    return {"x": x.tolist(), "y": y.tolist()}


def calcular_seno(A: float, B: float, C: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Seno: y = A*sin(Bx + C)"""
    x = np.linspace(x_min, x_max, puntos)
    y = A * np.sin(B * x + C)
    return {"x": x.tolist(), "y": y.tolist()}


def calcular_circunferencia(r: float, theta_min: float, theta_max: float, puntos: int = 100) -> dict:
    """Circunferencia paramétrica"""
    theta = np.linspace(theta_min, theta_max, puntos)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}


def calcular_espiral_arquimedes(a: float, b: float, theta_min: float, theta_max: float, puntos: int = 200) -> dict:
    """Espiral de Arquímedes: r = a + b*θ"""
    theta = np.linspace(theta_min, theta_max, puntos)
    r = a + b * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}


def calcular_espiral_logaritmica(a: float, b: float, theta_min: float, theta_max: float, puntos: int = 200) -> dict:
    """Espiral logarítmica: r = a*e^(b*θ)"""
    theta = np.linspace(theta_min, theta_max, puntos)
    r = a * np.exp(b * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}


def calcular_cardioide(a: float, theta_min: float, theta_max: float, puntos: int = 200) -> dict:
    """Cardioide: r = a*(1 + cos(θ))"""
    theta = np.linspace(theta_min, theta_max, puntos)
    r = a * (1 + np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}


def calcular_lemniscata(a: float, theta_min: float, theta_max: float, puntos: int = 200) -> dict:
    """Lemniscata: r² = a²*cos(2θ)

    IMPORTANTE: Filtra valores ANTES de calcular para evitar NaN.
    Solo calcula puntos donde cos(2θ) >= 0 (solución real existe).
    """
    theta = np.linspace(theta_min, theta_max, puntos)
    cos_2theta = np.cos(2 * theta)

    # FILTRAR: Solo puntos donde cos(2θ) >= 0 (evita NaN)
    valid_mask = cos_2theta >= 0
    theta_valid = theta[valid_mask]
    cos_2theta_valid = cos_2theta[valid_mask]

    # Calcular r solo para valores válidos (sin NaN)
    r = a * np.sqrt(cos_2theta_valid)

    # Lado positivo
    x_pos = r * np.cos(theta_valid)
    y_pos = r * np.sin(theta_valid)

    # Lado negativo (simetría)
    x_neg = -r * np.cos(theta_valid)
    y_neg = -r * np.sin(theta_valid)

    # Combinar ambos lados (sin NaN, JSON válido)
    x_full = np.concatenate([x_pos, x_neg])
    y_full = np.concatenate([y_pos, y_neg])

    return {"x": x_full.tolist(), "y": y_full.tolist()}


# ============================================
# FÓRMULAS 3D
# ============================================

def calcular_helice(r: float, c: float, t_min: float, t_max: float, puntos: int = 200) -> dict:
    """Hélice 3D: x = r·cos(t), y = r·sin(t), z = c·t

    Args:
        r: Radio de la hélice
        c: Constante de elevación (pitch)
        t_min: Tiempo inicial
        t_max: Tiempo final
        puntos: Número de puntos a calcular

    Returns:
        dict: {"x": [...], "y": [...], "z": [...]}
    """
    t = np.linspace(t_min, t_max, puntos)
    x = r * np.cos(t)
    y = r * np.sin(t)
    z = c * t

    return {"x": x.tolist(), "y": y.tolist(), "z": z.tolist()}


def calcular_lorenz(sigma: float, rho: float, beta: float, t_max: float, puntos: int = 2000) -> dict:
    """Atractor de Lorenz: Sistema de ecuaciones diferenciales

    dx/dt = σ(y - x)
    dy/dt = x(ρ - z) - y
    dz/dt = xy - βz

    Args:
        sigma: Parámetro σ (típicamente 10)
        rho: Parámetro ρ (típicamente 28)
        beta: Parámetro β (típicamente 8/3)
        t_max: Tiempo máximo de simulación
        puntos: Número de puntos a calcular

    Returns:
        dict: {"x": [...], "y": [...], "z": [...]}
    """
    dt = t_max / puntos

    # Condiciones iniciales
    x, y, z = 1.0, 1.0, 1.0

    # Arrays para almacenar resultados
    xs, ys, zs = [x], [y], [z]

    # Integración usando método de Euler
    for _ in range(puntos - 1):
        dx = sigma * (y - x) * dt
        dy = (x * (rho - z) - y) * dt
        dz = (x * y - beta * z) * dt

        x += dx
        y += dy
        z += dz

        xs.append(x)
        ys.append(y)
        zs.append(z)

    return {"x": xs, "y": ys, "z": zs}


def calcular_toro(R: float, r: float, u_min: float, u_max: float, v_min: float, v_max: float, puntos_u: int = 50, puntos_v: int = 50) -> dict:
    """Toro 3D (dona): Superficie paramétrica

    x = (R + r·cos(v))·cos(u)
    y = (R + r·cos(v))·sin(u)
    z = r·sin(v)

    Args:
        R: Radio mayor (centro del tubo al centro del toro)
        r: Radio menor (radio del tubo)
        u_min, u_max: Rango para parámetro u (ángulo mayor)
        v_min, v_max: Rango para parámetro v (ángulo menor)
        puntos_u, puntos_v: Número de puntos en cada dirección

    Returns:
        dict: {"x": [...], "y": [...], "z": [...]}
    """
    u = np.linspace(u_min, u_max, puntos_u)
    v = np.linspace(v_min, v_max, puntos_v)
    u, v = np.meshgrid(u, v)

    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)

    # Aplanar arrays para devolver lista 1D
    return {
        "x": x.flatten().tolist(),
        "y": y.flatten().tolist(),
        "z": z.flatten().tolist()
    }


def calcular_ondas_3d(amplitud: float, frecuencia: float, x_min: float, x_max: float, y_min: float, y_max: float, puntos: int = 50) -> dict:
    """Ondas 3D: z = A·sin(f·√(x²+y²))

    Genera una superficie de ondas circulares concéntricas.

    Args:
        amplitud: Amplitud de las ondas (A)
        frecuencia: Frecuencia de las ondas (f)
        x_min, x_max: Rango en X
        y_min, y_max: Rango en Y
        puntos: Número de puntos en cada dirección

    Returns:
        dict: {"x": [...], "y": [...], "z": [...]}
    """
    x = np.linspace(x_min, x_max, puntos)
    y = np.linspace(y_min, y_max, puntos)
    x, y = np.meshgrid(x, y)

    # Calcular distancia desde el origen
    r = np.sqrt(x**2 + y**2)

    # Calcular altura de la onda
    z = amplitud * np.sin(frecuencia * r)

    # Aplanar arrays para devolver lista 1D
    return {
        "x": x.flatten().tolist(),
        "y": y.flatten().tolist(),
        "z": z.flatten().tolist()
    }


# Bloque de prueba (solo se ejecuta si ejecutamos este archivo directamente)
if __name__ == "__main__":
    print("🧮 Probando función calcular_mru()...\n")

    # Prueba 1: Valores del ejemplo (v=5 m/s, desde reposo)
    print("Prueba 1: v=5 m/s, x₀=0 m, t=0-10s")
    resultado = calcular_mru(x0=0, v=5, t_min=0, t_max=10, puntos=5)
    print(f"  t: {resultado['t']}")
    print(f"  x: {resultado['x']}")
    print(f"  ✓ Generó {len(resultado['t'])} puntos\n")

    # Prueba 2: Partiendo desde x₀=10
    print("Prueba 2: v=3 m/s, x₀=10 m, t=0-5s")
    resultado = calcular_mru(x0=10, v=3, t_min=0, t_max=5, puntos=6)
    print(f"  t: {resultado['t']}")
    print(f"  x: {resultado['x']}")
    print(f"  ✓ La posición inicial es {resultado['x'][0]} (debe ser 10)\n")

    # Prueba 3: Velocidad negativa (retroceso)
    print("Prueba 3: v=-2 m/s (retroceso), x₀=20 m, t=0-5s")
    resultado = calcular_mru(x0=20, v=-2, t_min=0, t_max=5, puntos=6)
    print(f"  t: {resultado['t']}")
    print(f"  x: {resultado['x']}")
    print(f"  ✓ La posición disminuye (velocidad negativa)\n")

    # Prueba 4: Reposo (v=0)
    print("Prueba 4: v=0 m/s (reposo), x₀=15 m, t=0-10s")
    resultado = calcular_mru(x0=15, v=0, t_min=0, t_max=10, puntos=3)
    print(f"  t: {resultado['t']}")
    print(f"  x: {resultado['x']}")
    print(f"  ✓ Posición constante (reposo)\n")

    # Prueba 5: Muchos puntos (para graficar)
    print("Prueba 5: 100 puntos (típico para gráfico)")
    resultado = calcular_mru(x0=0, v=5, t_min=0, t_max=10)  # puntos=100 por defecto
    print(f"  Cantidad de puntos: {len(resultado['t'])}")
    print(f"  Primeros 3 valores t: {resultado['t'][:3]}")
    print(f"  Primeros 3 valores x: {resultado['x'][:3]}")
    print(f"  Últimos 3 valores t: {resultado['t'][-3:]}")
    print(f"  Últimos 3 valores x: {resultado['x'][-3:]}")
    print(f"  ✓ Listo para graficar\n")

    print("✅ Todas las pruebas completadas")

```


### Archivo: backend/services/supabase_client.py

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


## Carpeta: backend/routes


### Archivo: backend/routes/__init__.py

```python
# backend/routes/__init__.py
# Módulo de rutas API

```


### Archivo: backend/routes/calculos.py

```python
# backend/routes/calculos.py
# ============================================
# QUÉ HACE: Endpoints para realizar cálculos de fórmulas
# CONSUME:
#   - Datos del usuario (formula_id + valores) vía POST
#   - Fórmulas de Supabase (tabla formulas)
#   - Historial de cálculos (tabla calculos)
# EXPONE:
#   - POST /api/calcular → Calcula, guarda y devuelve resultado
#   - GET /api/historial → Devuelve historial de cálculos con JOIN a formulas
# RELACIONADO CON:
#   - Usa: backend/services/supabase_client.py (conexión BD)
#   - Usa: backend/services/calculadora.py (función calcular_mru)
#   - Usado por: frontend/js/api.js (próxima fase)
# ============================================

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from backend.services.supabase_client import supabase
from backend.services.calculadora import (
    calcular_mru,
    calcular_mrua,
    calcular_caida_libre,
    calcular_tiro_parabolico,
    calcular_armonico_simple,
    calcular_onda_sinusoidal,
    calcular_parabola,
    calcular_exponencial,
    calcular_logaritmica,
    calcular_seno,
    calcular_circunferencia,
    calcular_espiral_arquimedes,
    calcular_espiral_logaritmica,
    calcular_cardioide,
    calcular_lemniscata,
    # Funciones 3D
    calcular_helice,
    calcular_lorenz,
    calcular_toro,
    calcular_ondas_3d
)

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
        # Identificamos el tipo por el nombre ya que el campo 'tipo' no existe en la BD
        # Extraemos rango dinámico de la fórmula o usamos valores del usuario
        rango_min = datos.valores.get(formula["variable_rango"] + "_min", formula.get("rango_min", 0))
        rango_max = datos.valores.get(formula["variable_rango"] + "_max", formula.get("rango_max", 10))

        # Identificar fórmula por nombre y llamar función correspondiente
        if "MRU" in formula["nombre"] and "Uniformemente Acelerado" not in formula["nombre"]:
            resultado = calcular_mru(
                x0=datos.valores.get("x0", 0),
                v=datos.valores.get("v", 5),
                t_min=rango_min,
                t_max=rango_max
            )

        elif "MRUA" in formula["nombre"] or "Uniformemente Acelerado" in formula["nombre"]:
            resultado = calcular_mrua(
                x0=datos.valores.get("x0", 0),
                v0=datos.valores.get("v0", 5),
                a=datos.valores.get("a", 2),
                t_min=rango_min,
                t_max=rango_max
            )

        elif "Caída Libre" in formula["nombre"]:
            resultado = calcular_caida_libre(
                y0=datos.valores.get("y0", 100),
                g=datos.valores.get("g", 9.8),
                t_min=rango_min,
                t_max=rango_max
            )

        elif "Tiro Parabólico" in formula["nombre"]:
            resultado = calcular_tiro_parabolico(
                v0=datos.valores.get("v0", 20),
                theta=datos.valores.get("theta", 45),
                g=datos.valores.get("g", 9.8),
                t_min=rango_min,
                t_max=rango_max
            )

        elif "Armónico Simple" in formula["nombre"]:
            resultado = calcular_armonico_simple(
                A=datos.valores.get("A", 5),
                omega=datos.valores.get("omega", 2),
                phi=datos.valores.get("phi", 0),
                t_min=rango_min,
                t_max=rango_max
            )

        elif "Onda Sinusoidal" in formula["nombre"]:
            resultado = calcular_onda_sinusoidal(
                A=datos.valores.get("A", 3),
                k=datos.valores.get("k", 1),
                omega=datos.valores.get("omega", 0),
                x_min=rango_min,
                x_max=rango_max
            )

        elif "Parábola" in formula["nombre"]:
            resultado = calcular_parabola(
                a=datos.valores.get("a", 1),
                b=datos.valores.get("b", 0),
                c=datos.valores.get("c", 0),
                x_min=rango_min,
                x_max=rango_max
            )

        elif "Exponencial" in formula["nombre"]:
            resultado = calcular_exponencial(
                a=datos.valores.get("a", 1),
                b=datos.valores.get("b", 0.5),
                x_min=rango_min,
                x_max=rango_max
            )

        elif "Logarítmica" in formula["nombre"] and "Espiral" not in formula["nombre"]:
            resultado = calcular_logaritmica(
                a=datos.valores.get("a", 1),
                b=datos.valores.get("b", 0),
                x_min=rango_min,
                x_max=rango_max
            )

        elif "Seno" in formula["nombre"]:
            resultado = calcular_seno(
                A=datos.valores.get("A", 1),
                B=datos.valores.get("B", 1),
                C=datos.valores.get("C", 0),
                x_min=rango_min,
                x_max=rango_max
            )

        elif "Circunferencia" in formula["nombre"]:
            resultado = calcular_circunferencia(
                r=datos.valores.get("r", 5),
                theta_min=rango_min,
                theta_max=rango_max
            )

        elif "Arquímedes" in formula["nombre"]:
            resultado = calcular_espiral_arquimedes(
                a=datos.valores.get("a", 0),
                b=datos.valores.get("b", 0.5),
                theta_min=rango_min,
                theta_max=rango_max
            )

        elif "Logarítmica" in formula["nombre"] and "Espiral" in formula["nombre"]:
            resultado = calcular_espiral_logaritmica(
                a=datos.valores.get("a", 0.5),
                b=datos.valores.get("b", 0.15),
                theta_min=rango_min,
                theta_max=rango_max
            )

        elif "Cardioide" in formula["nombre"]:
            resultado = calcular_cardioide(
                a=datos.valores.get("a", 3),
                theta_min=rango_min,
                theta_max=rango_max
            )

        elif "Lemniscata" in formula["nombre"]:
            resultado = calcular_lemniscata(
                a=datos.valores.get("a", 5),
                theta_min=rango_min,
                theta_max=rango_max
            )

        # ============================================
        # FÓRMULAS 3D
        # ============================================

        elif "Hélice" in formula["nombre"]:
            resultado = calcular_helice(
                r=datos.valores.get("r", 5),
                c=datos.valores.get("c", 0.5),
                t_min=rango_min,
                t_max=rango_max
            )

        elif "Lorenz" in formula["nombre"]:
            resultado = calcular_lorenz(
                sigma=datos.valores.get("sigma", 10),
                rho=datos.valores.get("rho", 28),
                beta=datos.valores.get("beta", 8/3),
                t_max=rango_max,
                puntos=datos.valores.get("puntos", 2000)
            )

        elif "Toro" in formula["nombre"]:
            resultado = calcular_toro(
                R=datos.valores.get("R", 3),
                r=datos.valores.get("r", 1),
                u_min=datos.valores.get("u_min", 0),
                u_max=datos.valores.get("u_max", 6.28),
                v_min=datos.valores.get("v_min", 0),
                v_max=datos.valores.get("v_max", 6.28),
                puntos_u=datos.valores.get("puntos_u", 50),
                puntos_v=datos.valores.get("puntos_v", 50)
            )

        elif "Ondas 3D" in formula["nombre"]:
            resultado = calcular_ondas_3d(
                amplitud=datos.valores.get("amplitud", 1),
                frecuencia=datos.valores.get("frecuencia", 1),
                x_min=datos.valores.get("x_min", -5),
                x_max=datos.valores.get("x_max", 5),
                y_min=datos.valores.get("y_min", -5),
                y_max=datos.valores.get("y_max", 5),
                puntos=datos.valores.get("puntos", 50)
            )

        else:
            # Si el tipo de fórmula no está implementado
            return {
                "data": None,
                "error": f"Fórmula '{formula['nombre']}' no tiene implementación de cálculo aún"
            }

        # PASO 3: Guardar el cálculo en la tabla 'calculos' (historial)
        calculo_guardado = supabase.table("calculos").insert({
            "formula_id": datos.formula_id,
            "valores_entrada": datos.valores,  # La columna se llama 'valores_entrada' en Supabase
            "resultado": resultado
        }).execute()

        # PASO 4: Devolver el resultado
        return {
            "data": {
                "formula": {
                    "id": formula["id"],
                    "nombre": formula["nombre"],
                    "categoria": formula.get("categoria", "")
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


@router.get("/historial")
def obtener_historial(limite: int = 20):
    """
    Obtiene el historial de cálculos realizados, ordenados por más recientes primero.

    Este endpoint consulta la tabla 'calculos' y hace un JOIN automático con la tabla
    'formulas' para incluir información completa de cada fórmula utilizada.

    Args:
        limite (int, optional): Cantidad máxima de cálculos a devolver. Por defecto 20.
                               El usuario puede personalizar: /api/historial?limite=10

    Returns:
        dict: {
            "data": [
                {
                    "id": 2,
                    "formula_id": 1,
                    "valores_entrada": {"x0": 0, "v": 5, ...},
                    "resultado": {"t": [...], "x": [...]},
                    "created_at": "2025-12-29T14:30:00+00:00",
                    "formulas": {
                        "id": 1,
                        "nombre": "MRU - Movimiento Rectilíneo Uniforme",
                        "categoria": "fisica",
                        "formula_latex": "x = x_0 + v \\\\cdot t",
                        ...
                    }
                },
                ...
            ],
            "error": None
        }

    Example:
        GET http://localhost:8000/api/historial         # Últimos 20
        GET http://localhost:8000/api/historial?limite=5  # Últimos 5

    Technical notes:
        - Usa .select("*, formulas(*)") para hacer JOIN automático
        - Ordenado por created_at DESC (más recientes primero)
        - El nombre "formulas" viene de la relación foreign key en Supabase
    """
    try:
        # Consultar tabla calculos con JOIN a formulas
        # "*" = todos los campos de calculos
        # "formulas(*)" = JOIN con tabla formulas, traer todos sus campos
        response = supabase.table("calculos") \
            .select("*, formulas(*)") \
            .order("created_at", desc=True) \
            .limit(limite) \
            .execute()

        # Supabase devuelve los datos con la fórmula anidada en cada cálculo
        # El objeto "formulas" contiene toda la info de la fórmula asociada

        return {
            "data": response.data,
            "error": None
        }

    except Exception as e:
        # Capturar cualquier error inesperado
        return {
            "data": None,
            "error": f"Error al obtener el historial: {str(e)}"
        }


# Bloque de prueba (solo se ejecuta si ejecutamos este archivo directamente)
if __name__ == "__main__":
    print("⚠️  Este archivo define rutas de FastAPI.")
    print("   Para probarlo, ejecuta:")
    print("   uvicorn backend.main:app --reload")
    print("   Luego usa curl o Postman para hacer POST a /api/calcular")

```


### Archivo: backend/routes/formulas.py

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

# ============================================
# ENDPOINT PARA OBTENER FÓRMULA POR ID
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


## Carpeta: backend/scripts


### Archivo: backend/scripts/corregir_variables_usuario.py

```python
#!/usr/bin/env python3
# backend/scripts/corregir_variables_usuario.py
# ============================================
# QUÉ HACE: Corrige el formato de variables_usuario en Supabase
# CONSUME: Tabla 'formulas' de Supabase
# EXPONE: Actualiza registros con formato correcto
# RELACIONADO CON:
#   - Usa: services/supabase_client.py
#   - Modifica: Tabla formulas en Supabase
# ============================================

import sys
import os

# Añadir el directorio padre al path para poder importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.supabase_client import supabase

# Mapeo de fórmulas a sus variables correctas
VARIABLES_CORRECTAS = {
    "MRU": ["x₀", "v", "t"],
    "MRUA": ["x₀", "v₀", "a", "t"],
    "Caída Libre": ["h₀", "g", "t"],
    "Parábola": ["a", "b", "c", "x"],
    "Seno": ["A", "ω", "φ", "t"],
    "Coseno": ["A", "ω", "φ", "t"],
    "Exponencial": ["a", "b", "x"],
    "Logaritmo": ["a", "b", "x"],
    "Circunferencia": ["r", "θ"],
}

def verificar_formulas():
    """
    Verifica el estado actual de las fórmulas en Supabase.
    Muestra qué fórmulas tienen variables_usuario incorrectas.
    """
    print("🔍 Verificando fórmulas en Supabase...\n")

    try:
        # Obtener todas las fórmulas
        response = supabase.table("formulas").select("*").execute()
        formulas = response.data

        print(f"✅ Encontradas {len(formulas)} fórmulas\n")
        print("=" * 80)

        formulas_incorrectas = []

        for formula in formulas:
            nombre = formula['nombre']
            variables_actuales = formula.get('variables_usuario', [])
            variables_correctas = VARIABLES_CORRECTAS.get(nombre, [])

            # Verificar si las variables son incorrectas
            # (ej: ["0", "1", "2"] en lugar de ["x₀", "v₀", "a"])
            es_incorrecta = False

            if not variables_actuales:
                es_incorrecta = True
                razon = "Campo vacío"
            elif all(v.isdigit() for v in variables_actuales):
                es_incorrecta = True
                razon = "Contiene solo números (0,1,2...)"
            elif variables_actuales != variables_correctas and variables_correctas:
                es_incorrecta = True
                razon = "Variables no coinciden con el mapeo correcto"

            # Mostrar estado
            status = "❌" if es_incorrecta else "✅"
            print(f"{status} {nombre} (ID: {formula['id']})")
            print(f"   Actual:   {variables_actuales}")
            if variables_correctas:
                print(f"   Correcta: {variables_correctas}")
            if es_incorrecta:
                print(f"   Razón: {razon}")
                formulas_incorrectas.append({
                    'id': formula['id'],
                    'nombre': nombre,
                    'actual': variables_actuales,
                    'correcta': variables_correctas
                })
            print()

        print("=" * 80)
        print(f"\n📊 Resumen:")
        print(f"   Total: {len(formulas)}")
        print(f"   Correctas: {len(formulas) - len(formulas_incorrectas)}")
        print(f"   Incorrectas: {len(formulas_incorrectas)}")

        return formulas_incorrectas

    except Exception as e:
        print(f"❌ Error al verificar fórmulas: {str(e)}")
        raise

def corregir_formulas(formulas_incorrectas):
    """
    Corrige las fórmulas que tienen variables_usuario incorrectas.

    Args:
        formulas_incorrectas: Lista de diccionarios con info de fórmulas a corregir
    """
    if not formulas_incorrectas:
        print("\n✅ No hay fórmulas que corregir. Todo está correcto.")
        return

    print(f"\n🔧 Corrigiendo {len(formulas_incorrectas)} fórmulas...\n")

    corregidas = 0
    errores = 0

    for formula in formulas_incorrectas:
        try:
            # Actualizar la fórmula en Supabase
            response = supabase.table("formulas").update({
                "variables_usuario": formula['correcta']
            }).eq("id", formula['id']).execute()

            print(f"✅ {formula['nombre']} (ID: {formula['id']})")
            print(f"   {formula['actual']} → {formula['correcta']}")
            corregidas += 1

        except Exception as e:
            print(f"❌ Error al corregir {formula['nombre']}: {str(e)}")
            errores += 1

    print(f"\n📊 Resultado:")
    print(f"   Corregidas: {corregidas}")
    print(f"   Errores: {errores}")

def main():
    """
    Función principal del script.
    """
    print("\n" + "=" * 80)
    print(" SCRIPT DE CORRECCIÓN: variables_usuario en Supabase")
    print("=" * 80 + "\n")

    # Verificar estado actual
    formulas_incorrectas = verificar_formulas()

    # Si hay fórmulas incorrectas, preguntar si se deben corregir
    if formulas_incorrectas:
        print("\n" + "=" * 80)
        respuesta = input("\n¿Deseas corregir estas fórmulas? (s/n): ").lower()

        if respuesta == 's':
            corregir_formulas(formulas_incorrectas)
            print("\n✅ Proceso completado.")
        else:
            print("\n❌ Corrección cancelada.")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()

```


### Archivo: backend/scripts/insert_formulas_3d.sql

```python
-- ============================================
-- INSERTAR FÓRMULAS 3D EN SUPABASE
-- ============================================
-- Ejecutar este script en Supabase SQL Editor
-- Ubicación: Supabase Dashboard > SQL Editor > New Query

-- 1. HÉLICE 3D
INSERT INTO formulas (
    nombre,
    formula_latex,
    categoria,
    descripcion,
    variables_usuario,
    variable_rango,
    rango_min,
    rango_max
) VALUES (
    'Hélice 3D',
    'x = r \cdot \cos(t), \quad y = r \cdot \sin(t), \quad z = c \cdot t',
    'geometria_3d',
    'Curva helicoidal en el espacio 3D. Radio r y constante de elevación c.',
    '{"r": 5, "c": 0.5}',
    't',
    0,
    20
);

-- 2. ATRACTOR DE LORENZ
INSERT INTO formulas (
    nombre,
    formula_latex,
    categoria,
    descripcion,
    variables_usuario,
    variable_rango,
    rango_min,
    rango_max
) VALUES (
    'Atractor de Lorenz',
    '\frac{dx}{dt} = \sigma(y-x), \quad \frac{dy}{dt} = x(\rho-z)-y, \quad \frac{dz}{dt} = xy-\beta z',
    'geometria_3d',
    'Sistema de ecuaciones diferenciales que genera un atractor caótico. Parámetros clásicos: σ=10, ρ=28, β=8/3.',
    '{"sigma": 10, "rho": 28, "beta": 2.667, "puntos": 2000}',
    't',
    0,
    50
);

-- 3. TORO 3D
INSERT INTO formulas (
    nombre,
    formula_latex,
    categoria,
    descripcion,
    variables_usuario,
    variable_rango,
    rango_min,
    rango_max
) VALUES (
    'Toro 3D',
    'x = (R + r\cos v)\cos u, \quad y = (R + r\cos v)\sin u, \quad z = r\sin v',
    'geometria_3d',
    'Superficie toroidal (dona) en 3D. R es el radio mayor y r el radio del tubo.',
    '{"R": 3, "r": 1, "u_min": 0, "u_max": 6.28, "v_min": 0, "v_max": 6.28, "puntos_u": 50, "puntos_v": 50}',
    'u',
    0,
    6.28
);

-- 4. ONDAS 3D
INSERT INTO formulas (
    nombre,
    formula_latex,
    categoria,
    descripcion,
    variables_usuario,
    variable_rango,
    rango_min,
    rango_max
) VALUES (
    'Ondas 3D',
    'z = A \cdot \sin(f \cdot \sqrt{x^2 + y^2})',
    'geometria_3d',
    'Superficie de ondas circulares concéntricas. A es amplitud y f frecuencia.',
    '{"amplitud": 1, "frecuencia": 1, "x_min": -5, "x_max": 5, "y_min": -5, "y_max": 5, "puntos": 50}',
    'x',
    -5,
    5
);

-- Verificar que se insertaron correctamente
SELECT id, nombre, categoria FROM formulas WHERE categoria = 'geometria_3d';

```


### Archivo: backend/scripts/insertar_formulas_3d.py

```python
#!/usr/bin/env python3
"""
Script para insertar fórmulas 3D en Supabase
Ejecutar desde la raíz del proyecto:
    python3 backend/scripts/insertar_formulas_3d.py
"""

import sys
import os

# Añadir el directorio raíz al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from backend.services.supabase_client import supabase

# Definir las 4 fórmulas 3D
formulas_3d = [
    {
        "nombre": "Hélice 3D",
        "formula_latex": r"x = r \cdot \cos(t), \quad y = r \cdot \sin(t), \quad z = c \cdot t",
        "categoria": "geometria_3d",
        "variables_usuario": {"r": 5, "c": 0.5},
        "variable_rango": "t",
        "rango_min": 0,
        "rango_max": 20,
        "rango_dinamico": True
    },
    {
        "nombre": "Atractor de Lorenz",
        "formula_latex": r"\frac{dx}{dt} = \sigma(y-x), \quad \frac{dy}{dt} = x(\rho-z)-y, \quad \frac{dz}{dt} = xy-\beta z",
        "categoria": "geometria_3d",
        "variables_usuario": {"sigma": 10, "rho": 28, "beta": 2.667, "puntos": 2000},
        "variable_rango": "t",
        "rango_min": 0,
        "rango_max": 50,
        "rango_dinamico": True
    },
    {
        "nombre": "Toro 3D",
        "formula_latex": r"x = (R + r\cos v)\cos u, \quad y = (R + r\cos v)\sin u, \quad z = r\sin v",
        "categoria": "geometria_3d",
        "variables_usuario": {"R": 3, "r": 1, "u_min": 0, "u_max": 6.28, "v_min": 0, "v_max": 6.28, "puntos_u": 50, "puntos_v": 50},
        "variable_rango": "u",
        "rango_min": 0,
        "rango_max": 6.28,
        "rango_dinamico": True
    },
    {
        "nombre": "Ondas 3D",
        "formula_latex": r"z = A \cdot \sin(f \cdot \sqrt{x^2 + y^2})",
        "categoria": "geometria_3d",
        "variables_usuario": {"amplitud": 1, "frecuencia": 1, "x_min": -5, "x_max": 5, "y_min": -5, "y_max": 5, "puntos": 50},
        "variable_rango": "x",
        "rango_min": -5,
        "rango_max": 5,
        "rango_dinamico": True
    }
]

def insertar_formulas():
    """Inserta las fórmulas 3D en Supabase"""
    print("🚀 Insertando fórmulas 3D en Supabase...\n")

    for formula in formulas_3d:
        try:
            # Verificar si ya existe
            existing = supabase.table("formulas").select("id").eq("nombre", formula["nombre"]).execute()

            if existing.data:
                print(f"⚠️  '{formula['nombre']}' ya existe (ID: {existing.data[0]['id']})")
                continue

            # Insertar nueva fórmula
            result = supabase.table("formulas").insert(formula).execute()

            if result.data:
                print(f"✅ '{formula['nombre']}' insertada (ID: {result.data[0]['id']})")
            else:
                print(f"❌ Error al insertar '{formula['nombre']}'")

        except Exception as e:
            print(f"❌ Error con '{formula['nombre']}': {e}")

    print("\n✅ Proceso completado. Verificando...")

    # Verificar fórmulas 3D
    result = supabase.table("formulas").select("id, nombre, categoria").eq("categoria", "geometria_3d").execute()

    if result.data:
        print(f"\n📊 Fórmulas 3D en Supabase ({len(result.data)} total):")
        for formula in result.data:
            print(f"   - ID {formula['id']}: {formula['nombre']}")
    else:
        print("\n⚠️  No se encontraron fórmulas 3D en la base de datos")

if __name__ == "__main__":
    insertar_formulas()

```


---

# 🌐 FRONTEND (HTML + CSS + JavaScript)


## Carpeta: frontend/js


### Archivo: frontend/js/animacion.js

```javascript
// frontend/js/animacion.js
// ============================================
// QUÉ HACE: Sistema de animación para gráficos 2D y 3D
// CONSUME: Datos de cálculos (arrays x, y, z, t)
// EXPONE: animarCurva2D(), animarCurva3D()
// RELACIONADO CON:
//   - Usado por: graficos.js (para renderizar con animación)
//   - Usa: Plotly.js (Plotly.extendTraces, Plotly.addFrames)
// ============================================

/**
 * Anima la construcción de una curva 2D punto por punto
 * @param {Object} datos - {x: [...], y: [...]} o {t: [...], x: [...]}
 * @param {number} duracion - Duración total de la animación en ms (default 3000)
 * @returns {number} - ID del timer (para poder cancelar con clearInterval)
 */
function animarCurva2D(datos, duracion = 3000) {
    const container = document.getElementById('graficoContainer');
    const totalPuntos = datos.x.length;
    const intervalo = duracion / totalPuntos;

    // Ocultar placeholder si existe
    const placeholder = document.getElementById('placeholderGrafico');
    if (placeholder) {
        placeholder.style.display = 'none';
    }

    // Configuración inicial (traza vacía)
    const trace = {
        x: [],
        y: datos.y ? [] : [],
        mode: 'lines',
        line: {
            color: '#3b82f6',
            width: 3
        },
        name: 'Curva'
    };

    // Si no hay 'y', usamos 't' como eje Y (para gráficos tiempo-posición)
    const yData = datos.y || datos.t;

    const layout = {
        paper_bgcolor: '#0f172a',
        plot_bgcolor: '#1e293b',
        font: { color: '#94a3b8' },
        xaxis: {
            gridcolor: '#334155',
            zerolinecolor: '#475569',
            color: '#94a3b8',
            title: datos.y ? 'X' : 'Tiempo (s)'
        },
        yaxis: {
            gridcolor: '#334155',
            zerolinecolor: '#475569',
            color: '#94a3b8',
            title: datos.y ? 'Y' : 'Posición (m)'
        },
        margin: { l: 60, r: 40, t: 40, b: 60 },
        showlegend: false
    };

    const config = {
        responsive: true,
        displayModeBar: true,
        displaylogo: false,
        modeBarButtonsToRemove: ['toImage']
    };

    // Crear gráfico vacío
    Plotly.newPlot(container, [trace], layout, config);

    // Animar punto por punto
    let i = 0;
    const timer = setInterval(() => {
        if (i >= totalPuntos) {
            clearInterval(timer);
            console.log('✅ Animación 2D completada');
            return;
        }

        // Añadir siguiente punto usando extendTraces
        Plotly.extendTraces(container, {
            x: [[datos.x[i]]],
            y: [[yData[i]]]
        }, [0]);

        i++;
    }, intervalo);

    return timer;
}

/**
 * Anima una curva 3D con evolución temporal usando frames de Plotly
 * @param {Object} datos - {x: [...], y: [...], z: [...]}
 * @param {number} duracion - Duración total de la animación en ms (default 5000)
 */
function animarCurva3D(datos, duracion = 5000) {
    const container = document.getElementById('graficoContainer');
    const totalPuntos = datos.x.length;

    // Ocultar placeholder si existe
    const placeholder = document.getElementById('placeholderGrafico');
    if (placeholder) {
        placeholder.style.display = 'none';
    }

    // Crear frames de animación (máximo 100 frames para rendimiento)
    const frames = [];
    const step = Math.max(1, Math.floor(totalPuntos / 100));

    for (let i = step; i <= totalPuntos; i += step) {
        frames.push({
            name: `frame${i}`,
            data: [{
                x: datos.x.slice(0, i),
                y: datos.y.slice(0, i),
                z: datos.z.slice(0, i)
            }]
        });
    }

    // Traza inicial (solo primer punto)
    const trace = {
        type: 'scatter3d',
        mode: 'lines',
        x: datos.x.slice(0, 1),
        y: datos.y.slice(0, 1),
        z: datos.z.slice(0, 1),
        line: {
            color: datos.z,  // Color basado en el valor Z
            colorscale: 'Viridis',
            width: 4
        },
        name: 'Curva 3D'
    };

    const layout = {
        scene: {
            xaxis: {
                title: 'X',
                gridcolor: '#334155',
                backgroundcolor: '#0f172a',
                color: '#94a3b8'
            },
            yaxis: {
                title: 'Y',
                gridcolor: '#334155',
                backgroundcolor: '#0f172a',
                color: '#94a3b8'
            },
            zaxis: {
                title: 'Z',
                gridcolor: '#334155',
                backgroundcolor: '#0f172a',
                color: '#94a3b8'
            },
            bgcolor: '#0f172a',
            camera: {
                eye: { x: 1.5, y: 1.5, z: 1.2 }
            }
        },
        paper_bgcolor: '#0f172a',
        font: { color: '#94a3b8' },
        showlegend: false,
        margin: { l: 0, r: 0, t: 0, b: 0 },
        updatemenus: [{
            type: 'buttons',
            showactive: false,
            y: 1,
            x: 0.1,
            yanchor: 'top',
            buttons: [{
                label: '▶ Play',
                method: 'animate',
                args: [null, {
                    fromcurrent: true,
                    frame: { duration: duracion / frames.length, redraw: true },
                    transition: { duration: 0 },
                    mode: 'immediate'
                }]
            }, {
                label: '⏸ Pause',
                method: 'animate',
                args: [[null], {
                    mode: 'immediate',
                    frame: { duration: 0, redraw: false }
                }]
            }]
        }],
        sliders: [{
            active: 0,
            steps: frames.map((f, i) => ({
                label: `${Math.round(i * 100 / frames.length)}%`,
                method: 'animate',
                args: [[f.name], {
                    mode: 'immediate',
                    frame: { duration: 0, redraw: true },
                    transition: { duration: 0 }
                }]
            })),
            x: 0.1,
            len: 0.8,
            y: 0,
            yanchor: 'top',
            currentvalue: {
                prefix: 'Progreso: ',
                visible: true,
                xanchor: 'center',
                font: { color: '#94a3b8' }
            }
        }]
    };

    const config = {
        responsive: true,
        displayModeBar: true,
        displaylogo: false,
        modeBarButtonsToRemove: ['toImage']
    };

    // Crear gráfico 3D con frames
    Plotly.newPlot(container, [trace], layout, config).then(() => {
        Plotly.addFrames(container, frames);
        console.log(`✅ Gráfico 3D creado con ${frames.length} frames`);
    });
}

/**
 * Función auxiliar: Cancela una animación en curso
 * @param {number} timerId - ID del timer devuelto por animarCurva2D
 */
function cancelarAnimacion(timerId) {
    if (timerId) {
        clearInterval(timerId);
        console.log('⏹ Animación cancelada');
    }
}

// Exportar funciones para uso global
window.animacion = {
    animarCurva2D,
    animarCurva3D,
    cancelarAnimacion
};

```


### Archivo: frontend/js/api.js

```javascript
// frontend/js/api.js
// ============================================
// QUÉ HACE: Funciones para comunicarse con el backend FastAPI
// CONSUME: API REST en http://localhost:8000
// EXPONE: Funciones async para obtener y enviar datos
// RELACIONADO CON:
//   - Usado por: frontend/js/app.js
//   - Conecta con: backend/main.py (FastAPI)
// ============================================

// Configuración de la API
// Detecta automáticamente si estamos en desarrollo (localhost) o producción
const API_BASE = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:8000'
    : 'https://web-production-daa0.up.railway.app'; // ✅ Backend desplegado en Railway

/**
 * Muestra una notificación toast al usuario
 * @param {string} mensaje - Texto a mostrar
 * @param {string} tipo - 'success', 'error', 'info'
 */
function mostrarToast(mensaje, tipo = 'info') {
    const toastContainer = document.getElementById('toastContainer');

    const colores = {
        success: 'alert-success',
        error: 'alert-error',
        info: 'alert-info',
        warning: 'alert-warning'
    };

    const iconos = {
        success: '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>',
        error: '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>',
        info: '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>',
        warning: '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>'
    };

    const toast = document.createElement('div');
    toast.className = `alert ${colores[tipo] || colores.info} shadow-lg mb-2`;
    toast.innerHTML = `
        <div>
            ${iconos[tipo] || iconos.info}
            <span>${mensaje}</span>
        </div>
    `;

    toastContainer.appendChild(toast);

    // Auto-eliminar después de 4 segundos
    setTimeout(() => {
        toast.classList.add('opacity-0', 'transition-opacity');
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

/**
 * Actualiza el indicador de estado de conexión
 * @param {boolean} conectado - true si está conectado, false si no
 */
function actualizarEstadoConexion(conectado) {
    const indicador = document.getElementById('statusIndicator');
    const texto = document.getElementById('statusText');

    if (conectado) {
        indicador.classList.remove('loading');
        indicador.classList.add('bg-green-500', 'w-2', 'h-2', 'rounded-full');
        texto.textContent = 'Conectado';
    } else {
        indicador.classList.add('loading');
        indicador.classList.remove('bg-green-500', 'w-2', 'h-2', 'rounded-full');
        texto.textContent = 'Desconectado';
    }
}

/**
 * Obtiene todas las fórmulas disponibles desde el backend
 * @returns {Promise<Array>} Array de fórmulas o array vacío si hay error
 */
async function obtenerFormulas() {
    try {
        const response = await fetch(`${API_BASE}/api/formulas`);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const resultado = await response.json();

        if (resultado.error) {
            throw new Error(resultado.error);
        }

        actualizarEstadoConexion(true);
        return resultado.data || [];

    } catch (error) {
        console.error('Error al obtener fórmulas:', error);
        mostrarToast('Error al cargar las fórmulas', 'error');
        actualizarEstadoConexion(false);
        return [];
    }
}

/**
 * Obtiene una fórmula específica por su ID
 * @param {number} id - ID de la fórmula
 * @returns {Promise<Object|null>} Objeto fórmula o null si hay error
 */
async function obtenerFormula(id) {
    try {
        const response = await fetch(`${API_BASE}/api/formula/${id}`);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const resultado = await response.json();

        if (resultado.error) {
            throw new Error(resultado.error);
        }

        return resultado.data;

    } catch (error) {
        console.error('Error al obtener fórmula:', error);
        mostrarToast('Error al cargar la fórmula', 'error');
        return null;
    }
}

/**
 * Calcula una fórmula con los valores proporcionados
 * @param {number} formulaId - ID de la fórmula a calcular
 * @param {Object} valores - Objeto con los valores de las variables
 * @returns {Promise<Object|null>} Resultado del cálculo o null si hay error
 */
async function calcularFormula(formulaId, valores) {
    try {
        const response = await fetch(`${API_BASE}/api/calcular`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                formula_id: formulaId,
                valores: valores
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const resultado = await response.json();

        if (resultado.error) {
            throw new Error(resultado.error);
        }

        mostrarToast('Cálculo realizado con éxito', 'success');
        return resultado.data;

    } catch (error) {
        console.error('Error al calcular fórmula:', error);
        mostrarToast(`Error en el cálculo: ${error.message}`, 'error');
        return null;
    }
}

/**
 * Obtiene el historial de cálculos realizados
 * @param {number} limite - Cantidad de cálculos a obtener (por defecto 10)
 * @returns {Promise<Array>} Array de cálculos o array vacío si hay error
 */
async function obtenerHistorial(limite = 10) {
    try {
        const response = await fetch(`${API_BASE}/api/historial?limite=${limite}`);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const resultado = await response.json();

        if (resultado.error) {
            throw new Error(resultado.error);
        }

        return resultado.data || [];

    } catch (error) {
        console.error('Error al obtener historial:', error);
        mostrarToast('Error al cargar el historial', 'error');
        return [];
    }
}

/**
 * Verifica que el backend esté funcionando
 * @returns {Promise<boolean>} true si el servidor responde, false si no
 */
async function verificarBackend() {
    try {
        const response = await fetch(`${API_BASE}/health`);

        if (!response.ok) {
            throw new Error('Backend no responde');
        }

        const resultado = await response.json();

        if (resultado.status === 'ok') {
            actualizarEstadoConexion(true);
            return true;
        }

        return false;

    } catch (error) {
        console.error('Error al verificar backend:', error);
        actualizarEstadoConexion(false);
        mostrarToast('No se puede conectar con el servidor. Verifica que esté corriendo.', 'error');
        return false;
    }
}

// Exportar funciones para uso global
// (En un proyecto moderno usaríamos ES6 modules, pero para simplicidad usamos global)
window.api = {
    obtenerFormulas,
    obtenerFormula,
    calcularFormula,
    obtenerHistorial,
    verificarBackend,
    mostrarToast,
    actualizarEstadoConexion
};

```


### Archivo: frontend/js/app.js

```javascript
// frontend/js/app.js
// ============================================
// QUÉ HACE: Lógica principal de la aplicación (controlador)
// CONSUME: api.js (funciones HTTP), graficos.js (renderizado Plotly)
// EXPONE: Funciones de inicialización y manejo de eventos
// RELACIONADO CON:
//   - Usa: api.js, graficos.js
//   - Manipula: DOM (index.html)
// ============================================

// Estado global de la aplicación
let formulasDisponibles = [];
let formulaActual = null;

/**
 * Inicializa la aplicación cuando el DOM está listo
 */
document.addEventListener('DOMContentLoaded', async () => {
    console.log('🚀 Inicializando aplicación...');

    // Verificar que el backend esté funcionando
    const backendOk = await api.verificarBackend();

    if (!backendOk) {
        api.mostrarToast('⚠️  El backend no está disponible. Inicia el servidor FastAPI.', 'warning');
        return;
    }

    // Cargar fórmulas disponibles
    await cargarFormulas();

    // Cargar historial
    await cargarHistorial();

    // Configurar event listeners
    configurarEventListeners();

    console.log('✅ Aplicación inicializada correctamente');
});

/**
 * Carga todas las fórmulas disponibles desde el backend
 */
async function cargarFormulas() {
    const selector = document.getElementById('formulaSelector');

    // Obtener fórmulas
    formulasDisponibles = await api.obtenerFormulas();

    if (formulasDisponibles.length === 0) {
        selector.innerHTML = '<option disabled selected>No hay fórmulas disponibles</option>';
        return;
    }

    // Limpiar selector
    selector.innerHTML = '';

    // Añadir opción por defecto
    const optionDefault = document.createElement('option');
    optionDefault.disabled = true;
    optionDefault.selected = true;
    optionDefault.textContent = 'Selecciona una fórmula...';
    selector.appendChild(optionDefault);

    // Añadir cada fórmula como opción
    formulasDisponibles.forEach(formula => {
        const option = document.createElement('option');
        option.value = formula.id;
        option.textContent = formula.nombre;
        option.dataset.categoria = formula.categoria;
        selector.appendChild(option);
    });

    // Seleccionar la primera fórmula automáticamente
    if (formulasDisponibles.length > 0) {
        selector.selectedIndex = 1; // Índice 1 (la primera fórmula real)
        await cargarFormulaSeleccionada();
    }
}

/**
 * Carga los detalles de la fórmula actualmente seleccionada
 */
async function cargarFormulaSeleccionada() {
    const selector = document.getElementById('formulaSelector');
    const formulaId = parseInt(selector.value);

    if (isNaN(formulaId)) {
        return;
    }

    // Obtener detalles completos de la fórmula
    formulaActual = await api.obtenerFormula(formulaId);

    if (!formulaActual) {
        return;
    }

    // Actualizar UI
    mostrarFormulaLatex(formulaActual.formula_latex);
    mostrarCategoria(formulaActual.categoria);
    generarInputsDinamicos(formulaActual);
}

/**
 * Muestra la fórmula LaTeX renderizada con MathJax
 * @param {string} latex - Fórmula en formato LaTeX
 */
function mostrarFormulaLatex(latex) {
    const display = document.getElementById('formulaDisplay');

    // Formatear para MathJax (delimitadores $$)
    display.innerHTML = `$$${latex}$$`;

    // Re-renderizar MathJax si está disponible
    if (window.MathJax) {
        MathJax.typesetPromise([display]).catch(err => {
            console.error('Error al renderizar LaTeX:', err);
        });
    }
}

/**
 * Muestra la categoría de la fórmula
 * @param {string} categoria - Nombre de la categoría
 */
function mostrarCategoria(categoria) {
    const badge = document.getElementById('categoriaDisplay');
    badge.textContent = categoria || 'Sin categoría';
}

/**
 * Diccionario de etiquetas amigables para variables comunes
 */
const ETIQUETAS_VARIABLES = {
    // Posiciones y coordenadas
    'x0': { label: 'Posición inicial x₀', placeholder: 'metros', unidad: 'm' },
    'y0': { label: 'Posición inicial y₀', placeholder: 'metros', unidad: 'm' },
    'x': { label: 'Coordenada x', placeholder: 'unidades', unidad: '' },

    // Velocidades
    'v': { label: 'Velocidad', placeholder: 'm/s', unidad: 'm/s' },
    'v0': { label: 'Velocidad inicial', placeholder: 'm/s', unidad: 'm/s' },

    // Aceleración y gravedad
    'a': { label: 'Aceleración a', placeholder: 'm/s²', unidad: 'm/s²' },
    'g': { label: 'Gravedad g', placeholder: 'm/s²', unidad: 'm/s²' },

    // Coeficientes matemáticos
    'A': { label: 'Coeficiente A', placeholder: 'número', unidad: '' },
    'B': { label: 'Coeficiente B', placeholder: 'número', unidad: '' },
    'C': { label: 'Coeficiente C', placeholder: 'número', unidad: '' },
    'b': { label: 'Coeficiente b', placeholder: 'número', unidad: '' },
    'c': { label: 'Coeficiente c', placeholder: 'número', unidad: '' },
    'k': { label: 'Constante k', placeholder: 'número', unidad: '' },

    // Variables paramétricas y polares
    't': { label: 'Parámetro t', placeholder: 'unidades', unidad: '' },
    'theta': { label: 'Ángulo θ', placeholder: 'radianes', unidad: 'rad' },
    'r': { label: 'Radio r', placeholder: 'unidades', unidad: '' },
    'omega': { label: 'Frecuencia angular ω', placeholder: 'rad/s', unidad: 'rad/s' },
    'phi': { label: 'Fase φ', placeholder: 'radianes', unidad: 'rad' }
};

/**
 * Genera inputs dinámicos según las variables de la fórmula
 * @param {Object} formula - Objeto fórmula con variables_usuario
 */
function generarInputsDinamicos(formula) {
    const container = document.getElementById('inputsContainer');
    container.innerHTML = '';

    // FIX: variables_usuario a veces viene como STRING en lugar de OBJECT
    // Cuando viene como string '{"x0": 0, "v0": 5}', hay que parsearlo
    let variables = formula.variables_usuario || {};

    if (typeof variables === 'string') {
        try {
            variables = JSON.parse(variables);
            console.log('✅ variables_usuario parseado de string a object');
        } catch (e) {
            console.error('❌ Error al parsear variables_usuario:', e);
            variables = {};
        }
    }

    // 1. Generar inputs para cada variable en variables_usuario
    Object.entries(variables).forEach(([nombreVar, valorDefecto]) => {
        const config = ETIQUETAS_VARIABLES[nombreVar] || {
            label: nombreVar,
            placeholder: 'valor',
            unidad: ''
        };

        const div = document.createElement('div');
        div.className = 'form-control w-full';

        const label = document.createElement('label');
        label.className = 'label';
        label.innerHTML = `<span class="label-text text-slate-300 text-sm">${config.label}</span>`;

        const input = document.createElement('input');
        input.type = 'number';
        input.name = nombreVar;
        input.id = `input_${nombreVar}`;
        input.className = 'input input-bordered input-sm bg-slate-700 text-slate-100 border-slate-600 focus:border-blue-500 w-full';
        input.placeholder = config.placeholder;
        input.step = '0.1';
        input.required = true;
        input.value = valorDefecto;

        div.appendChild(label);
        div.appendChild(input);
        container.appendChild(div);
    });

    // 2. Generar sliders para el rango (variable_rango_min, variable_rango_max)
    const rangoMin = {
        nombre: `${formula.variable_rango}_min`,
        label: `${formula.variable_rango} mínimo`,
        valor: formula.rango_min || 0,
        min: formula.rango_min !== null ? formula.rango_min - 10 : -10,
        max: formula.rango_max !== null ? formula.rango_max : 100
    };

    const rangoMax = {
        nombre: `${formula.variable_rango}_max`,
        label: `${formula.variable_rango} máximo`,
        valor: formula.rango_max || 10,
        min: formula.rango_min !== null ? formula.rango_min : 0,
        max: formula.rango_max !== null ? formula.rango_max + 10 : 100
    };

    [rangoMin, rangoMax].forEach(rango => {
        const div = document.createElement('div');
        div.className = 'form-control w-full';

        const labelContainer = document.createElement('div');
        labelContainer.className = 'flex justify-between items-center mb-1';

        const label = document.createElement('label');
        label.className = 'label-text text-slate-300 text-sm';
        label.textContent = rango.label;

        const valorDisplay = document.createElement('span');
        valorDisplay.id = `display_${rango.nombre}`;
        valorDisplay.className = 'text-blue-400 text-sm font-mono';
        valorDisplay.textContent = rango.valor;

        labelContainer.appendChild(label);
        labelContainer.appendChild(valorDisplay);

        const slider = document.createElement('input');
        slider.type = 'range';
        slider.name = rango.nombre;
        slider.id = `input_${rango.nombre}`;
        slider.className = 'range range-primary range-sm';
        slider.min = rango.min;
        slider.max = rango.max;
        slider.step = '0.1';
        slider.value = rango.valor;
        slider.required = true;

        // Actualizar display del valor cuando cambia el slider
        slider.addEventListener('input', (e) => {
            valorDisplay.textContent = e.target.value;
        });

        div.appendChild(labelContainer);
        div.appendChild(slider);
        container.appendChild(div);
    });
}

/**
 * Configura todos los event listeners de la aplicación
 */
function configurarEventListeners() {
    // Selector de fórmula
    const selector = document.getElementById('formulaSelector');
    selector.addEventListener('change', cargarFormulaSeleccionada);

    // Botón calcular
    const btnCalcular = document.getElementById('btnCalcular');
    btnCalcular.addEventListener('click', realizarCalculo);

    // Botón refrescar historial
    const btnRefrescar = document.getElementById('btnRefrescarHistorial');
    btnRefrescar.addEventListener('click', cargarHistorial);
}

/**
 * Realiza el cálculo con los valores ingresados
 */
async function realizarCalculo() {
    if (!formulaActual) {
        api.mostrarToast('Selecciona una fórmula primero', 'warning');
        return;
    }

    const btnCalcular = document.getElementById('btnCalcular');

    // Recopilar valores de los inputs
    const valores = {};
    const inputs = document.querySelectorAll('#inputsContainer input');
    let valido = true;

    inputs.forEach(input => {
        const valor = parseFloat(input.value);

        if (isNaN(valor) || input.value.trim() === '') {
            input.classList.add('input-error');
            valido = false;
        } else {
            input.classList.remove('input-error');
            valores[input.name] = valor;
        }
    });

    if (!valido) {
        api.mostrarToast('Por favor completa todos los campos correctamente', 'warning');
        return;
    }

    // Mostrar loading en el botón
    const textoOriginal = btnCalcular.innerHTML;
    btnCalcular.disabled = true;
    btnCalcular.innerHTML = '<span class="loading loading-spinner loading-sm"></span> Calculando...';

    try {
        // Llamar a la API para calcular
        const resultado = await api.calcularFormula(formulaActual.id, valores);

        if (!resultado) {
            throw new Error('No se obtuvo resultado del cálculo');
        }

        // Renderizar el gráfico
        graficos.renderizarGrafico(resultado, formulaActual);

        // Actualizar historial
        await cargarHistorial();

    } catch (error) {
        console.error('Error en el cálculo:', error);
        api.mostrarToast('Error al realizar el cálculo', 'error');
    } finally {
        // Restaurar botón
        btnCalcular.disabled = false;
        btnCalcular.innerHTML = textoOriginal;
    }
}

/**
 * Carga y muestra el historial de cálculos
 */
async function cargarHistorial() {
    const container = document.getElementById('historialContainer');

    // Obtener historial (últimos 5)
    const historial = await api.obtenerHistorial(5);

    if (historial.length === 0) {
        container.innerHTML = '<p class="text-slate-400 text-sm">No hay cálculos en el historial aún</p>';
        return;
    }

    // Generar cards de historial (layout vertical para panel lateral)
    const cardsHTML = historial.map((calculo, index) => {
        const formula = calculo.formulas || {};
        const fecha = new Date(calculo.created_at);
        const fechaFormateada = fecha.toLocaleString('es-ES', {
            day: '2-digit',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit'
        });

        const miniaturaId = `miniatura-${calculo.id}`;

        return `
            <div class="card bg-slate-600 shadow-md hover:bg-slate-500 transition-colors duration-200 cursor-pointer border border-slate-500"
                 data-calculo-id="${calculo.id}"
                 onclick="cargarCalculoDeHistorial(${calculo.id})">
                <div class="card-body p-3">
                    <h3 class="text-xs font-semibold text-blue-300 truncate">${formula.nombre || 'Sin nombre'}</h3>
                    <p class="text-xs text-slate-400">${fechaFormateada}</p>

                    <!-- Miniatura del gráfico -->
                    <div id="${miniaturaId}" class="h-16 mt-2 rounded bg-slate-700"></div>

                    <!-- Valores -->
                    <div class="text-xs text-slate-300 mt-2">
                        ${calculo.valores_entrada ? Object.entries(calculo.valores_entrada).map(([k, v]) =>
                            `<span class="badge badge-xs badge-outline mr-1 mb-1">${k}: ${v}</span>`
                        ).join('') : 'Sin datos'}
                    </div>
                </div>
            </div>
        `;
    }).join('');

    container.innerHTML = cardsHTML;

    // Renderizar miniaturas de gráficos (después de que el DOM esté actualizado)
    setTimeout(() => {
        historial.forEach(calculo => {
            if (calculo.resultado) {
                const miniaturaId = `miniatura-${calculo.id}`;
                graficos.renderizarMiniaturaGrafico(miniaturaId, calculo.resultado);
            }
        });
    }, 100);
}

/**
 * Carga un cálculo del historial (al hacer click)
 * @param {number} calculoId - ID del cálculo a cargar
 */
async function cargarCalculoDeHistorial(calculoId) {
    const historial = await api.obtenerHistorial(20);
    const calculo = historial.find(c => c.id === calculoId);

    if (!calculo) {
        api.mostrarToast('No se pudo cargar el cálculo', 'error');
        return;
    }

    // Cargar fórmula
    const selector = document.getElementById('formulaSelector');
    selector.value = calculo.formula_id;
    await cargarFormulaSeleccionada();

    // Rellenar inputs con los valores del historial
    if (calculo.valores_entrada) {
        Object.entries(calculo.valores_entrada).forEach(([nombre, valor]) => {
            const input = document.getElementById(`input_${nombre}`);
            if (input) {
                input.value = valor;
            }
        });
    }

    // Renderizar el gráfico
    if (calculo.resultado) {
        graficos.renderizarGrafico(calculo, calculo.formulas || {});
    }

    api.mostrarToast('Cálculo cargado desde el historial', 'info');

    // Scroll al inicio
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Exponer funciones globalmente para onclick en HTML
window.cargarCalculoDeHistorial = cargarCalculoDeHistorial;

// ============================================
// REDISEÑO V2.0: Toggle panel + Tabs 2D/3D
// 8 Enero 2026
// ============================================

/**
 * Inicializar funcionalidad del toggle del panel de controles
 */
function initToggleControls() {
    const toggleBtn = document.getElementById('toggleControls');
    const content = document.getElementById('controlsContent');
    const icon = document.getElementById('toggleIcon');
    
    if (!toggleBtn || !content) return;
    
    toggleBtn.addEventListener('click', () => {
        const isHidden = content.classList.contains('hidden');
        
        if (isHidden) {
            // Expandir
            content.classList.remove('hidden');
            toggleBtn.classList.remove('collapsed');
        } else {
            // Colapsar
            content.classList.add('hidden');
            toggleBtn.classList.add('collapsed');
        }
    });
}

/**
 * Inicializar funcionalidad de tabs 2D/3D
 */
function initTabs() {
    const tab2D = document.getElementById('tab2D');
    const tab3D = document.getElementById('tab3D');
    
    if (!tab2D || !tab3D) return;
    
    tab2D.addEventListener('click', () => {
        tab2D.classList.add('tab-active');
        tab3D.classList.remove('tab-active');
        console.log('🎨 Modo 2D activado');
        // TODO FASE 6.4: Filtrar fórmulas 2D
    });
    
    tab3D.addEventListener('click', () => {
        tab3D.classList.add('tab-active');
        tab2D.classList.remove('tab-active');
        console.log('🎨 Modo 3D activado');
        // TODO FASE 6.4: Filtrar fórmulas 3D
    });
}

// Inicializar cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        initToggleControls();
        initTabs();
    });
} else {
    // DOM ya está listo
    initToggleControls();
    initTabs();
}

```


### Archivo: frontend/js/graficos.js

```javascript
// frontend/js/graficos.js
// ============================================
// QUÉ HACE: Configuración y renderizado de gráficos con Plotly.js
// CONSUME: Datos de cálculos (arrays de puntos t, x)
// EXPONE: Funciones para crear y actualizar gráficos
// RELACIONADO CON:
//   - Usado por: frontend/js/app.js
//   - Usa: Plotly.js (librería global cargada vía CDN)
// ============================================

/**
 * Configuración global de Plotly (botones, comportamiento)
 */
const configPlotly = {
    responsive: true,                // Adaptar al tamaño del contenedor
    displayModeBar: true,            // Mostrar barra de herramientas
    displaylogo: false,              // No mostrar logo de Plotly
    modeBarButtonsToRemove: [        // Quitar botones innecesarios
        'lasso2d',
        'select2d'
    ],
    toImageButtonOptions: {          // Opciones del botón "Descargar como imagen"
        format: 'png',
        filename: 'formula_grafico',
        height: 800,
        width: 1200,
        scale: 2                     // Mayor resolución
    }
};

/**
 * Layout (diseño) del gráfico con tema oscuro elegante
 */
const layoutOscuro = {
    // Colores de fondo
    paper_bgcolor: '#1e293b',        // Fondo del "papel" (exterior)
    plot_bgcolor: '#1e293b',         // Fondo del área de gráfico

    // Tipografía
    font: {
        color: '#f8fafc',            // Color de texto (slate-50)
        family: 'Inter, sans-serif',
        size: 12
    },

    // Configuración del eje X
    xaxis: {
        title: {
            text: 't (tiempo)',
            font: { size: 14, color: '#94a3b8' }  // slate-400
        },
        gridcolor: '#334155',        // Color de las líneas de cuadrícula (slate-700)
        zerolinecolor: '#475569',    // Color de la línea del cero (slate-600)
        tickfont: { color: '#cbd5e1' },  // Color de los números (slate-300)
        showgrid: true,
        zeroline: true
    },

    // Configuración del eje Y
    yaxis: {
        title: {
            text: 'x (posición)',
            font: { size: 14, color: '#94a3b8' }
        },
        gridcolor: '#334155',
        zerolinecolor: '#475569',
        tickfont: { color: '#cbd5e1' },
        showgrid: true,
        zeroline: true
    },

    // Márgenes
    margin: {
        t: 50,   // Top
        r: 30,   // Right
        b: 60,   // Bottom
        l: 70    // Left
    },

    // Configuración de hover (tooltip)
    hovermode: 'closest',
    hoverlabel: {
        bgcolor: '#0f172a',         // Fondo del tooltip
        bordercolor: '#3b82f6',     // Borde azul
        font: {
            color: '#f8fafc',
            family: 'Inter, sans-serif',
            size: 13
        }
    },

    // Título del gráfico (se añade dinámicamente)
    title: {
        text: '',
        font: {
            size: 18,
            color: '#3b82f6',       // blue-500
            family: 'Inter, sans-serif'
        },
        x: 0.5,                     // Centrado
        xanchor: 'center'
    },

    // Mostrar leyenda
    showlegend: true,
    legend: {
        bgcolor: '#0f172a',
        bordercolor: '#334155',
        borderwidth: 1,
        font: { color: '#f8fafc' }
    }
};

/**
 * Renderiza un gráfico con los datos de un cálculo
 * ACTUALIZADO: Detecta automáticamente el tipo de datos (temporal, función o paramétrica)
 * @param {Object} datosCalculo - Objeto con resultado del cálculo
 * @param {Object} formula - Objeto con información de la fórmula
 */
function renderizarGrafico(datosCalculo, formula) {
    const contenedor = document.getElementById('graficoContainer');
    const placeholder = document.getElementById('placeholderGrafico');

    // Ocultar mensaje placeholder
    if (placeholder) {
        placeholder.style.display = 'none';
    }

    const resultado = datosCalculo.resultado;
    let xData, yData, xLabel, yLabel, hoverTemplate;

    // DETECTAR TIPO DE DATOS según las claves presentes
    if (resultado.t !== undefined) {
        // TIPO 1: Fórmulas temporales (t, x) o (t, y)
        xData = resultado.t;
        xLabel = 't (tiempo)';

        if (resultado.x !== undefined) {
            yData = resultado.x;
            yLabel = 'x (posición)';
            hoverTemplate = '<b>t</b>: %{x:.2f}<br><b>x</b>: %{y:.2f}<extra></extra>';
        } else if (resultado.y !== undefined) {
            yData = resultado.y;
            yLabel = 'y (altura)';
            hoverTemplate = '<b>t</b>: %{x:.2f}<br><b>y</b>: %{y:.2f}<extra></extra>';
        }

    } else if (resultado.theta !== undefined) {
        // TIPO 2: Curvas paramétricas polares (theta, x, y)
        // Graficar en plano cartesiano (x, y)
        xData = resultado.x;
        yData = resultado.y;
        xLabel = 'x';
        yLabel = 'y';
        hoverTemplate = '<b>x</b>: %{x:.2f}<br><b>y</b>: %{y:.2f}<extra></extra>';

    } else {
        // TIPO 3: Funciones matemáticas (x, y)
        xData = resultado.x;
        yData = resultado.y;
        xLabel = 'x';
        yLabel = 'y';
        hoverTemplate = '<b>x</b>: %{x:.2f}<br><b>y</b>: %{y:.2f}<extra></extra>';
    }

    // Configurar los datos de la traza (línea)
    const traza = {
        x: xData,
        y: yData,
        type: 'scatter',
        mode: 'lines',
        name: formula.nombre || 'Resultado',
        line: {
            color: '#3b82f6',        // blue-500
            width: 3,
            shape: 'spline',         // Línea suave
            smoothing: 1.3
        },
        hovertemplate: hoverTemplate
    };

    // Clonar el layout base y personalizar
    const layout = {
        ...layoutOscuro,
        title: {
            ...layoutOscuro.title,
            text: formula.nombre || 'Gráfico'
        },
        xaxis: {
            ...layoutOscuro.xaxis,
            title: { text: xLabel, font: { size: 14, color: '#94a3b8' } }
        },
        yaxis: {
            ...layoutOscuro.yaxis,
            title: { text: yLabel, font: { size: 14, color: '#94a3b8' } }
        }
    };

    // Para curvas paramétricas: aspect ratio 1:1 (escala igual en x e y)
    if (resultado.theta !== undefined) {
        layout.yaxis.scaleanchor = 'x';
        layout.yaxis.scaleratio = 1;
    }

    // Renderizar con Plotly (con animación)
    Plotly.newPlot(
        contenedor,
        [traza],
        layout,
        configPlotly
    );

    // Añadir animación de entrada
    contenedor.style.animation = 'fadeIn 0.5s ease-in';
}

/**
 * Actualiza un gráfico existente con nuevos datos (con animación)
 * @param {Object} datosCalculo - Nuevos datos del cálculo
 */
function actualizarGrafico(datosCalculo) {
    const contenedor = document.getElementById('graficoContainer');

    const { t, x } = datosCalculo.resultado;

    // Actualizar datos con animación suave
    Plotly.animate(
        contenedor,
        {
            data: [{
                x: t,
                y: x
            }]
        },
        {
            transition: {
                duration: 500,       // Duración de la animación en ms
                easing: 'cubic-in-out'
            },
            frame: {
                duration: 500
            }
        }
    );
}

/**
 * Limpia el gráfico y muestra el placeholder inicial
 */
function limpiarGrafico() {
    const contenedor = document.getElementById('graficoContainer');
    const placeholder = document.getElementById('placeholderGrafico');

    // Limpiar contenedor Plotly
    Plotly.purge(contenedor);

    // Mostrar placeholder
    if (placeholder) {
        placeholder.style.display = 'flex';
    }
}

/**
 * Renderiza una previsualización pequeña del gráfico (para historial)
 * ACTUALIZADO: Detecta automáticamente el tipo de datos
 * @param {string} contenedorId - ID del div donde renderizar
 * @param {Object} datos - Datos del cálculo (puede ser t,x o x,y o theta,x,y)
 */
function renderizarMiniaturaGrafico(contenedorId, datos) {
    let xData, yData;

    // Detectar tipo de datos (igual que en renderizarGrafico)
    if (datos.t !== undefined) {
        xData = datos.t;
        yData = datos.x || datos.y;
    } else if (datos.theta !== undefined) {
        xData = datos.x;
        yData = datos.y;
    } else {
        xData = datos.x;
        yData = datos.y;
    }

    const traza = {
        x: xData,
        y: yData,
        type: 'scatter',
        mode: 'lines',
        line: {
            color: '#3b82f6',
            width: 2
        },
        hoverinfo: 'skip'            // Sin hover en miniaturas
    };

    const layoutMiniatura = {
        paper_bgcolor: '#0f172a',
        plot_bgcolor: '#0f172a',
        margin: { t: 10, r: 10, b: 10, l: 10 },
        xaxis: {
            showgrid: false,
            showticklabels: false,
            zeroline: false
        },
        yaxis: {
            showgrid: false,
            showticklabels: false,
            zeroline: false
        },
        showlegend: false,
        hovermode: false
    };

    const configMiniatura = {
        displayModeBar: false,
        staticPlot: true             // Sin interacción
    };

    Plotly.newPlot(
        contenedorId,
        [traza],
        layoutMiniatura,
        configMiniatura
    );
}

/**
 * Renderiza un gráfico con animación (punto por punto)
 * NUEVO en v2.0: Usa el sistema de animación de animacion.js
 * @param {Object} datosCalculo - Objeto con resultado del cálculo
 * @param {Object} formula - Objeto con información de la fórmula
 * @param {boolean} conAnimacion - Si true, anima; si false, renderiza directo (default: true)
 */
function renderizarGraficoAnimado(datosCalculo, formula, conAnimacion = true) {
    const contenedor = document.getElementById('graficoContainer');
    const placeholder = document.getElementById('placeholderGrafico');

    // Ocultar mensaje placeholder
    if (placeholder) {
        placeholder.style.display = 'none';
    }

    const resultado = datosCalculo.resultado;

    // Si no hay sistema de animación o no se quiere animación, usar método tradicional
    if (!window.animacion || !conAnimacion) {
        renderizarGrafico(datosCalculo, formula);
        return;
    }

    // DETECTAR si es 2D o 3D
    const es3D = resultado.z !== undefined;

    if (es3D) {
        // Gráfico 3D con animación
        console.log('🎨 Renderizando gráfico 3D con animación');
        window.animacion.animarCurva3D(resultado, 5000);
    } else {
        // Gráfico 2D con animación
        console.log('🎨 Renderizando gráfico 2D con animación');

        // Preparar datos según el tipo
        let datos = { x: [], y: [] };

        if (resultado.t !== undefined) {
            // Fórmulas temporales (t, x) o (t, y)
            datos.x = resultado.t;
            datos.y = resultado.x || resultado.y;
        } else if (resultado.theta !== undefined) {
            // Curvas paramétricas polares
            datos.x = resultado.x;
            datos.y = resultado.y;
        } else {
            // Funciones matemáticas (x, y)
            datos.x = resultado.x;
            datos.y = resultado.y;
        }

        window.animacion.animarCurva2D(datos, 3000);
    }
}

// Exportar funciones para uso global
window.graficos = {
    renderizarGrafico,
    renderizarGraficoAnimado,  // ← NUEVA función con animación
    actualizarGrafico,
    limpiarGrafico,
    renderizarMiniaturaGrafico,
    configPlotly,
    layoutOscuro
};

```


## Carpeta: frontend/css


### Archivo: frontend/css/styles.css

```css
/* frontend/css/styles.css
 * ============================================
 * QUÉ HACE: Estilos custom que Tailwind/DaisyUI no cubren
 * PROPÓSITO: Animaciones, transiciones y efectos especiales
 * ============================================
 */

/* Animación de entrada para elementos */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Animación de escala */
@keyframes scaleIn {
    from {
        opacity: 0;
        transform: scale(0.95);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

/* Transición suave para cards */
.card {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
}

/* Efecto glow en botón principal */
.btn-primary {
    position: relative;
    overflow: hidden;
}

.btn-primary::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s;
}

.btn-primary:hover::before {
    left: 100%;
}

/* Efecto de hover en inputs */
.input:focus {
    transform: scale(1.01);
    transition: transform 0.2s ease;
}

/* Animación del loading spinner personalizado */
@keyframes pulse-glow {
    0%, 100% {
        box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.7);
    }
    50% {
        box-shadow: 0 0 0 10px rgba(59, 130, 246, 0);
    }
}

.loading.loading-ring {
    animation: pulse-glow 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

/* Estilo para el contenedor del gráfico */
#graficoContainer {
    animation: fadeIn 0.5s ease-in;
}

/* Transición suave para el selector */
.select {
    transition: all 0.2s ease;
}

.select:focus {
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
}

/* Hover effect para cards del historial */
#historialContainer .card {
    cursor: pointer;
    border: 1px solid transparent;
    transition: all 0.3s ease;
}

#historialContainer .card:hover {
    border-color: #3b82f6;
    box-shadow: 0 10px 40px rgba(59, 130, 246, 0.3);
}

/* Animación para notificaciones toast */
.toast .alert {
    animation: scaleIn 0.3s ease;
}

/* Efecto ripple en botones (opcional) */
.btn {
    position: relative;
    overflow: hidden;
}

.btn::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.3);
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
}

.btn:active::after {
    width: 300px;
    height: 300px;
}

/* Scrollbar personalizado para el historial */
#historialContainer::-webkit-scrollbar {
    height: 8px;
}

#historialContainer::-webkit-scrollbar-track {
    background: #1e293b;
    border-radius: 4px;
}

#historialContainer::-webkit-scrollbar-thumb {
    background: #475569;
    border-radius: 4px;
}

#historialContainer::-webkit-scrollbar-thumb:hover {
    background: #64748b;
}

/* Animación para badges */
.badge {
    transition: all 0.2s ease;
}

.badge:hover {
    transform: scale(1.05);
}

/* Placeholder del gráfico con animación sutil */
#placeholderGrafico {
    animation: fadeIn 0.8s ease;
}

#placeholderGrafico svg {
    animation: pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
    0%, 100% {
        opacity: 0.5;
    }
    50% {
        opacity: 0.8;
    }
}

/* Mejora visual para inputs con error */
.input-error {
    border-color: #ef4444 !important;
    animation: shake 0.3s;
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
}

/* Transición para el header */
header {
    animation: fadeIn 0.6s ease;
}

/* Footer con animación */
footer {
    animation: fadeIn 1s ease;
}

/* Smooth scroll en toda la página */
html {
    scroll-behavior: smooth;
}

/* Mejoras de accesibilidad: focus visible */
*:focus-visible {
    outline: 2px solid #3b82f6;
    outline-offset: 2px;
}

/* Ocultar outline en clicks de mouse pero mantenerlo en teclado */
*:focus:not(:focus-visible) {
    outline: none;
}

/* Estilo para el renderizado de MathJax */
#formulaDisplay .MathJax {
    color: #f8fafc !important;
}

/* Responsive: ajustes para móvil */
@media (max-width: 768px) {
    .card {
        transform: none;
    }

    .card:hover {
        transform: translateY(-2px);
    }

    #historialContainer {
        -webkit-overflow-scrolling: touch;
    }
}

/* Animaciones de carga inicial */
.container {
    animation: fadeIn 0.8s ease;
}

/* Efecto de brillo en el logo */
header .bg-blue-500 {
    box-shadow: 0 0 20px rgba(59, 130, 246, 0.4);
    transition: box-shadow 0.3s ease;
}

header .bg-blue-500:hover {
    box-shadow: 0 0 30px rgba(59, 130, 246, 0.6);
    transform: scale(1.05);
    transition: all 0.3s ease;
}

/* Estilo especial para los valores en el historial */
.badge-xs {
    font-size: 0.65rem;
    padding: 0.2rem 0.4rem;
}

/* Mejora visual para el estado de conexión */
#statusIndicator.bg-green-500 {
    box-shadow: 0 0 10px rgba(34, 197, 94, 0.6);
    animation: pulse-green 2s infinite;
}

@keyframes pulse-green {
    0%, 100% {
        box-shadow: 0 0 10px rgba(34, 197, 94, 0.6);
    }
    50% {
        box-shadow: 0 0 15px rgba(34, 197, 94, 0.9);
    }
}

/* ============================================
 * REDISEÑO V2.0 - 8 Enero 2026
 * Inputs numéricos sin spinners (flechas)
 * ============================================ */

/* Ocultar spinners en inputs type="number" */
input[type="number"] {
    -webkit-appearance: textfield;
    -moz-appearance: textfield;
    appearance: textfield;
}

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}

/* Para Firefox */
input[type="number"] {
    -moz-appearance: textfield;
}

/* ============================================
 * REDISEÑO V2.0 - LAYOUT VERTICAL
 * 8 Enero 2026 - Gráfico protagonista
 * ============================================ */

/* Main layout vertical */
.main-redesign {
    display: flex;
    flex-direction: column;
    height: calc(100vh - 140px); /* EXACTA: viewport - header - footer */
    gap: 0;
    padding: 0;
    margin: 0;
    max-width: 100%;
    overflow: hidden; /* Prevenir scroll en el main */
}

/* Área de visualización: 75-80% de la pantalla */
.visualization-area-redesign {
    flex: 1 1 auto; /* Crecer y encoger según espacio */
    padding: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden; /* No scroll en esta área */
}

.graph-container-redesign {
    width: 100%;
    max-width: 1800px;
    height: 100%; /* Usar 100% del contenedor padre */
    background: #1e293b;
    border-radius: 12px;
    border: 1px solid #334155;
    overflow: hidden;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
}

/* Panel de controles en la parte inferior */
.controls-panel-redesign {
    background: #0f172a;
    border-top: 1px solid #334155;
    width: 100%;
}

/* Botón toggle para colapsar/expandir */
.toggle-controls-btn {
    width: 100%;
    padding: 0.75rem;
    background: #1e293b;
    border: none;
    color: #3b82f6;
    font-weight: 600;
    font-size: 0.875rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    cursor: pointer;
    transition: all 0.2s ease;
}

.toggle-controls-btn:hover {
    background: #334155;
}

.toggle-controls-btn svg {
    transition: transform 0.3s ease;
}

.toggle-controls-btn.collapsed svg {
    transform: rotate(180deg);
}

/* Contenido del panel (colapsable) */
.controls-content-redesign {
    max-height: 600px;
    overflow-y: auto;
    transition: max-height 0.4s ease, opacity 0.3s ease;
    padding: 1rem;
}

.controls-content-redesign.hidden {
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    padding: 0;
}

/* Tabs 2D/3D */
.tab-redesign {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    border: 1px solid #334155;
    background: #1e293b;
    color: #94a3b8;
    border-radius: 8px;
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
}

.tab-redesign:hover {
    background: #334155;
    color: #f1f5f9;
}

.tab-redesign.tab-active {
    background: #3b82f6;
    color: white;
    border-color: #3b82f6;
    box-shadow: 0 0 15px rgba(59, 130, 246, 0.4);
}

/* Responsive */
@media (max-width: 768px) {
    .visualization-area-redesign {
        min-height: 60vh;
        padding: 0.5rem;
    }
    
    .graph-container-redesign {
        min-height: 60vh;
        border-radius: 8px;
    }
    
    .controls-content-redesign {
        max-height: 500px;
    }
}

@media (min-width: 1920px) {
    .graph-container-redesign {
        max-width: 2200px;
        min-height: 75vh;
    }
}

@media (min-width: 2560px) {
    .graph-container-redesign {
        max-width: 2600px;
        min-height: 80vh;
    }
}

```


### Archivo: frontend/index.html

```html
<!DOCTYPE html>
<html lang="es" class="dark" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualizador de Fórmulas Matemáticas</title>

    <!-- Google Fonts: Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <!-- Tailwind CSS + DaisyUI -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@4.4.19/dist/full.min.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- Plotly.js para gráficos interactivos -->
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>

    <!-- MathJax para renderizar fórmulas LaTeX -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script>
        // Configuración de MathJax ANTES de cargar el script
        MathJax = {
            tex: {
                inlineMath: [['\\(', '\\)']],
                displayMath: [['$$', '$$']],
                processEscapes: true
            },
            svg: {
                fontCache: 'global'
            }
        };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <!-- Estilos custom -->
    <link rel="stylesheet" href="css/styles.css">

    <!-- Configuración Tailwind -->
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-slate-900 text-slate-50 font-sans antialiased min-h-screen">

    <!-- HEADER -->
    <header class="bg-slate-800 shadow-lg border-b border-slate-700">
        <div class="container mx-auto px-4 py-4">
            <!-- Línea superior: Logo + Estado -->
            <div class="flex items-center justify-between mb-3">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 bg-blue-500 rounded-lg flex items-center justify-center">
                        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                        </svg>
                    </div>
                    <div>
                        <h1 class="text-xl font-bold text-slate-50">Visualizador de Fórmulas</h1>
                        <p class="text-xs text-slate-400">Matemáticas y Física Interactivas</p>
                    </div>
                </div>
                <div class="badge badge-md bg-blue-500 text-white border-0">
                    <span class="loading loading-ring loading-xs mr-2" id="statusIndicator"></span>
                    <span id="statusText">Conectado</span>
                </div>
            </div>

            <!-- Tabs 2D/3D -->
            <div class="flex items-center gap-2">
                <button id="tab2D" class="tab-redesign tab-active">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" />
                    </svg>
                    <span>Gráficos 2D</span>
                </button>
                <button id="tab3D" class="tab-redesign">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4" />
                    </svg>
                    <span>Gráficos 3D</span>
                </button>
            </div>
        </div>
    </header>

    <!-- MAIN CONTENT -->
    <main class="px-4 py-6 max-w-full">

        <!-- Grid 2 columnas: Gráfico (80%) + Panel (20%) -->
        <div class="grid grid-cols-1 lg:grid-cols-5 gap-4">

            <!-- ÁREA DE VISUALIZACIÓN: Gráfico (IZQUIERDA - 80%) -->
            <div class="lg:col-span-4">
                <div class="card bg-slate-800 shadow-xl border border-slate-700" style="min-height: calc(100vh - 200px);">
                    <div class="card-body p-4">
                        <!-- Contenedor del gráfico Plotly -->
                        <div id="graficoContainer" class="w-full" style="min-height: calc(100vh - 240px);">
                            <!-- Mensaje inicial -->
                            <div id="placeholderGrafico" class="flex flex-col items-center justify-center h-full text-slate-400 space-y-4" style="min-height: calc(100vh - 240px);">
                                <svg class="w-24 h-24 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" />
                                </svg>
                                <p class="text-lg">Selecciona una fórmula y haz clic en <strong class="text-blue-400">Calcular</strong></p>
                                <p class="text-sm text-slate-500">El gráfico interactivo aparecerá aquí</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PANEL DERECHO: Controles (DERECHA - 20%) -->
            <div class="lg:col-span-1">
                <!-- Grid horizontal: selector, variables, historial -->
                <div class="card bg-slate-800 shadow-xl border border-slate-700">
                    <div class="card-body">
                        <h2 class="card-title text-blue-400 mb-4">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                            </svg>
                            Configuración
                        </h2>

                        <!-- Selector de fórmula -->
                        <div class="form-control w-full">
                            <label class="label">
                                <span class="label-text text-slate-300 font-medium">Seleccionar Fórmula</span>
                            </label>
                            <select id="formulaSelector" class="select select-bordered bg-slate-700 text-slate-100 w-full border-slate-600 focus:border-blue-500">
                                <option disabled selected>Cargando fórmulas...</option>
                            </select>
                        </div>

                        <!-- Fórmula LaTeX -->
                        <div class="mt-4 p-4 bg-slate-700 rounded-lg border border-slate-600">
                            <p class="text-xs text-slate-400 mb-2">Fórmula:</p>
                            <div id="formulaDisplay" class="text-center text-lg overflow-x-auto">
                                $$...$$
                            </div>
                        </div>

                        <!-- Categoría -->
                        <div class="mt-2">
                            <span id="categoriaDisplay" class="badge badge-outline border-blue-400 text-blue-400"></span>
                        </div>

                        <!-- Inputs dinámicos -->
                        <div id="inputsContainer" class="mt-6 space-y-3">
                            <!-- Se generan dinámicamente con JavaScript -->
                        </div>

                        <!-- Botón Calcular -->
                        <button id="btnCalcular" class="btn btn-primary w-full mt-6 bg-blue-500 hover:bg-blue-600 border-0 text-white shadow-lg shadow-blue-500/50">
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                            </svg>
                            Calcular y Graficar
                        </button>

                        <!-- HISTORIAL DE CÁLCULOS (Colapsable) -->
                        <div class="collapse collapse-arrow bg-slate-700 mt-6 border border-slate-600">
                            <input type="checkbox" id="toggleHistorial" />
                            <div class="collapse-title text-sm font-medium text-blue-400 flex items-center">
                                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                Historial
                                <button id="btnRefrescarHistorial" class="btn btn-xs btn-ghost text-slate-400 hover:text-blue-400 ml-auto" onclick="event.stopPropagation();">
                                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                                    </svg>
                                </button>
                            </div>
                            <div class="collapse-content">
                                <!-- Contenedor de cards de historial (vertical) -->
                                <div id="historialContainer" class="space-y-2 max-h-96 overflow-y-auto">
                                    <!-- Se generan dinámicamente con JavaScript -->
                                    <p class="text-slate-400 text-xs">Cargando historial...</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- FOOTER -->
    <footer class="bg-slate-800 border-t border-slate-700 mt-12">
        <div class="container mx-auto px-4 py-6">
            <div class="flex flex-col md:flex-row items-center justify-between text-sm text-slate-400">
                <p>
                    Proyecto educativo - Visualización de Fórmulas Matemáticas
                </p>
                <p class="mt-2 md:mt-0">
                    Stack: <span class="text-blue-400">FastAPI</span> +
                    <span class="text-blue-400">Supabase</span> +
                    <span class="text-blue-400">Plotly.js</span>
                </p>
            </div>
        </div>
    </footer>

    <!-- Toast notifications (DaisyUI) -->
    <div class="toast toast-end" id="toastContainer">
        <!-- Notificaciones dinámicas -->
    </div>

    <!-- Scripts: Orden de carga importante -->
    <script src="js/api.js"></script>
    <script src="js/animacion.js"></script>
    <script src="js/graficos.js"></script>
    <script src="js/app.js"></script>
</body>
</html>

```


---

# 🗄️ BASE DE DATOS (Supabase)


## Tabla: formulas
Columnas:
- id
- nombre
- formula_latex
- variable_rango
- rango_min
- rango_max
- rango_dinamico
- variables_usuario
- categoria
- created_at

## Tabla: calculos
Columnas:
- id
- formula_id
- valores_entrada
- resultado
- created_at

**Relaciones:**
- calculos.formula_id → formulas.id (FK)


---

## 📊 ESTADÍSTICAS

- **Total líneas de código:** ~26
- **Archivos incluidos:** Backend (Python) + Frontend (JS/HTML/CSS)
- **Esquema BD:** Supabase (PostgreSQL)

## 🎯 CÓMO USAR ESTE ARCHIVO EN GOOGLE AI STUDIO

1. **Sube este archivo** a Google AI Studio (botón +)
2. **Sube también las capturas** de los errores (si las tienes)
3. **Sube el documento de problemas:** `docs/contexto_opus/20260108_estado_fase_6_4_problemas.md`

4. **Usa este prompt:**

```
Analiza este proyecto Full Stack de visualización de fórmulas.

CONTEXTO:
- Backend: Python/FastAPI en Railway
- Frontend: JS Vanilla en Cloudflare
- BD: Supabase (PostgreSQL)

ESTADO ACTUAL:
- Backend 3D completo ✅
- Frontend 3D con 5 problemas ❌

Lee el archivo "20260108_estado_fase_6_4_problemas.md" para ver los problemas.

PREGUNTA:
¿Ves los 5 problemas identificados?
¿Hay errores adicionales que Claude no detectó?
¿Las soluciones propuestas son correctas?
Dame código específico para arreglar cada problema.
```

---

**FIN DEL CONTEXTO**
**Generado con:** Claude Sonnet 4.5
