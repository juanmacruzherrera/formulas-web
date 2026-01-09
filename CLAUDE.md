# CLAUDE.md - Instrucciones para Claude Code

## 📋 ESTADO ACTUAL: FASE 6 COMPLETADA ✅

**FASE 6: REDISEÑO v2.0 + SISTEMA 3D COMPLETO**

**🎉 ÚLTIMA ACTUALIZACIÓN: 9 Enero 2026**

### ✅ TODO COMPLETADO Y FUNCIONAL

**📖 DOCUMENTOS CLAVE:**
1. **FIXES APLICADOS (9 Enero):** `docs/5_FIXES_EXACTOS.md` ⭐ **NUEVO**
2. **PLAN ORIGINAL (Opus):** `docs/REDISENO_COMPLETO_V2.md`
3. **ESTADO ANTERIOR (8 Enero):** `docs/contexto_opus/20260108_estado_fase_6_4_problemas.md` (RESUELTO)
4. **REGISTRO DE CAMBIOS:** `docs/aprendizaje/17_rediseno_v2.md`
5. **CONTEXTO PARA GEMINI:** `docs/gemini/` (Actualizado con código funcional)

**🚀 SISTEMA FUNCIONANDO AL 100%:**
- ✅ Tabs 2D/3D con filtrado dinámico
- ✅ Renderizado 3D automático (Plotly scatter3d)
- ✅ Lorenz sin errores NaN (protección implementada)
- ✅ Inputs limpios sin spinners
- ✅ Gráfico protagonista 80% pantalla
- ✅ 4 fórmulas 3D funcionando (Hélice, Lorenz, Toro, Ondas)
- ✅ 15 fórmulas 2D funcionando

**🎯 OBJETIVOS CUMPLIDOS:**
1. ✅ **Inputs limpios** - Sin spinners, escribir números directamente
2. ✅ **Separar 2D y 3D** - Tabs funcionales con filtrado por categoria
3. ⏳ **Animación temporal** - Infraestructura lista, pendiente activar
4. ✅ **Gráfico protagonista** - 80% de la pantalla
5. ✅ **Responsive** - Layout adaptativo
6. ✅ **Nuevas fórmulas 3D** - Hélice, Lorenz, Toro, Ondas implementadas

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

## 📅 HISTORIAL DE ACTUALIZACIONES

### 9 Enero 2026 - FASE 6 COMPLETADA ✅
- ✅ Sistema 3D completo con 5 fixes aplicados
- ✅ Tabs 2D/3D con filtrado dinámico funcionando
- ✅ Renderizado 3D automático con Plotly
- ✅ Lorenz protegido contra NaN/Inf
- ✅ 19 fórmulas totales (15 en 2D, 4 en 3D)

### 8 Enero 2026 - Problemas identificados
- Backend 3D implementado
- Frontend con 5 problemas críticos documentados

### 29 Diciembre 2024 - Inicio FASE 6
- Rediseño UI v2.0 planificado

---

*Última actualización: 9 Enero 2026*
