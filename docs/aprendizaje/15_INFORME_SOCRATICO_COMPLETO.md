# INFORME SOCRÁTICO COMPLETO: Proyecto Fórmulas Web

> **Propósito:** Entender TODO el proyecto - qué hace cada parte, cómo se conectan, y por qué.
> **Para:** Juan Manuel - Repaso completo antes de seguir avanzando

---

## PARTE 1: VISIÓN GLOBAL - ¿Qué hemos construido?

### El producto final

Una aplicación web que:
1. Muestra 15 fórmulas matemáticas y físicas
2. Permite al usuario introducir valores
3. Calcula puntos para graficar
4. Muestra gráficos interactivos
5. Guarda historial de cálculos

### Las 3 capas de la aplicación

```
┌─────────────────────────────────────────────────────────────────────┐
│                         USUARIO (Navegador)                         │
│                                                                     │
│  "Quiero ver cómo se mueve un objeto con velocidad 5 m/s"           │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     CAPA 1: FRONTEND                                │
│                     (Lo que ve el usuario)                          │
│                                                                     │
│   HTML     → Estructura (qué elementos hay)                         │
│   CSS      → Apariencia (cómo se ven)                               │
│   JavaScript → Comportamiento (qué hacen cuando clicas)             │
│                                                                     │
│   Archivos: index.html, styles.css, api.js, app.js, graficos.js     │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ HTTP (JSON)
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     CAPA 2: BACKEND                                 │
│                     (El cerebro/servidor)                           │
│                                                                     │
│   FastAPI  → Recibe peticiones, las procesa, responde               │
│   Python   → Hace los cálculos matemáticos                          │
│                                                                     │
│   Archivos: main.py, routes/formulas.py, routes/calculos.py,        │
│             services/calculadora.py, services/supabase_client.py    │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ HTTP (JSON)
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     CAPA 3: BASE DE DATOS                           │
│                     (La memoria permanente)                         │
│                                                                     │
│   Supabase → PostgreSQL en la nube                                  │
│   Tablas   → formulas (15 fórmulas), calculos (historial)           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## PARTE 2: EL FRONTEND EN DETALLE

### 2.1 HTML - La estructura (index.html)

**¿Qué es?**
El esqueleto de la página. Define QUÉ elementos existen.

**Analogía:** Los planos de una casa. Dicen "aquí va una puerta", "aquí una ventana", pero no dicen de qué color ni qué pasa cuando abres la puerta.

**Estructura de nuestro index.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <!-- 1. METADATOS: Info sobre la página -->
    <title>Visualizador de Fórmulas</title>
    
    <!-- 2. ESTILOS: Cómo se ve (CSS externo) -->
    <link href="css/styles.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/daisyui..." rel="stylesheet">
    
    <!-- 3. SCRIPTS EXTERNOS: Librerías que usamos -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3..."></script>
</head>
<body>
    <!-- 4. CONTENIDO: Lo que ve el usuario -->
    
    <!-- Header -->
    <header>Visualizador de Fórmulas</header>
    
    <!-- Panel de configuración -->
    <div id="config-panel">
        <select id="selector-formula">...</select>  <!-- Dropdown -->
        <div id="formula-latex">...</div>           <!-- Fórmula renderizada -->
        <div id="inputs-container">...</div>        <!-- Inputs dinámicos -->
        <button id="btn-calcular">Calcular</button>
    </div>
    
    <!-- Área de visualización -->
    <div id="grafico">
        <!-- Plotly dibuja aquí -->
    </div>
    
    <!-- Historial -->
    <div id="historial">...</div>
    
    <!-- 5. SCRIPTS PROPIOS: Nuestro código JS -->
    <script src="js/api.js"></script>
    <script src="js/graficos.js"></script>
    <script src="js/app.js"></script>
</body>
</html>
```

**Puntos clave:**
- Los `id="..."` son como nombres únicos para que JavaScript pueda encontrar elementos
- Los `<script>` al final del body = se cargan después del HTML
- El orden de los scripts importa: api.js antes de app.js porque app.js usa funciones de api.js

---

### 2.2 CSS - La apariencia (styles.css + Tailwind + DaisyUI)

**¿Qué es?**
Las reglas de estilo. Define CÓMO se ven los elementos.

**Analogía:** El decorador de interiores. Dice "la puerta es azul", "la ventana tiene cortinas blancas".

**Tres fuentes de estilos en nuestro proyecto:**

```
1. TAILWIND (CDN)
   └── Clases utilitarias: bg-blue-500, text-white, p-4, rounded
   └── Se usan directamente en el HTML
   
2. DAISYUI (sobre Tailwind)
   └── Componentes predefinidos: btn, card, select, input
   └── Temas: dark, light, cupcake, etc.
   
3. styles.css (nuestro)
   └── Estilos personalizados que no cubren los anteriores
   └── Animaciones, efectos hover especiales
```

**Cómo se aplican los estilos:**

```html
<!-- Tailwind: clases directas -->
<button class="bg-blue-500 text-white p-4 rounded-lg hover:bg-blue-600">
    Calcular
</button>

<!-- DaisyUI: componentes -->
<button class="btn btn-primary">
    Calcular
</button>
<!-- DaisyUI internamente aplica múltiples clases de Tailwind -->

<!-- CSS propio: para cosas específicas -->
<div class="mi-animacion-personalizada">
```

**¿Por qué Tailwind + DaisyUI?**

| Sin Tailwind | Con Tailwind |
|--------------|--------------|
| Crear archivo CSS | Escribir clases en HTML |
| Inventar nombres: `.boton-azul-grande` | Usar estándar: `bg-blue-500 text-lg` |
| Muchos archivos CSS | Un solo lugar |
| Inconsistencia de estilos | Consistencia automática |

---

### 2.3 JavaScript - El comportamiento

**¿Qué es?**
El código que hace que las cosas "funcionen". Define QUÉ PASA cuando el usuario interactúa.

**Analogía:** La electricidad y los mecanismos. Hace que cuando pulses el interruptor, se encienda la luz.

#### Nuestros 3 archivos JS y sus responsabilidades:

```
frontend/js/
├── api.js       → Habla con el backend (el cartero)
├── graficos.js  → Dibuja con Plotly (el pintor)
└── app.js       → Coordina todo (el director)
```

---

#### 2.3.1 api.js - El cartero

**Responsabilidad única:** Comunicarse con el backend. Nada más.

```javascript
// api.js - Simplificado para entender

// Dirección del backend
const API_BASE = 'http://localhost:8000';

// Función 1: Obtener lista de fórmulas
async function obtenerFormulas() {
    // fetch = "ve a buscar"
    // await = "espera a que termine"
    const respuesta = await fetch(`${API_BASE}/api/formulas`);
    
    // Convertir respuesta a JSON (objeto JavaScript)
    const datos = await respuesta.json();
    
    // Devolver los datos
    return datos;
}

// Función 2: Calcular una fórmula
async function calcularFormula(formulaId, valores) {
    const respuesta = await fetch(`${API_BASE}/api/calcular`, {
        method: 'POST',           // POST = enviar datos
        headers: {
            'Content-Type': 'application/json'  // "Envío JSON"
        },
        body: JSON.stringify({    // Convertir objeto a texto JSON
            formula_id: formulaId,
            valores: valores
        })
    });
    
    const datos = await respuesta.json();
    return datos;
}

// Función 3: Obtener historial
async function obtenerHistorial() {
    const respuesta = await fetch(`${API_BASE}/api/historial`);
    const datos = await respuesta.json();
    return datos;
}
```

**Conceptos clave:**

| Concepto | Qué es | Ejemplo |
|----------|--------|---------|
| `fetch()` | Función para hacer peticiones HTTP | `fetch('http://...')` |
| `async` | "Esta función es asíncrona (tarda)" | `async function nombre()` |
| `await` | "Espera a que esto termine" | `await fetch(...)` |
| `JSON.stringify()` | Objeto JS → texto JSON | `{a:1}` → `'{"a":1}'` |
| `.json()` | Texto JSON → objeto JS | `'{"a":1}'` → `{a:1}` |

**¿Por qué async/await?**

```javascript
// Las peticiones HTTP tardan (red, servidor, BD...)
// Sin async/await:
fetch('/api/formulas')  // Esto tarda 500ms
console.log(datos)      // Esto se ejecuta ANTES de tener los datos
                        // datos = undefined ❌

// Con async/await:
const datos = await fetch('/api/formulas')  // Espera 500ms
console.log(datos)                          // Ahora sí tiene los datos ✅
```

---

#### 2.3.2 graficos.js - El pintor

**Responsabilidad única:** Dibujar gráficos con Plotly. Nada más.

```javascript
// graficos.js - Simplificado

// Configuración del tema oscuro para Plotly
const layoutOscuro = {
    paper_bgcolor: '#1e293b',  // Fondo del "papel"
    plot_bgcolor: '#1e293b',   // Fondo del gráfico
    font: { 
        color: '#f8fafc',      // Color del texto
        family: 'Inter'        // Fuente
    },
    xaxis: { 
        gridcolor: '#334155',  // Color de la cuadrícula
        title: 'x'
    },
    yaxis: { 
        gridcolor: '#334155',
        title: 'y'
    }
};

// Función principal: dibujar gráfico
function dibujarGrafico(resultado, nombreFormula) {
    // 1. Detectar qué tipo de datos tenemos
    let xData, yData;
    
    if (resultado.t !== undefined) {
        // Fórmulas temporales: t vs x
        xData = resultado.t;
        yData = resultado.x || resultado.y;
    } else {
        // Curvas paramétricas: x vs y
        xData = resultado.x;
        yData = resultado.y;
    }
    
    // 2. Crear el "trace" (la línea a dibujar)
    const trace = {
        x: xData,
        y: yData,
        type: 'scatter',      // Tipo de gráfico
        mode: 'lines',        // Solo líneas (no puntos)
        name: nombreFormula,
        line: {
            color: '#3b82f6', // Azul
            width: 2
        }
    };
    
    // 3. Dibujar con Plotly
    Plotly.newPlot('grafico', [trace], layoutOscuro);
}
```

**Tipos de gráficos en Plotly:**

| type | mode | Resultado |
|------|------|-----------|
| `scatter` | `lines` | Línea continua |
| `scatter` | `markers` | Solo puntos |
| `scatter` | `lines+markers` | Línea con puntos |
| `scatter3d` | `lines` | Línea en 3D |

---

#### 2.3.3 app.js - El director de orquesta

**Responsabilidad:** Coordinar todo. Escuchar eventos, llamar funciones, actualizar la página.

```javascript
// app.js - Simplificado

// ============================================
// PASO 1: Cuando la página carga
// ============================================
document.addEventListener('DOMContentLoaded', async () => {
    // DOMContentLoaded = "el HTML ya está listo"
    
    // 1. Cargar la lista de fórmulas
    const formulas = await obtenerFormulas();  // Llama a api.js
    
    // 2. Llenar el selector
    const selector = document.getElementById('selector-formula');
    formulas.data.forEach(formula => {
        const opcion = document.createElement('option');
        opcion.value = formula.id;
        opcion.textContent = formula.nombre;
        selector.appendChild(opcion);
    });
    
    // 3. Cargar la primera fórmula
    cargarFormula(formulas.data[0]);
});

// ============================================
// PASO 2: Cuando cambia la fórmula seleccionada
// ============================================
document.getElementById('selector-formula').addEventListener('change', async (e) => {
    // e.target.value = el ID de la fórmula seleccionada
    const formulaId = e.target.value;
    
    // Obtener datos de esa fórmula
    const respuesta = await obtenerFormula(formulaId);  // Llama a api.js
    
    // Actualizar la interfaz
    cargarFormula(respuesta.data);
});

// ============================================
// PASO 3: Función para cargar una fórmula
// ============================================
function cargarFormula(formula) {
    // 1. Mostrar fórmula LaTeX
    document.getElementById('formula-latex').innerHTML = `\\(${formula.formula_latex}\\)`;
    MathJax.typeset();  // Renderizar LaTeX
    
    // 2. Mostrar categoría
    document.getElementById('categoria').textContent = formula.categoria;
    
    // 3. Generar inputs dinámicos
    generarInputs(formula);
}

// ============================================
// PASO 4: Generar inputs según la fórmula
// ============================================
function generarInputs(formula) {
    const container = document.getElementById('inputs-container');
    container.innerHTML = '';  // Limpiar
    
    // formula.variables_usuario = {"x0": 0, "v": 5, ...}
    const variables = formula.variables_usuario;
    
    for (const [nombre, valorDefault] of Object.entries(variables)) {
        // Crear label + input para cada variable
        const div = document.createElement('div');
        div.innerHTML = `
            <label>${nombre}</label>
            <input type="number" 
                   id="input-${nombre}" 
                   value="${valorDefault}"
                   class="input input-bordered">
        `;
        container.appendChild(div);
    }
    
    // Añadir inputs de rango (t_min, t_max, etc.)
    const varRango = formula.variable_rango;  // "t", "x", "theta"
    // ... crear inputs para rango_min y rango_max
}

// ============================================
// PASO 5: Cuando hacen clic en Calcular
// ============================================
document.getElementById('btn-calcular').addEventListener('click', async () => {
    // 1. Obtener la fórmula seleccionada
    const formulaId = document.getElementById('selector-formula').value;
    
    // 2. Obtener los valores de los inputs
    const valores = {};
    const inputs = document.querySelectorAll('#inputs-container input');
    inputs.forEach(input => {
        const nombre = input.id.replace('input-', '');
        valores[nombre] = parseFloat(input.value);
    });
    
    // 3. Llamar al backend
    const resultado = await calcularFormula(formulaId, valores);  // api.js
    
    // 4. Dibujar el gráfico
    dibujarGrafico(resultado.data.resultado, resultado.data.formula.nombre);  // graficos.js
    
    // 5. Actualizar historial
    actualizarHistorial();
});
```

**Conceptos clave de JavaScript:**

| Concepto | Qué hace | Ejemplo |
|----------|----------|---------|
| `document.getElementById()` | Busca elemento por ID | `document.getElementById('mi-boton')` |
| `document.querySelector()` | Busca con selector CSS | `document.querySelector('.clase')` |
| `addEventListener()` | "Cuando pase X, haz Y" | `boton.addEventListener('click', funcion)` |
| `innerHTML` | Cambia el HTML interno | `div.innerHTML = '<p>Hola</p>'` |
| `createElement()` | Crea nuevo elemento | `document.createElement('div')` |
| `appendChild()` | Añade hijo a elemento | `padre.appendChild(hijo)` |

---

## PARTE 3: EL BACKEND EN DETALLE

### 3.1 main.py - El punto de entrada

```python
# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar nuestros routers
from backend.routes.formulas import router as formulas_router
from backend.routes.calculos import router as calculos_router

# Crear la aplicación
app = FastAPI(
    title="API Fórmulas Matemáticas",
    description="Backend para visualización de fórmulas",
    version="0.1.0"
)

# CORS - Permitir que el frontend hable con nosotros
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Quién puede hablar con nosotros
    allow_credentials=True,
    allow_methods=["*"],       # GET, POST, etc.
    allow_headers=["*"],
)

# Registrar rutas
app.include_router(formulas_router)  # /api/formulas, /api/formula/{id}
app.include_router(calculos_router)  # /api/calcular, /api/historial

# Endpoint de prueba
@app.get("/health")
def health_check():
    return {"status": "ok"}
```

**¿Por qué CORS?**

Sin CORS, el navegador bloquea las peticiones del frontend (localhost:3000) al backend (localhost:8000) porque son "orígenes diferentes". CORS le dice al navegador "tranquilo, sí permito esto".

---

### 3.2 routes/formulas.py - Endpoints de fórmulas

```python
# routes/formulas.py

from fastapi import APIRouter
from backend.services.supabase_client import supabase

router = APIRouter(prefix="/api", tags=["formulas"])

@router.get("/formulas")
def listar_formulas():
    """Devuelve TODAS las fórmulas."""
    response = supabase.table("formulas").select("*").execute()
    return {"data": response.data, "error": None}

@router.get("/formula/{formula_id}")
def obtener_formula(formula_id: int):
    """Devuelve UNA fórmula por ID."""
    response = supabase.table("formulas").select("*").eq("id", formula_id).execute()
    
    if not response.data:
        return {"data": None, "error": "Fórmula no encontrada"}
    
    return {"data": response.data[0], "error": None}
```

**¿Qué devuelve `/api/formulas`?**

```json
{
  "data": [
    {
      "id": 1,
      "nombre": "MRU - Movimiento Rectilíneo Uniforme",
      "categoria": "fisica",
      "formula_latex": "x = x_0 + v \\cdot t",
      "variables_usuario": {"x0": 0, "v": 5},
      "variable_rango": "t",
      "rango_min": 0,
      "rango_max": 10
    },
    {
      "id": 2,
      "nombre": "MRUA...",
      ...
    }
  ],
  "error": null
}
```

---

### 3.3 routes/calculos.py - El endpoint de cálculo

```python
# routes/calculos.py - Simplificado

from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.supabase_client import supabase
from backend.services.calculadora import (
    calcular_mru, calcular_mrua, calcular_parabola, ...
)

router = APIRouter(prefix="/api", tags=["calculos"])

# Modelo de datos que esperamos recibir
class DatosCalculo(BaseModel):
    formula_id: int
    valores: dict

@router.post("/calcular")
def calcular(datos: DatosCalculo):
    # 1. Obtener la fórmula de la BD
    formula_response = supabase.table("formulas").select("*").eq("id", datos.formula_id).execute()
    formula = formula_response.data[0]
    
    # 2. Obtener rango
    rango_min = datos.valores.get("t_min", formula["rango_min"])
    rango_max = datos.valores.get("t_max", formula["rango_max"])
    
    # 3. Identificar qué fórmula es y calcular
    if "MRU" in formula["nombre"] and "Uniformemente" not in formula["nombre"]:
        resultado = calcular_mru(
            x0=datos.valores.get("x0", 0),
            v=datos.valores.get("v", 5),
            t_min=rango_min,
            t_max=rango_max
        )
    elif "MRUA" in formula["nombre"]:
        resultado = calcular_mrua(...)
    elif "Parábola" in formula["nombre"]:
        resultado = calcular_parabola(...)
    # ... más fórmulas
    
    # 4. Guardar en historial
    supabase.table("calculos").insert({
        "formula_id": datos.formula_id,
        "valores_entrada": datos.valores,
        "resultado": resultado
    }).execute()
    
    # 5. Devolver resultado
    return {
        "data": {
            "formula": formula,
            "valores": datos.valores,
            "resultado": resultado
        },
        "error": None
    }
```

**¿Qué devuelve `/api/calcular`?**

```json
{
  "data": {
    "formula": {
      "id": 1,
      "nombre": "MRU...",
      "variables_usuario": {"x0": 0, "v": 5},
      ...
    },
    "valores": {"x0": 0, "v": 5, "t_min": 0, "t_max": 10},
    "resultado": {
      "t": [0, 0.1, 0.2, ..., 10],
      "x": [0, 0.5, 1.0, ..., 50]
    }
  },
  "error": null
}
```

---

### 3.4 services/calculadora.py - Las matemáticas

```python
# calculadora.py

import numpy as np

def calcular_mru(x0, v, t_min, t_max, puntos=100):
    """MRU: x = x0 + v*t"""
    t = np.linspace(t_min, t_max, puntos)  # 100 valores entre t_min y t_max
    x = x0 + v * t                          # Fórmula matemática
    return {"t": t.tolist(), "x": x.tolist()}

def calcular_parabola(a, b, c, x_min, x_max, puntos=100):
    """Parábola: y = ax² + bx + c"""
    x = np.linspace(x_min, x_max, puntos)
    y = a * x**2 + b * x + c
    return {"x": x.tolist(), "y": y.tolist()}

def calcular_cardioide(a, theta_min, theta_max, puntos=200):
    """Cardioide: r = a*(1 + cos(θ))"""
    theta = np.linspace(theta_min, theta_max, puntos)
    r = a * (1 + np.cos(theta))
    x = r * np.cos(theta)  # Convertir polar a cartesiano
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}
```

---

## PARTE 4: EL FLUJO COMPLETO - EJEMPLO REAL

### Escenario: Usuario selecciona "Parábola" y hace clic en Calcular

```
PASO 1: Usuario selecciona "Parábola" en el dropdown
────────────────────────────────────────────────────

[FRONTEND - app.js]
selector.addEventListener('change', async (e) => {
    const formulaId = e.target.value;  // formulaId = 7
    const respuesta = await obtenerFormula(7);
    cargarFormula(respuesta.data);
});

↓

[FRONTEND - api.js]
async function obtenerFormula(id) {
    const respuesta = await fetch('http://localhost:8000/api/formula/7');
    return await respuesta.json();
}

↓ HTTP GET /api/formula/7

[BACKEND - routes/formulas.py]
@router.get("/formula/{formula_id}")
def obtener_formula(formula_id: int):  # formula_id = 7
    response = supabase.table("formulas").select("*").eq("id", 7).execute()
    return {"data": response.data[0], "error": None}

↓ Supabase query

[SUPABASE]
SELECT * FROM formulas WHERE id = 7;
→ {id: 7, nombre: "Parábola", variables_usuario: {"a":1, "b":0, "c":0}, ...}

↑ Respuesta sube de vuelta

[FRONTEND - app.js]
cargarFormula(formula);
// formula = {id: 7, nombre: "Parábola", variables_usuario: {"a":1, "b":0, "c":0}, ...}

function generarInputs(formula) {
    // Crea inputs para a, b, c con valores por defecto
}


PASO 2: Usuario cambia valores y hace clic en Calcular
──────────────────────────────────────────────────────

[FRONTEND - app.js]
btnCalcular.addEventListener('click', async () => {
    const valores = {a: 2, b: -3, c: 1, x_min: -5, x_max: 5};
    const resultado = await calcularFormula(7, valores);
    dibujarGrafico(resultado.data.resultado, "Parábola");
});

↓

[FRONTEND - api.js]
async function calcularFormula(formulaId, valores) {
    const respuesta = await fetch('http://localhost:8000/api/calcular', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({formula_id: 7, valores: {a:2, b:-3, c:1, x_min:-5, x_max:5}})
    });
    return await respuesta.json();
}

↓ HTTP POST /api/calcular

[BACKEND - routes/calculos.py]
@router.post("/calcular")
def calcular(datos: DatosCalculo):
    formula = supabase.table("formulas").select("*").eq("id", 7).execute().data[0]
    
    # Identificar: "Parábola" está en el nombre
    resultado = calcular_parabola(a=2, b=-3, c=1, x_min=-5, x_max=5)
    
    # Guardar en historial
    supabase.table("calculos").insert({...}).execute()
    
    return {"data": {"formula": formula, "resultado": resultado}, "error": None}

↓

[BACKEND - services/calculadora.py]
def calcular_parabola(a, b, c, x_min, x_max, puntos=100):
    x = np.linspace(-5, 5, 100)      # [-5, -4.9, -4.8, ..., 4.9, 5]
    y = 2*x**2 + (-3)*x + 1          # [56, 53.02, ..., 36]
    return {"x": x.tolist(), "y": y.tolist()}

↑ Respuesta sube

[FRONTEND - graficos.js]
function dibujarGrafico(resultado, nombre) {
    // resultado = {x: [-5, -4.9, ...], y: [56, 53.02, ...]}
    Plotly.newPlot('grafico', [{
        x: resultado.x,
        y: resultado.y,
        type: 'scatter',
        mode: 'lines'
    }], layoutOscuro);
}

→ Se dibuja la parábola en pantalla
```

---

## PARTE 5: CÓMO PYTHON LE DICE AL FRONTEND QUÉ MOSTRAR

### El problema actual

Los inputs siempre muestran "Posición inicial (x₀)", "Velocidad (v)" aunque la fórmula sea "Parábola" que usa a, b, c.

### La solución

**La información YA está en la base de datos:**

```json
// Fórmula MRU en Supabase:
{
  "id": 1,
  "nombre": "MRU",
  "variables_usuario": {"x0": 0, "v": 5}
}

// Fórmula Parábola en Supabase:
{
  "id": 7,
  "nombre": "Parábola",
  "variables_usuario": {"a": 1, "b": 0, "c": 0}
}
```

**El frontend debe LEER esto y generar inputs dinámicamente:**

```javascript
// app.js - Versión mejorada

function generarInputs(formula) {
    const container = document.getElementById('inputs-container');
    container.innerHTML = '';
    
    // formula.variables_usuario = {"a": 1, "b": 0, "c": 0}
    const variables = formula.variables_usuario;
    
    // Para cada variable, crear un input
    for (const [nombre, valorDefault] of Object.entries(variables)) {
        const div = document.createElement('div');
        div.className = 'form-control';
        div.innerHTML = `
            <label class="label">
                <span class="label-text">${nombre}</span>
            </label>
            <input type="number" 
                   id="input-${nombre}" 
                   value="${valorDefault}"
                   step="0.1"
                   class="input input-bordered">
        `;
        container.appendChild(div);
    }
}
```

**Problema:** Los nombres son técnicos (x0, v, a, b, c). 

**Solución mejorada:** Añadir metadata en Supabase:

```json
// Versión mejorada de la BD:
{
  "id": 1,
  "nombre": "MRU",
  "variables_usuario": {
    "x0": {"nombre_display": "Posición inicial (x₀)", "default": 0, "unidad": "m"},
    "v": {"nombre_display": "Velocidad (v)", "default": 5, "unidad": "m/s"}
  }
}
```

**Entonces el frontend puede mostrar:**
```javascript
for (const [key, config] of Object.entries(variables)) {
    div.innerHTML = `
        <label>${config.nombre_display}</label>
        <input value="${config.default}">
        <span class="unidad">${config.unidad}</span>
    `;
}
```

---

## PARTE 6: DEPLOY - CÓMO SUBIR A INTERNET

### 6.1 Subir a GitHub

```bash
# 1. Inicializar repositorio
cd /Volumes/Akitio01/Claude_MCP/formulas-web
git init

# 2. Crear .gitignore (ya existe, pero verificar)
cat .gitignore
# Debe incluir:
# .env
# venv/
# __pycache__/
# .DS_Store

# 3. Añadir archivos
git add .

# 4. Commit
git commit -m "Proyecto completo: 15 fórmulas funcionando"

# 5. Crear repo en GitHub (desde web o CLI)
# https://github.com/new → crear "formulas-web"

# 6. Conectar y subir
git remote add origin https://github.com/TU_USUARIO/formulas-web.git
git branch -M main
git push -u origin main
```

---

### 6.2 Deploy Backend en Render

**¿Qué es Render?**
Servicio de hosting que ejecuta tu código Python en la nube. Gratis para proyectos pequeños.

**Pasos:**

1. **Crear cuenta en Render** (https://render.com)

2. **Crear archivo `render.yaml`** en la raíz del proyecto:
```yaml
services:
  - type: web
    name: formulas-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn backend.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: SUPABASE_URL
        sync: false  # Lo pondrás manualmente
      - key: SUPABASE_KEY
        sync: false
```

3. **En Render:**
   - New → Web Service
   - Connect repository (GitHub)
   - Seleccionar `formulas-web`
   - Environment: Python 3
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`

4. **Añadir variables de entorno:**
   - SUPABASE_URL = (tu URL)
   - SUPABASE_KEY = (tu key)

5. **Deploy!**
   - Te da una URL tipo: `https://formulas-api.onrender.com`

---

### 6.3 Deploy Frontend en Cloudflare Pages

**¿Qué es Cloudflare Pages?**
Hosting gratuito para sitios estáticos (HTML/CSS/JS). Muy rápido, CDN global.

**Pasos:**

1. **Crear cuenta en Cloudflare** (https://dash.cloudflare.com)

2. **Modificar `api.js`** para usar la URL del backend desplegado:
```javascript
// ANTES (desarrollo)
const API_BASE = 'http://localhost:8000';

// DESPUÉS (producción)
const API_BASE = 'https://formulas-api.onrender.com';

// MEJOR (configurable)
const API_BASE = window.location.hostname === 'localhost' 
    ? 'http://localhost:8000' 
    : 'https://formulas-api.onrender.com';
```

3. **En Cloudflare:**
   - Pages → Create project
   - Connect to Git → Seleccionar repo
   - Framework preset: None
   - Build command: (vacío, no hay build)
   - Build output directory: `frontend`

4. **Deploy!**
   - Te da una URL tipo: `https://formulas-web.pages.dev`

---

## PARTE 7: SEGURIDAD (Básica)

### 7.1 Lo que YA tenemos bien

| Aspecto | Estado | Por qué |
|---------|--------|---------|
| Credenciales en `.env` | ✅ | No se suben a Git |
| `.gitignore` configurado | ✅ | Excluye archivos sensibles |
| Supabase Row Level Security | ⚠️ | Deberíamos activarlo |

### 7.2 Mejoras recomendadas

**1. Activar RLS en Supabase:**
```sql
-- En Supabase SQL Editor
ALTER TABLE formulas ENABLE ROW LEVEL SECURITY;
ALTER TABLE calculos ENABLE ROW LEVEL SECURITY;

-- Permitir lectura pública de fórmulas
CREATE POLICY "Fórmulas públicas" ON formulas
    FOR SELECT USING (true);

-- Permitir escritura en cálculos (cualquiera puede guardar)
CREATE POLICY "Cálculos públicos" ON calculos
    FOR INSERT WITH CHECK (true);
```

**2. Rate limiting (opcional):**
Evitar que alguien haga miles de peticiones por segundo.

**3. Validación de inputs:**
Ya lo hace Pydantic en el backend (BaseModel).

**4. HTTPS:**
Render y Cloudflare lo dan gratis automáticamente.

---

## PARTE 8: RESUMEN VISUAL FINAL

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              PROYECTO COMPLETO                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   FRONTEND (Cloudflare Pages)          BACKEND (Render)                     │
│   https://formulas.pages.dev           https://formulas-api.onrender.com    │
│                                                                             │
│   ┌─────────────────────────┐          ┌─────────────────────────┐          │
│   │     index.html          │          │     main.py             │          │
│   │     (estructura)        │          │     (FastAPI app)       │          │
│   ├─────────────────────────┤          ├─────────────────────────┤          │
│   │     styles.css          │          │   routes/               │          │
│   │     Tailwind + DaisyUI  │   HTTP   │     formulas.py         │          │
│   │     (apariencia)        │ ◄──────► │     calculos.py         │          │
│   ├─────────────────────────┤   JSON   ├─────────────────────────┤          │
│   │     js/                 │          │   services/             │          │
│   │       api.js            │          │     supabase_client.py  │          │
│   │       graficos.js       │          │     calculadora.py      │          │
│   │       app.js            │          │                         │          │
│   └─────────────────────────┘          └───────────┬─────────────┘          │
│                                                    │                        │
│                                                    │ SQL                    │
│                                                    ▼                        │
│                                        ┌─────────────────────────┐          │
│                                        │     SUPABASE            │          │
│                                        │     (PostgreSQL)        │          │
│                                        │                         │          │
│                                        │   formulas (15 rows)    │          │
│                                        │   calculos (historial)  │          │
│                                        └─────────────────────────┘          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## PARTE 9: GLOSARIO RÁPIDO

| Término | Significado |
|---------|-------------|
| **API** | Interfaz para que programas hablen entre sí |
| **Endpoint** | Una dirección específica de la API (/api/formulas) |
| **JSON** | Formato de texto para datos: `{"clave": "valor"}` |
| **async/await** | Forma de esperar operaciones lentas en JS |
| **fetch** | Función JS para hacer peticiones HTTP |
| **FastAPI** | Framework Python para crear APIs |
| **Pydantic** | Librería para validar datos en Python |
| **Router** | Agrupador de endpoints en FastAPI |
| **Supabase** | Base de datos PostgreSQL en la nube |
| **CORS** | Permiso para que el frontend hable con el backend |
| **CDN** | Red de servidores que entrega archivos rápido |
| **Deploy** | Subir código a un servidor para que funcione en internet |

---

*Documento creado: 30 diciembre 2024*
*Proyecto: Fórmulas Web - Informe Socrático Completo*
