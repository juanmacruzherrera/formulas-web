# INSTRUCCIONES FASE 3: Frontend Elegante

> **Objetivo:** Crear un frontend visualmente atractivo, moderno y funcional.
> **Prioridad:** Elegancia visual + Buena UX + Código limpio

---

## STACK FRONTEND ELEGIDO

| Tecnología | Versión/CDN | Por qué |
|------------|-------------|---------|
| **Tailwind CSS** | CDN última | Estilos modernos, Claude lo domina perfectamente |
| **DaisyUI** | CDN última | Componentes bonitos sobre Tailwind (botones, cards, modals) |
| **Plotly.js** | CDN última | Gráficos interactivos, animaciones, zoom, hover |
| **Vanilla JS** | ES6+ | Simple, sin frameworks innecesarios |
| **Google Fonts** | Inter | Tipografía moderna y limpia |

---

## DISEÑO VISUAL DESEADO

### Paleta de colores (modo oscuro elegante)
```
Fondo principal:    #0f172a (slate-900)
Fondo cards:        #1e293b (slate-800)
Acentos:            #3b82f6 (blue-500)
Texto principal:    #f8fafc (slate-50)
Texto secundario:   #94a3b8 (slate-400)
Éxito:              #22c55e (green-500)
Error:              #ef4444 (red-500)
```

### Layout general
```
┌─────────────────────────────────────────────────────────────────┐
│  HEADER: Logo + Título "Visualizador de Fórmulas"               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────┐  ┌─────────────────────────────────┐   │
│  │                     │  │                                 │   │
│  │  PANEL IZQUIERDO    │  │     ÁREA DE VISUALIZACIÓN       │   │
│  │                     │  │                                 │   │
│  │  • Selector fórmula │  │     [GRÁFICO PLOTLY GRANDE]     │   │
│  │  • Inputs variables │  │                                 │   │
│  │  • Botón calcular   │  │     Con animación y zoom        │   │
│  │  • Fórmula LaTeX    │  │                                 │   │
│  │                     │  │                                 │   │
│  └─────────────────────┘  └─────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  HISTORIAL: Últimos cálculos (cards horizontales)       │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  FOOTER: "Proyecto educativo - Stack: FastAPI + Supabase"       │
└─────────────────────────────────────────────────────────────────┘
```

---

## TAREA 3.1: Estructura HTML base

### Archivo: `frontend/index.html`

**Requisitos:**
1. HTML5 semántico
2. Cargar CDNs: Tailwind, DaisyUI, Plotly, MathJax (para LaTeX)
3. Estructura responsive (móvil primero)
4. Tema oscuro por defecto
5. Fuente Inter de Google Fonts

**CDNs a incluir:**
```html
<!-- Tailwind + DaisyUI -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@4.4.19/dist/full.min.css" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>

<!-- Plotly para gráficos -->
<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>

<!-- MathJax para renderizar LaTeX -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

**Componentes DaisyUI a usar:**
- `card` - Para paneles
- `select` - Para selector de fórmulas
- `input` - Para variables
- `btn` - Botones con estilos
- `badge` - Para categorías
- `loading` - Spinner mientras carga

**Configuración Tailwind para tema oscuro:**
```html
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
```

---

## TAREA 3.2: JavaScript para API

### Archivo: `frontend/js/api.js`

**Funciones a crear:**

```javascript
// Configuración base
const API_BASE = 'http://localhost:8000';

// 1. Obtener todas las fórmulas
async function obtenerFormulas() { ... }

// 2. Obtener una fórmula por ID
async function obtenerFormula(id) { ... }

// 3. Calcular fórmula
async function calcularFormula(formulaId, valores) { ... }

// 4. Obtener historial
async function obtenerHistorial() { ... }
```

**Requisitos:**
- Usar `fetch` con async/await
- Manejo de errores con try/catch
- Mostrar loading mientras carga
- Mostrar errores de forma elegante (toast o alert)

---

## TAREA 3.3: Visualización con Plotly

### Archivo: `frontend/js/graficos.js`

**Configuración del gráfico Plotly:**

```javascript
const configPlotly = {
  responsive: true,
  displayModeBar: true,
  modeBarButtonsToRemove: ['lasso2d', 'select2d'],
  displaylogo: false,
  toImageButtonOptions: {
    format: 'png',
    filename: 'formula_grafico'
  }
};

const layoutOscuro = {
  paper_bgcolor: '#1e293b',
  plot_bgcolor: '#1e293b',
  font: { color: '#f8fafc', family: 'Inter' },
  xaxis: { 
    gridcolor: '#334155',
    zerolinecolor: '#475569'
  },
  yaxis: { 
    gridcolor: '#334155',
    zerolinecolor: '#475569'
  },
  margin: { t: 50, r: 30, b: 50, l: 60 }
};
```

**Características deseadas:**
- Animación al cambiar datos
- Hover con información detallada
- Zoom y pan habilitados
- Línea suave (spline) para curvas
- Colores vibrantes sobre fondo oscuro

---

## TAREA 3.4: Estilos y UX

### Archivo: `frontend/css/styles.css`

**Solo para estilos custom que Tailwind no cubra:**
- Animaciones personalizadas
- Transiciones suaves
- Efectos hover especiales

**Efectos deseados:**
```css
/* Transición suave en cards */
.card {
  transition: transform 0.2s, box-shadow 0.2s;
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 40px rgba(0,0,0,0.3);
}

/* Glow en botón principal */
.btn-primary {
  box-shadow: 0 0 20px rgba(59, 130, 246, 0.5);
}

/* Animación de entrada */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
```

---

## INTERACCIONES UX

### Flujo del usuario:

1. **Carga inicial:**
   - Mostrar spinner elegante
   - Cargar lista de fórmulas desde API
   - Seleccionar primera fórmula por defecto

2. **Seleccionar fórmula:**
   - Mostrar fórmula en LaTeX renderizado
   - Mostrar inputs dinámicos según variables de la fórmula
   - Prellenar con valores por defecto de la BD

3. **Calcular:**
   - Botón con loading state mientras procesa
   - Animar la transición del gráfico
   - Mostrar mensaje de éxito/error

4. **Historial:**
   - Cards con los últimos cálculos
   - Click en card = cargar esos valores

---

## ESTRUCTURA FINAL DE ARCHIVOS

```
frontend/
├── index.html          # Estructura principal
├── css/
│   └── styles.css      # Estilos custom mínimos
└── js/
    ├── api.js          # Comunicación con backend
    ├── graficos.js     # Renderizado Plotly
    └── app.js          # Lógica principal (eventos, DOM)
```

---

## COMANDO PARA CLAUDE CODE

```
Lee CLAUDE.md y PLAN.md en /Volumes/Akitio01/Claude_MCP/formulas-web

Ejecuta la FASE 3 COMPLETA (tareas 3.1, 3.2, 3.3, 3.4):

IMPORTANTE - Stack visual:
- Tailwind CSS + DaisyUI para estilos modernos
- Plotly.js para gráficos interactivos
- MathJax para renderizar fórmulas LaTeX
- Tema OSCURO elegante (slate-900, blue-500)
- Fuente Inter de Google Fonts

Crea estos archivos:
1. frontend/index.html - Estructura con CDNs y layout responsive
2. frontend/js/api.js - Funciones fetch para comunicar con backend
3. frontend/js/graficos.js - Configuración Plotly tema oscuro
4. frontend/js/app.js - Lógica principal y eventos DOM
5. frontend/css/styles.css - Solo estilos custom necesarios

Diseño:
- Panel izquierdo: selector fórmula + inputs + botón calcular
- Área derecha grande: gráfico Plotly
- Abajo: historial de cálculos en cards
- Header y footer elegantes

Documenta cada archivo en docs/aprendizaje/ correspondiente.
El frontend debe poder servirse con: python -m http.server 3000

Recuerda: documentar diffs, no sobreescribir docs existentes.
```

---

## NOTAS IMPORTANTES

### 1. CORS - OBLIGATORIO ANTES DE EMPEZAR

El backend FastAPI **NO tiene CORS configurado**. Sin esto, el frontend NO puede comunicarse con el backend.

**PRIMERA TAREA:** Modificar `backend/main.py` para añadir CORS:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # AÑADIR

app = FastAPI(...)

# AÑADIR ESTO después de crear app:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Documentar este cambio con diff en `docs/aprendizaje/09_html_estructura.md`.

2. **Servir frontend:** Para probar, usar:
```bash
cd frontend
python -m http.server 3000
```
Luego abrir http://localhost:3000

3. **Backend debe estar corriendo:**
```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
uvicorn backend.main:app --reload
```

---

*Documento preparado: 29 diciembre 2024*
*Para: Claude Code - Fase 3 Frontend*
