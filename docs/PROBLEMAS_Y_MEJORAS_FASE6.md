# PROBLEMAS DETECTADOS Y MEJORAS NECESARIAS - Fase 6

**Fecha:** 7 Enero 2026
**Estado:** Producción funcionando, pero con mejoras pendientes
**URLs Producción:**
- Frontend: https://formulas-web.pages.dev
- Backend: https://web-production-daa0.up.railway.app

---

## 🎯 RESUMEN EJECUTIVO

La aplicación está **DESPLEGADA Y FUNCIONANDO** en producción:
- ✅ Backend en Railway (FastAPI + Supabase)
- ✅ Frontend en Cloudflare Pages
- ✅ Conexión funcionando
- ✅ Cálculos y gráficos operativos

**PERO:** Se detectaron 4 problemas importantes que requieren corrección.

---

## 📋 LISTA DE PROBLEMAS

### 🔴 PROBLEMA 1: Inputs dinámicos rotos (algunas fórmulas)

**Severidad:** Alta
**Estado:** Bug crítico

#### Descripción del problema:

**Fórmulas que funcionan correctamente:**
- ✅ **MRU** (Movimiento Rectilíneo Uniforme)
  - Muestra: "Velocidad", "Posición inicial x₀"
  - Inputs tienen nombres descriptivos
  - Sliders para t_min, t_max funcionan

**Fórmulas que NO funcionan:**
- ❌ **MRUA** (Movimiento Rectilíneo Uniformemente Acelerado)
  - Muestra: 0, 1, 2, 3, 4, 5, 6, 7 (números en lugar de nombres)
  - Inputs dicen "valor" genérico
  - No se entiende qué variable es cada input

- ❌ **Caída Libre**
  - Mismo problema: 0, 1, 2, 3, 4, 5, 6, 7
  - Inputs sin etiquetas descriptivas

#### Evidencia (capturas de pantalla):

**Captura 1 - MRU (funciona bien):**
- Select muestra: "MRU - Movimiento Rectilíneo Uniforme"
- Fórmula renderizada: `x = x₀ + v·t`
- Inputs:
  - "Velocidad" (valor 5)
  - "Posición inicial x₀" (valor 0)
  - Slider "t mínimo" (0)
  - Slider "t máximo" (10)

**Captura 2 - MRUA (ROTO):**
- Select muestra: "MRUA - Movimiento Uniformemente Acelerado"
- Fórmula renderizada: `x = x₀ + v₀·t + ½·a·t²`
- Inputs ROTOS:
  - Campo "0" con placeholder "valor"
  - Campo "1" con placeholder "valor"
  - Campo "2" con placeholder "valor"
  - ...hasta "7"
  - **NO muestra nombres de variables**

**Captura 3 - Caída Libre (ROTO):**
- Select muestra: "Caída Libre"
- Fórmula: `y = y₀ - ½·g·t²`
- Inputs ROTOS: 0, 1, 2, 3, 4, 5, 6, 7

#### Diagnóstico técnico:

**Causa raíz:**
Inconsistencia en cómo están almacenadas las `variables_usuario` en Supabase.

**Caso 1 - MRU (funciona):**
```json
{
  "variables_usuario": {
    "x0": 0,
    "v": 5
  }
}
```
Tipo: **Objeto** (JavaScript Object)

**Caso 2 - MRUA (roto):**
```json
{
  "variables_usuario": [0, 1, 2, 3, 4, 5, 6, 7]
}
```
Tipo: **Array** (JavaScript Array)

**Código en `frontend/js/app.js` línea 169-204:**
```javascript
function generarInputsDinamicos(formula) {
    const variables = formula.variables_usuario || {};

    // Itera sobre las variables
    Object.entries(variables).forEach(([nombreVar, valorDefecto]) => {
        // Si variables_usuario es un array:
        // nombreVar = "0", "1", "2", ... (índices del array)
        // En lugar de "x0", "v0", "a", ...

        const config = ETIQUETAS_VARIABLES[nombreVar] || {
            label: nombreVar,  // ← Aquí se imprime "0", "1", "2"
            placeholder: 'valor',
            unidad: ''
        };
    });
}
```

**¿Por qué ocurre?**
- Algunas fórmulas se insertaron con objeto: `{x0: 0, v: 5}`
- Otras con array: `[0, 1, 2]`
- El código espera SIEMPRE objeto

#### Solución propuesta:

**Opción A: Arreglar datos en Supabase (recomendado)**

1. Leer todas las fórmulas
2. Identificar cuáles tienen `variables_usuario` como array
3. Convertir arrays a objetos:
   ```python
   # Ejemplo para MRUA que tiene [0, 1, 2, 3, 4]
   # Debería ser:
   {
       "x0": 0,
       "v0": 5,
       "a": 2
   }
   ```
4. Actualizar en Supabase

**Opción B: Adaptar el código frontend (menos recomendado)**

Modificar `generarInputsDinamicos()` para detectar arrays:
```javascript
let variables = formula.variables_usuario || {};

// Si es array, convertir a objeto
if (Array.isArray(variables)) {
    console.warn('Formula tiene variables_usuario como array, debe ser objeto');
    variables = {}; // Por ahora, crear vacío y pedir valores al usuario
}
```

**Recomendación:** **Opción A** - Los datos en BD deben estar consistentes.

---

### 🔴 PROBLEMA 2: Inputs tipo number con controles arriba/abajo

**Severidad:** Media
**Estado:** UX mejorable

#### Descripción del problema:

Los inputs usan `<input type="number">`, que muestra **flechas arriba/abajo** (spinners):

```html
<input type="number" value="5">
↑↓ ← Flechitas para incrementar/decrementar
```

**Problema:**
- El usuario quiere escribir "velocidad = 15.5 m/s" directamente
- Las flechitas son molestas y ocupan espacio
- No tiene sentido incrementar/decrementar valores de física de 1 en 1

**Ejemplo:**
- Velocidad: 15.5 m/s
- El usuario hace click en "↑" → Incrementa a 16.5
- No tiene utilidad real

#### Solución propuesta:

**Opción 1: Cambiar a `type="text"` con validación**
```html
<input type="text" pattern="[0-9.-]+" placeholder="15.5">
```

**Ventajas:**
- Sin flechitas
- Usuario escribe libremente
- Validación con patrón regex

**Desventajas:**
- El teclado móvil NO muestra teclado numérico automáticamente

**Opción 2: Mantener `type="number"` pero ocultar spinners con CSS**
```css
/* Ocultar spinners en Chrome, Safari, Edge */
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}

/* Ocultar spinners en Firefox */
input[type="number"] {
    -moz-appearance: textfield;
}
```

**Ventajas:**
- ✅ Mantiene validación de número
- ✅ Teclado numérico en móvil
- ✅ Sin flechitas molestas

**Desventajas:**
- Ninguna

**Recomendación:** **Opción 2** - Mejor UX sin sacrificar funcionalidad.

**Archivo a modificar:** `frontend/css/styles.css` o dentro de `<style>` en `index.html`

---

### 🔴 PROBLEMA 3: Gráficos en 2D (requisito original: 3D)

**Severidad:** Alta
**Estado:** Incumplimiento de requisito original

#### Descripción del problema:

**Requisito inicial del proyecto:**
> "Visualización de fórmulas matemáticas y físicas con gráficos **3D interactivos**"

**Estado actual:**
- Los gráficos son **2D** (X vs Y)
- Plotly.js se usa en modo 2D
- Falta el eje Z

**Ejemplo actual (MRU):**
```javascript
// frontend/js/app.js - Función renderizarGrafico()
const trace = {
    x: datosGrafico.x,  // Eje X (tiempo)
    y: datosGrafico.y,  // Eje Y (posición)
    // ❌ Falta eje Z
    type: 'scatter',    // Tipo 2D
    mode: 'lines'
};
```

**Lo que debería ser:**
```javascript
const trace = {
    x: datosGrafico.x,  // Eje X
    y: datosGrafico.y,  // Eje Y
    z: datosGrafico.z,  // Eje Z ← FALTA ESTO
    type: 'scatter3d',  // Tipo 3D
    mode: 'lines'
};
```

#### ¿Qué fórmulas necesitan 3D?

**Fórmulas 2D (actual funciona bien):**
- MRU: x vs t (posición vs tiempo)
- MRUA: x vs t
- Caída Libre: y vs t

**Fórmulas que NECESITAN 3D:**
- **Tiro Parabólico:** x vs y vs t (trayectoria en el espacio)
- **Movimiento Circular:** x vs y vs t (círculo en plano XY)
- **Espiral:** x vs y vs z (3 dimensiones)
- **Hélice:** x vs y vs z
- **Paraboloide:** x vs y vs z(x,y)
- **Esfera:** x vs y vs z

**Total:**
- 3 fórmulas funcionan en 2D ✅
- **12 fórmulas necesitan 3D** ❌

#### Solución propuesta:

**Paso 1: Modificar backend para generar datos 3D**

**Archivo:** `backend/services/calculadora.py`

Añadir función para detectar si la fórmula es 2D o 3D:
```python
def es_formula_3d(formula_nombre):
    """Determina si una fórmula necesita gráfico 3D"""
    formulas_3d = [
        'Tiro Parabólico',
        'Movimiento Circular',
        'Espiral',
        'Hélice',
        'Paraboloide',
        'Esfera'
    ]
    return formula_nombre in formulas_3d
```

Modificar cálculo para devolver coordenada Z:
```python
if es_formula_3d(formula.nombre):
    resultado = {
        "x": lista_x,
        "y": lista_y,
        "z": lista_z,  # ← Añadir esto
        "tipo_grafico": "3d"
    }
else:
    resultado = {
        "x": lista_x,
        "y": lista_y,
        "tipo_grafico": "2d"
    }
```

**Paso 2: Modificar frontend para renderizar 3D**

**Archivo:** `frontend/js/app.js` - Función `renderizarGrafico()`

```javascript
function renderizarGrafico(datosGrafico) {
    const es3D = datosGrafico.tipo_grafico === '3d' && datosGrafico.z;

    if (es3D) {
        // Gráfico 3D
        const trace = {
            x: datosGrafico.x,
            y: datosGrafico.y,
            z: datosGrafico.z,
            type: 'scatter3d',
            mode: 'lines',
            line: {
                color: '#3b82f6',
                width: 3
            }
        };

        const layout = {
            scene: {
                xaxis: { title: datosGrafico.labels?.x || 'X' },
                yaxis: { title: datosGrafico.labels?.y || 'Y' },
                zaxis: { title: datosGrafico.labels?.z || 'Z' },
                camera: {
                    eye: { x: 1.5, y: 1.5, z: 1.5 }
                }
            },
            paper_bgcolor: '#1e293b',
            plot_bgcolor: '#1e293b'
        };

        Plotly.newPlot('graficoContainer', [trace], layout, {
            responsive: true
        });
    } else {
        // Gráfico 2D (código actual)
        // ... mantener como está
    }
}
```

**Paso 3: Actualizar fórmulas en Supabase**

Añadir campo `dimension` a la tabla `formulas`:
```sql
ALTER TABLE formulas ADD COLUMN dimension INTEGER DEFAULT 2;

UPDATE formulas SET dimension = 3
WHERE nombre IN (
    'Tiro Parabólico',
    'Movimiento Circular',
    'Espiral',
    'Hélice',
    'Paraboloide',
    'Esfera'
);
```

**Complejidad:** Media-Alta
**Tiempo estimado:** 4-6 horas
**Prioridad:** Alta (requisito original incumplido)

---

### 🔴 PROBLEMA 4: Área de visualización pequeña en pantallas grandes

**Severidad:** Media
**Estado:** UX mejorable

#### Descripción del problema:

**Contexto:**
- Usuario tiene monitor de 27 pulgadas (2560x1440 o 2560x1080)
- El área del gráfico se ve "enano" en esa resolución

**Código actual (index.html línea 85-100):**
```html
<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
    <!-- Gráfico: 2/3 del ancho en desktop -->
    <div class="lg:col-span-2">
        <div id="graficoContainer" style="min-height: 500px;"></div>
    </div>

    <!-- Controles: 1/3 del ancho -->
    <div class="lg:col-span-1">
        <!-- ... -->
    </div>
</div>
```

**Problema:**
- `lg:col-span-2` significa "2 de 3 columnas" = 66% del ancho
- En una pantalla de 2560px: 66% = 1706px de ancho
- Pero `min-height: 500px` → El gráfico es más ancho que alto
- Desproporcionado en pantallas grandes

**Layout actual:**
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│     Gráfico (2/3)            │  Controles (1/3)       │
│     min-height: 500px        │                        │
│                              │                        │
└─────────────────────────────────────────────────────────┘
```

**En 27":**
- Ancho gráfico: ~1700px
- Alto gráfico: 500px
- Ratio: 3.4:1 (muy panorámico)

#### Solución propuesta:

**Opción 1: Responsive height (recomendado)**

Usar CSS para adaptar la altura según el tamaño de pantalla:

```html
<div id="graficoContainer" class="grafico-responsive"></div>
```

```css
/* frontend/css/styles.css */
.grafico-responsive {
    /* Móvil: altura fija pequeña */
    min-height: 400px;
}

@media (min-width: 768px) {
    /* Tablet: altura media */
    .grafico-responsive {
        min-height: 600px;
    }
}

@media (min-width: 1024px) {
    /* Desktop: altura proporcional al ancho */
    .grafico-responsive {
        min-height: 700px;
    }
}

@media (min-width: 1920px) {
    /* Pantalla grande: altura máxima */
    .grafico-responsive {
        min-height: 900px;
    }
}
```

**Opción 2: Altura basada en viewport**

```css
.grafico-responsive {
    /* 70% de la altura de la ventana */
    height: 70vh;
    min-height: 500px;
}
```

**Ventajas:**
- Se adapta automáticamente a cualquier pantalla
- En 27" usa 70% de 1440px = 1008px de alto
- Mejor proporción

**Opción 3: Layout alternativo para pantallas grandes**

En pantallas >2000px, cambiar a layout vertical:

```css
@media (min-width: 2000px) {
    .grid-container {
        grid-template-rows: 2fr 1fr; /* 2/3 arriba, 1/3 abajo */
        grid-template-columns: 1fr;
    }
}
```

```
┌──────────────────────────────────┐
│                                  │
│     Gráfico (2/3 altura)         │
│                                  │
├──────────────────────────────────┤
│     Controles (1/3 altura)       │
└──────────────────────────────────┘
```

**Recomendación:** **Opción 1 + Opción 2** combinadas.

**Archivos a modificar:**
- `frontend/index.html` (añadir clase)
- `frontend/css/styles.css` (añadir reglas responsive)

---

## 🛠️ PLAN DE TRABAJO PROPUESTO

### Fase 6.1: Corrección de Bugs Críticos
**Prioridad:** Alta
**Tiempo estimado:** 2-3 horas

1. **Problema 1: Arreglar inputs dinámicos**
   - [ ] Conectar a Supabase con script Python
   - [ ] Leer todas las fórmulas
   - [ ] Identificar las que tienen `variables_usuario` como array
   - [ ] Convertir manualmente a objeto
   - [ ] Actualizar en Supabase
   - [ ] Probar en localhost
   - [ ] Verificar en producción

2. **Problema 2: Ocultar spinners de inputs**
   - [ ] Añadir CSS para ocultar spinners
   - [ ] Probar en Chrome, Firefox, Safari
   - [ ] Commit y push

### Fase 6.2: Implementación de Gráficos 3D
**Prioridad:** Alta
**Tiempo estimado:** 4-6 horas

3. **Problema 3: Gráficos 3D**
   - [ ] Añadir campo `dimension` en Supabase
   - [ ] Marcar fórmulas 3D en BD
   - [ ] Modificar `calculadora.py` para detectar y calcular Z
   - [ ] Modificar `app.js` para renderizar 3D cuando corresponda
   - [ ] Probar cada fórmula 3D en localhost
   - [ ] Ajustar cámara, colores, ejes
   - [ ] Commit y push

### Fase 6.3: Mejoras de UX
**Prioridad:** Media
**Tiempo estimado:** 1-2 horas

4. **Problema 4: Responsive para pantallas grandes**
   - [ ] Añadir media queries en CSS
   - [ ] Probar en diferentes resoluciones
   - [ ] Ajustar breakpoints
   - [ ] Commit y push

---

## 📊 ARQUITECTURA TÉCNICA AFECTADA

### Archivos que requieren modificación:

#### Backend:
```
backend/
├── services/
│   └── calculadora.py    ← Añadir cálculo de Z, detectar 3D
└── routes/
    └── calculos.py       ← Devolver campo tipo_grafico
```

#### Frontend:
```
frontend/
├── index.html            ← Añadir clase responsive a graficoContainer
├── css/
│   └── styles.css        ← Añadir media queries + ocultar spinners
└── js/
    └── app.js            ← Modificar renderizarGrafico() para 3D
```

#### Base de datos:
```sql
-- Añadir campo dimension
ALTER TABLE formulas ADD COLUMN dimension INTEGER DEFAULT 2;

-- Actualizar fórmulas 3D
UPDATE formulas SET dimension = 3 WHERE nombre IN (...);

-- Verificar consistencia de variables_usuario
-- Convertir arrays a objetos
```

---

## 🧪 TESTING REQUERIDO

### Después de cada corrección:

#### Test 1: Inputs dinámicos
- [ ] MRU muestra "Velocidad", "Posición inicial"
- [ ] MRUA muestra variables correctas (no 0,1,2,3)
- [ ] Caída Libre muestra variables correctas
- [ ] Todas las 15 fórmulas muestran labels descriptivas

#### Test 2: Inputs sin spinners
- [ ] Chrome: spinners ocultos
- [ ] Firefox: spinners ocultos
- [ ] Safari: spinners ocultos
- [ ] Teclado numérico aparece en móvil

#### Test 3: Gráficos 3D
- [ ] Fórmulas 2D siguen funcionando (MRU, MRUA, Caída Libre)
- [ ] Tiro Parabólico renderiza en 3D con trayectoria
- [ ] Espiral muestra 3 ejes X, Y, Z
- [ ] Cámara 3D permite rotar con mouse
- [ ] Zoom funciona en gráficos 3D

#### Test 4: Responsive
- [ ] Móvil (375px): gráfico 400px alto
- [ ] Tablet (768px): gráfico 600px alto
- [ ] Desktop (1920px): gráfico 700px alto
- [ ] Monitor 27" (2560px): gráfico 900px alto
- [ ] No desborda, no scroll horizontal

---

## 📝 NOTAS ADICIONALES

### Consideraciones de despliegue:

**Flujo de trabajo recomendado:**
1. **Crear rama `dev`** para trabajar
2. Hacer cambios en `dev`
3. Probar en localhost
4. Hacer commit a `dev`
5. Cloudflare genera preview URL automáticamente
6. Verificar en preview
7. Si todo funciona → **Merge a `main`**
8. Cloudflare despliega en producción

**Ventaja:**
- Producción (`formulas-web.pages.dev`) NUNCA se rompe
- Pruebas en preview URL primero

### Librerías ya disponibles:

- ✅ Plotly.js soporta 3D (tipo `scatter3d`)
- ✅ MathJax renderiza LaTeX
- ✅ DaisyUI + Tailwind para estilos

**NO necesitas instalar nada nuevo** para implementar 3D.

### Referencias útiles:

**Plotly 3D:**
- Documentación: https://plotly.com/javascript/3d-scatter-plots/
- Ejemplos: https://plotly.com/javascript/3d-line-plots/

**Tailwind responsive:**
- Breakpoints: https://tailwindcss.com/docs/responsive-design
- Media queries personalizadas: `@screen lg { ... }`

---

## ✅ CRITERIOS DE ACEPTACIÓN

**La Fase 6 estará completa cuando:**

- [ ] **Todas las 15 fórmulas** muestran inputs con nombres descriptivos (no números)
- [ ] Inputs de número **NO muestran flechas** arriba/abajo
- [ ] Fórmulas 2D muestran gráficos 2D correctamente
- [ ] **Fórmulas 3D muestran gráficos 3D interactivos** con ejes X, Y, Z
- [ ] Gráficos se ven proporcionales en pantallas de **27 pulgadas**
- [ ] **Todo funciona en localhost** antes de subir a producción
- [ ] **Todo funciona en producción** (Cloudflare + Railway)
- [ ] **Documentación actualizada** en `docs/aprendizaje/`

---

*Documento creado: 7 Enero 2026*
*Próxima fase: Corrección de bugs y mejoras UX*
