# Proyecto Web Fórmulas Matemáticas - Documento Maestro

**Autor:** Juan Manuel (51 años, nivel B2 Ciencia de Datos UOC)
**Fecha inicio:** 28 diciembre 2024
**Objetivo:** Aprender arquitectura web completa mediante proyecto práctico

---

## 1. CONTEXTO Y OBJETIVO

### ¿Qué es esto?
Una web de visualización de fórmulas matemáticas/físicas con animaciones interactivas. El objetivo NO es solo que funcione, sino **entender cómo se conecta todo el stack**.

### Flujo de la aplicación
1. Usuario selecciona una fórmula
2. Introduce valores para los parámetros
3. Python calcula el resultado
4. Se guarda en base de datos (historial)
5. Se muestra animación gráfica interactiva

### Método de aprendizaje
- **Socrático:** Entender el porqué, no solo copiar código
- **Incremental:** Primero lo mínimo que funcione, luego añadimos
- **Documentado:** Todo queda registrado en markdown

---

## 2. STACK TECNOLÓGICO

| Capa | Tecnología | Función |
|------|------------|---------|
| Frontend | HTML + CSS + JS | Interfaz visual, formularios, animaciones |
| Backend | Python + FastAPI | Lógica, validación, cálculos |
| Base de datos | Supabase (PostgreSQL) | Almacenamiento persistente en la nube |
| Gráficos | Plotly / D3 / Chart.js | Visualizaciones animadas |
| Despliegue | Render (Python) + Netlify/Pages (HTML) | Hosting gratuito |

**Nota:** Vercel descartado por razones éticas del usuario.

---

## 3. ARQUITECTURA DE TRES CAPAS (Analogía del Restaurante)

### Frontend = Comedor
- Lo que ve el cliente
- HTML (estructura), CSS (estilo), JS (interactividad)
- **NO expone endpoints**, solo consume
- Captura datos del usuario y los envía al backend

### Backend = Cocina  
- Donde se procesa todo
- Python + FastAPI
- Recibe peticiones, valida, calcula, guarda
- **DOBLE CARA:**
  - Servidor para frontend (expone endpoints)
  - Cliente para Supabase (consume endpoints)

### Base de Datos = Despensa
- Donde se guarda todo
- Supabase (PostgreSQL en la nube)
- **Solo expone endpoints** (no consume)
- NO interactúa directamente con frontend

---

## 4. FLUJO DE DATOS (DOS SALTOS)

```
Usuario pulsa botón en HTML
         ↓
   [SALTO 1] 
Frontend → POST JSON → Backend (FastAPI)
         ↓
Python recibe, valida, procesa, calcula
         ↓
   [SALTO 2]
Backend → API REST → Supabase
         ↓
Supabase guarda en tabla PostgreSQL
         ↓
   RESPUESTA (camino inverso)
Supabase → Python → Frontend → Usuario ve resultado
```

### Concepto clave: Python como "switch"
- **Cara hacia arriba:** Servidor (expone `/calcular`, `/historial`)
- **Cara hacia abajo:** Cliente (consume `/rest/v1/formulas`)

---

## 5. ENDPOINTS EXPLICADOS

### ¿Qué es un endpoint?
Una **dirección URL específica que activa una función concreta**.
Analogía: Ventanillas de atención al cliente.

### Ejemplos en nuestro proyecto

| Endpoint | Quién lo expone | Quién lo consume | Función |
|----------|-----------------|------------------|---------|
| `/api/calcular` | Python | Frontend (JS) | Recibe fórmula + valores |
| `/api/historial` | Python | Frontend (JS) | Devuelve cálculos guardados |
| `/rest/v1/formulas` | Supabase | Python | Obtener lista de fórmulas |
| `/rest/v1/calculos` | Supabase | Python | Guardar/leer cálculos |

---

## 6. JSON COMO PEGAMENTO UNIVERSAL

### ¿Qué es?
Formato de **texto plano** que permite comunicación entre lenguajes diferentes.

### ¿Por qué es importante?
- Frontend habla JavaScript
- Backend habla Python
- Base de datos habla SQL
- **JSON es el idioma común** que todos entienden

### Ejemplo
```json
{
  "formula": "mru",
  "valores": {
    "x0": 0,
    "v": 5,
    "t": 10
  }
}
```

---

## 7. LAS 15 FÓRMULAS INICIALES

### Física (6)
| # | Nombre | Fórmula | Var. rango |
|---|--------|---------|------------|
| 1 | MRU | x = x₀ + vt | t |
| 2 | MRUA | x = x₀ + v₀t + ½at² | t |
| 3 | Caída libre | y = ½gt² | t |
| 4 | Tiro parabólico | x = v₀cos(θ)t, y = v₀sin(θ)t - ½gt² | t |
| 5 | Péndulo simple | T = 2π√(L/g) | t |
| 6 | Onda armónica | y = Asin(kx - ωt) | t |

### Matemáticas (4)
| # | Nombre | Fórmula | Var. rango |
|---|--------|---------|------------|
| 7 | Parábola | y = ax² + bx + c | x |
| 8 | Círculo | x² + y² = r² | θ |
| 9 | Seno | y = Asin(ωt + φ) | t |
| 10 | Exponencial | y = e^(kx) | x |

### Curvas exóticas (5)
| # | Nombre | Fórmula | Var. rango |
|---|--------|---------|------------|
| 11 | Espiral logarítmica | r = ae^(bθ) | θ |
| 12 | Cicloide | x = r(θ - sinθ), y = r(1 - cosθ) | θ |
| 13 | Lemniscata | r² = a²cos(2θ) | θ |
| 14 | Cardioide | r = a(1 + cosθ) | θ |
| 15 | Rosa 3 pétalos | r = cos(3θ) | θ |

### Escalabilidad futura
Tras dominar estas 15, añadir conjuntos temáticos:
- Cinemática completa (15)
- Fluidos (15)
- Termodinámica (15)
- Electromagnetismo (15)

---

## 8. VARIABLES Y RANGOS

### Tipos de variables

**Variables de entrada (usuario elige):**
- Amplitud, velocidad, aceleración, ángulo, constantes
- Valores fijos para cada cálculo

**Variables de rango (para animación):**
- `t` (tiempo): física y ondas
- `x`: funciones matemáticas
- `θ` (theta): curvas polares/paramétricas

### Configuración por fórmula
Cada fórmula define independientemente:
- Qué variable es de rango
- Límite inferior
- Límite superior
- Paso de incremento

**Decisión arquitectónica:** Repetir configuración en cada fórmula (no normalizar). Razón: independencia y claridad sobre ahorro de espacio.

---

## 9. ESTRUCTURA DE BASE DE DATOS

### Tabla: `formulas`
```sql
CREATE TABLE formulas (
  id BIGINT PRIMARY KEY,
  nombre TEXT NOT NULL,
  formula_latex TEXT,           -- Para mostrar bonita
  variable_rango TEXT,          -- t, x, θ
  rango_min FLOAT,
  rango_max FLOAT,
  rango_dinamico BOOLEAN,       -- Si depende de otro valor
  variables_usuario JSONB,      -- {nombre: valor_defecto}
  categoria TEXT,               -- física/matemáticas/curvas
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Tabla: `calculos` (historial)
```sql
CREATE TABLE calculos (
  id BIGINT PRIMARY KEY,
  formula_id BIGINT REFERENCES formulas(id),
  valores_entrada JSONB,
  resultado JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## 10. SUPABASE - CONFIGURACIÓN

### ¿Qué es Supabase?
Base de datos PostgreSQL en la nube con API REST automática.
- Alternativa open source a Firebase
- Genera endpoints automáticamente para cada tabla

### Credenciales necesarias
- **URL del proyecto:** `https://xxxxxx.supabase.co`
- **API Key (service_role):** Para Python (SECRETA)
- **API Key (anon):** Para frontend si fuera necesario

### Archivo .env (NUNCA subir a GitHub)
```
SUPABASE_URL=https://xxxxxx.supabase.co
SUPABASE_KEY=tu_service_role_key_aqui
```

### Tutorial rápido de creación
1. Ir a [supabase.com](https://supabase.com)
2. Crear cuenta / Login
3. "New Project" → Nombre, contraseña BD, región EU West
4. **Security Options:**
   - ✅ Data API + Connection String
   - ✅ Use public schema for Data API
5. Esperar 1-2 minutos
6. Settings → API → Copiar URL y service_role key
7. Table Editor → Crear tablas

---

## 11. SEGURIDAD (Resumen de conversación con Gemini)

### Arquitectura segura
```
HTML (Tonto) → POST → Python (Cerebro) → API → Supabase (Almacén)
```
El usuario NUNCA toca la base de datos directamente.

### Las dos llaves de Supabase
- **anon/public key:** Para frontend (segura con RLS)
- **service_role key:** Para backend Python (SECRETA, se salta RLS)

### Protecciones en Python
1. **Validación de tipos:** Pydantic en FastAPI
2. **Validación de lógica:** if cantidad <= 0: error
3. **Sanitización:** Limpiar inputs de scripts maliciosos
4. **CORS:** Solo aceptar peticiones de tu dominio

### Protecciones adicionales (futuro)
- **Cloudflare:** Escudo contra DDoS (gratis)
- **Rate Limiting:** Máximo peticiones por minuto
- **RLS en Supabase:** Si hay usuarios con login

### Hosting gratuito
- **Python:** Render.com (sleep de 15 min en plan gratis)
- **HTML:** Netlify / GitHub Pages / Cloudflare Pages
- **Base de datos:** Supabase (500MB gratis)

---

## 12. METODOLOGÍA DE TRABAJO

### División de roles

**Claude Opus (chat principal):**
- Arquitecto y tutor pedagógico
- Diseño de estructura
- Explicaciones conceptuales
- Validación de comprensión
- **NO ejecuta código**

**Claude Code (Sonnet):**
- Ejecuta código según instrucciones
- Documenta en `bitacora.md`
- Implementa sin tomar decisiones arquitectónicas

### Reglas del proyecto
- ❌ No generar código para ejecutar (eso lo hace Claude Code)
- ❌ No avanzar a la siguiente capa sin cerrar la anterior
- ❌ No asumir que sabe algo solo porque lo hemos mencionado
- ✅ Preguntas tipo: "¿Qué crees que pasa cuando...?"
- ✅ Analogías con conceptos ya vistos
- ✅ Validar cada paso antes de seguir
- ✅ Juan marca el ritmo

### Entregables para Claude Code
Cuando un paso esté listo, generar bloque con:
- Qué archivo crear/modificar
- Qué debe hacer ese código
- Cómo se conecta con las otras piezas
- Qué resultado esperar para validar

---

## 13. CONCEPTOS CLAVE APRENDIDOS

### El backend tiene "doble cara"
- Servidor para frontend (expone endpoints)
- Cliente para Supabase (consume endpoints)

### JSON es el pegamento
- Independiente del lenguaje
- Texto plano legible
- Estándar universal

### Endpoints = Ventanillas
- Direcciones URL específicas
- Activan funciones concretas
- Se consumen con peticiones HTTP

### Normalizar vs Desnormalizar
- **Normalizar:** Separar en tablas relacionadas
- **Desnormalizar:** Repetir datos para independencia
- Para 15 fórmulas: mejor desnormalizar (claridad > ahorro)

---

## 14. ESTADO ACTUAL DEL PROYECTO

### ✅ Completado
- Concepto del proyecto definido
- Stack tecnológico seleccionado
- 15 fórmulas iniciales identificadas
- Variables y rangos analizados
- Arquitectura de tres capas comprendida
- Flujo de datos (dos saltos) entendido
- Concepto de endpoints clarificado
- Supabase como base de datos explicado
- Metodología de trabajo establecida
- Seguridad básica documentada
- Estructura de carpetas creada
- CLAUDE.md para Claude Code listo
- Proyecto Supabase creado (EU West - Ireland)
- Credenciales configuradas en .env
- Tabla `formulas` creada
- Tabla `calculos` creada
- Fórmula de prueba (MRU) insertada

### ⏳ Pendiente
- Implementar primer endpoint en Python
- Conectar Python con Supabase
- Crear frontend básico
- Conectar frontend con backend

### 🔮 Futuro (después de funcionar)
- Autenticación de usuarios
- RLS en Supabase
- Cloudflare como escudo
- Rate limiting
- Tests automáticos
- Despliegue público

---

## 15. PRÓXIMOS PASOS INMEDIATOS

1. **Juan crea proyecto en Supabase** (tutorial en sección 10)
2. **Juan copia URL y API key al archivo .env**
3. **Creamos tablas en Supabase**
4. **Claude Code implementa primer endpoint**
5. **Primera prueba: obtener lista de fórmulas**

---

*Documento generado: 29 diciembre 2024*
*Ubicación: /Volumes/Akitio01/Claude_MCP/formulas-web/docs/MAESTRO.md*
