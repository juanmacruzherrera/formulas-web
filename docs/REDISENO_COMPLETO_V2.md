# REDISEÑO COMPLETO: Visualizador de Fórmulas v2.0

> **ARQUITECTO:** Claude Opus
> **FECHA:** 8 Enero 2026
> **INSPIRACIÓN:** Desmos, GeoGebra, visualizaciones CFD con Plotly

---

## ⛔ REGLAS OBLIGATORIAS PARA CLAUDE CODE

### REGLA 1: DOCUMENTAR CADA CAMBIO CON DIFF

**ANTES de modificar cualquier archivo de código:**
1. Copia el código ANTES del cambio
2. Realiza el cambio
3. Documenta el DIFF en `docs/aprendizaje/17_rediseno_v2.md`

**Formato obligatorio:**
```markdown
### Cambio en `frontend/css/styles.css` - 8 Enero 2026 - 14:30

**Qué cambié:**
```diff
- /* No había nada para ocultar spinners */
+ /* Ocultar spinners de inputs numéricos */
+ input[type="number"]::-webkit-outer-spin-button,
+ input[type="number"]::-webkit-inner-spin-button {
+     -webkit-appearance: none;
+     margin: 0;
+ }
```

**Por qué lo cambié:**
Los spinners (flechas arriba/abajo) son molestos y no aportan valor.

**Resultado del test:**
✅ Chrome: Sin flechas
✅ Firefox: Sin flechas
```

### REGLA 2: TESTING OBLIGATORIO ANTES DE CADA PASO

**NUNCA pasar al siguiente paso sin verificar que el actual funciona.**

**Secuencia obligatoria:**

```
1. Escribir código
2. Guardar archivo
3. TEST EN TERMINAL:
   - Backend: curl http://localhost:8000/api/formulas
   - Frontend: abrir en navegador, inspeccionar consola
4. DOCUMENTAR RESULTADO:
   - Si funciona: ✅ + captura/evidencia
   - Si falla: ❌ + error exacto + diagnóstico + solución
5. SOLO SI FUNCIONA: pasar al siguiente paso
```

**Tests específicos por fase:**

| Fase | Test obligatorio |
|------|------------------|
| 6.1 Spinners | Abrir web → inputs no tienen flechas |
| 6.1 Variables | Seleccionar MRUA → muestra "x₀", "v₀", "a" (no 0,1,2) |
| 6.2 Layout | Gráfico ocupa >60% de la pantalla |
| 6.2 Responsive | Probar en 375px, 768px, 1920px, 2560px |
| 6.3 Animación | Click Play → curva se dibuja progresivamente |
| 6.4 Fórmulas 3D | Seleccionar Hélice → gráfico 3D rotable |

### REGLA 3: NO AVANZAR CON ERRORES

```
❌ MAL:
"Hay un error pero sigo con lo siguiente"

✅ BIEN:
"Hay un error. Lo diagnostico, lo soluciono, documento el proceso, verifico que funciona, y LUEGO sigo."
```

### REGLA 4: COMMITS PEQUEÑOS Y FRECUENTES

```bash
# Después de cada cambio que funcione:
git add .
git commit -m "Fix: Ocultar spinners en inputs numéricos"

# NO hacer commits gigantes con 10 cambios juntos
```

---

## 🎯 VISIÓN DEL PRODUCTO

**Actual:** Una herramienta "cutre" que funciona pero no inspira.

**Objetivo:** Una aplicación educativa profesional, visualmente atractiva, que:
- Muestre gráficas que ocupen el protagonismo (80% pantalla)
- Tenga animaciones que muestren la EVOLUCIÓN de las curvas
- Separe claramente 2D vs 3D
- Se adapte a cualquier pantalla (móvil → monitor 27")
- Inspire a estudiantes a explorar matemáticas

---

## 📐 ARQUITECTURA DE LA NUEVA UI

### Layout Principal (Desktop)

```
┌────────────────────────────────────────────────────────────────────────┐
│  HEADER: Logo + Título + Selector 2D/3D (tabs)                         │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│                                                                        │
│                     ÁREA DE VISUALIZACIÓN                              │
│                     (75-80% de la pantalla)                            │
│                                                                        │
│                     ┌─────────────────────────┐                        │
│                     │                         │                        │
│                     │      GRÁFICO            │                        │
│                     │      (Plotly)           │                        │
│                     │                         │                        │
│                     │   ▶️ Play/Pause         │                        │
│                     │   ━━━━━━━○━━━━━         │  ← Timeline animación  │
│                     └─────────────────────────┘                        │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤
│  PANEL INFERIOR (colapsable): Selector fórmula + Variables + Historial │
│                                                                        │
│  ┌──────────────┐  ┌─────────────────────────────┐  ┌────────────────┐ │
│  │  Categoría   │  │  Variables (inputs limpios) │  │   Historial    │ │
│  │  ▼ Física    │  │  x₀ = [____] m              │  │   (miniaturas) │ │
│  │    MRU       │  │  v  = [____] m/s            │  │                │ │
│  │    MRUA      │  │  ═══════○═══════ t: 0-10s   │  │                │ │
│  │  ▼ Curvas    │  │                             │  │                │ │
│  │    Espiral   │  │  [▶ Calcular y Animar]      │  │                │ │
│  └──────────────┘  └─────────────────────────────┘  └────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘
```

### Layout Móvil (< 768px)

```
┌─────────────────────┐
│  Header + 2D/3D     │
├─────────────────────┤
│                     │
│   GRÁFICO           │
│   (60vh)            │
│                     │
│  ▶️ ━━━━○━━━━       │
├─────────────────────┤
│  ▼ Configuración    │
│    (acordeón)       │
├─────────────────────┤
│  [Calcular]         │
└─────────────────────┘
```

---

## 🔧 CAMBIOS TÉCNICOS ESPECÍFICOS

### 1. INPUTS SIN SPINNERS (escribir números directamente)

**Archivo:** `frontend/css/styles.css`

```css
/* Inputs numéricos limpios - sin flechas */
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

/* Estilo limpio para inputs */
.input-variable {
    background: rgba(30, 41, 59, 0.8);
    border: 1px solid rgba(59, 130, 246, 0.3);
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 1.1rem;
    font-family: 'JetBrains Mono', monospace;
    color: #f1f5f9;
    width: 120px;
    text-align: right;
    transition: all 0.2s ease;
}

.input-variable:focus {
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
    outline: none;
}

/* Unidad al lado del input */
.input-group {
    display: flex;
    align-items: center;
    gap: 8px;
}

.input-unit {
    color: #94a3b8;
    font-size: 0.9rem;
}
```

---

### 2. SEPARAR SECCIONES 2D Y 3D

**Nueva estructura de navegación:**

```html
<!-- Header con tabs -->
<header class="header-main">
    <div class="logo">
        <span class="logo-icon">∫</span>
        <span class="logo-text">Visualizador de Fórmulas</span>
    </div>
    
    <nav class="nav-tabs">
        <button class="tab active" data-section="2d">
            <svg><!-- icono 2D --></svg>
            Gráficos 2D
        </button>
        <button class="tab" data-section="3d">
            <svg><!-- icono 3D --></svg>
            Gráficos 3D
        </button>
    </nav>
</header>
```

**Fórmulas por sección:**

| Sección 2D | Sección 3D (con animación) |
|------------|---------------------------|
| MRU | Tiro Parabólico 3D |
| MRUA | Hélice (espiral 3D) |
| Parábola | Superficie de onda |
| Seno/Coseno | Campo de temperatura |
| Exponencial | Flujo de fluido (streamlines) |
| Logarítmica | Atractor de Lorenz |
| Circunferencia | Esfera paramétrica |
| Cardioide | Toro (donut) |
| Lemniscata | Klein bottle |

---

### 3. ANIMACIÓN TEMPORAL (ver la gráfica construirse)

**Concepto:** El usuario ve cómo se dibuja la curva punto por punto, como si fuera un lápiz trazando.

**Implementación con Plotly:**

```javascript
// frontend/js/animacion.js

/**
 * Anima la construcción de una curva 2D
 * @param {Object} datos - {t: [...], x: [...]} o {x: [...], y: [...]}
 * @param {number} duracion - Duración en ms (default 3000)
 */
function animarCurva2D(datos, duracion = 3000) {
    const container = document.getElementById('graficoContainer');
    const totalPuntos = datos.x.length;
    const intervalo = duracion / totalPuntos;
    
    // Configuración inicial (vacío)
    const trace = {
        x: [],
        y: [],
        mode: 'lines',
        line: { color: '#3b82f6', width: 3 }
    };
    
    const layout = {
        paper_bgcolor: '#0f172a',
        plot_bgcolor: '#0f172a',
        xaxis: { 
            gridcolor: '#334155',
            zerolinecolor: '#475569',
            color: '#94a3b8'
        },
        yaxis: { 
            gridcolor: '#334155',
            zerolinecolor: '#475569',
            color: '#94a3b8'
        },
        margin: { l: 50, r: 20, t: 20, b: 50 }
    };
    
    Plotly.newPlot(container, [trace], layout, {responsive: true});
    
    // Animación punto por punto
    let i = 0;
    const timer = setInterval(() => {
        if (i >= totalPuntos) {
            clearInterval(timer);
            return;
        }
        
        // Añadir siguiente punto
        Plotly.extendTraces(container, {
            x: [[datos.x[i]]],
            y: [[datos.y[i] || datos.t[i]]]
        }, [0]);
        
        i++;
    }, intervalo);
    
    return timer; // Para poder pausar/cancelar
}

/**
 * Anima una curva 3D con evolución temporal
 */
function animarCurva3D(datos, duracion = 5000) {
    const container = document.getElementById('graficoContainer');
    const totalPuntos = datos.x.length;
    
    // Usar frames de Plotly para animación 3D
    const frames = [];
    const step = Math.max(1, Math.floor(totalPuntos / 100)); // Max 100 frames
    
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
    
    const trace = {
        type: 'scatter3d',
        mode: 'lines',
        x: datos.x.slice(0, 1),
        y: datos.y.slice(0, 1),
        z: datos.z.slice(0, 1),
        line: { 
            color: datos.z,
            colorscale: 'Viridis',
            width: 4
        }
    };
    
    const layout = {
        scene: {
            xaxis: { title: 'X', gridcolor: '#334155' },
            yaxis: { title: 'Y', gridcolor: '#334155' },
            zaxis: { title: 'Z/Tiempo', gridcolor: '#334155' },
            bgcolor: '#0f172a',
            camera: { eye: { x: 1.5, y: 1.5, z: 1.2 } }
        },
        paper_bgcolor: '#0f172a',
        updatemenus: [{
            type: 'buttons',
            showactive: false,
            y: 0,
            x: 0.1,
            buttons: [{
                label: '▶ Play',
                method: 'animate',
                args: [null, {
                    fromcurrent: true,
                    frame: { duration: duracion / frames.length },
                    transition: { duration: 0 }
                }]
            }, {
                label: '⏸ Pause',
                method: 'animate',
                args: [[null], {
                    mode: 'immediate',
                    frame: { duration: 0 }
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
                    frame: { duration: 0 }
                }]
            })),
            x: 0.1,
            len: 0.8,
            currentvalue: {
                prefix: 'Progreso: ',
                visible: true,
                xanchor: 'center'
            }
        }]
    };
    
    Plotly.newPlot(container, [trace], layout).then(() => {
        Plotly.addFrames(container, frames);
    });
}
```

---

### 4. NUEVAS FÓRMULAS 3D CON ANIMACIÓN

**Añadir a Supabase y calculadora.py:**

#### A) Hélice (Espiral 3D)
```python
def calcular_helice(a: float, b: float, c: float, t_min: float, t_max: float, puntos: int = 200) -> dict:
    """
    Hélice 3D: x = a*cos(t), y = a*sin(t), z = b*t
    
    Args:
        a: Radio de la hélice
        b: Paso vertical (cuánto sube por vuelta)
        c: Número de vueltas (usado para calcular t_max)
    """
    t = np.linspace(t_min, t_max, puntos)
    x = a * np.cos(t)
    y = a * np.sin(t)
    z = b * t
    return {"t": t.tolist(), "x": x.tolist(), "y": y.tolist(), "z": z.tolist(), "dimension": 3}
```

#### B) Atractor de Lorenz (caos)
```python
def calcular_lorenz(sigma: float = 10, rho: float = 28, beta: float = 8/3, 
                    dt: float = 0.01, steps: int = 10000) -> dict:
    """
    Sistema de Lorenz - visualización del caos
    dx/dt = σ(y - x)
    dy/dt = x(ρ - z) - y
    dz/dt = xy - βz
    """
    x, y, z = [0.1], [0.0], [0.0]
    
    for _ in range(steps - 1):
        dx = sigma * (y[-1] - x[-1]) * dt
        dy = (x[-1] * (rho - z[-1]) - y[-1]) * dt
        dz = (x[-1] * y[-1] - beta * z[-1]) * dt
        x.append(x[-1] + dx)
        y.append(y[-1] + dy)
        z.append(z[-1] + dz)
    
    return {"x": x, "y": y, "z": z, "dimension": 3, "tipo": "atractor"}
```

#### C) Superficie de onda (onda en agua)
```python
def calcular_onda_superficie(A: float, k: float, omega: float, 
                              x_min: float, x_max: float,
                              y_min: float, y_max: float,
                              t: float = 0, puntos: int = 50) -> dict:
    """
    Onda en superficie 2D: z = A * sin(k*r - ω*t)
    donde r = sqrt(x² + y²)
    """
    x = np.linspace(x_min, x_max, puntos)
    y = np.linspace(y_min, y_max, puntos)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    Z = A * np.sin(k * R - omega * t)
    
    return {
        "x": X.flatten().tolist(),
        "y": Y.flatten().tolist(),
        "z": Z.flatten().tolist(),
        "dimension": 3,
        "tipo": "superficie"
    }
```

#### D) Toro (Donut)
```python
def calcular_toro(R: float, r: float, u_max: float = 2*np.pi, 
                  v_max: float = 2*np.pi, puntos: int = 50) -> dict:
    """
    Toro paramétrico:
    x = (R + r*cos(v)) * cos(u)
    y = (R + r*cos(v)) * sin(u)
    z = r * sin(v)
    
    Args:
        R: Radio mayor (del centro del toro al centro del tubo)
        r: Radio menor (del tubo)
    """
    u = np.linspace(0, u_max, puntos)
    v = np.linspace(0, v_max, puntos)
    U, V = np.meshgrid(u, v)
    
    X = (R + r * np.cos(V)) * np.cos(U)
    Y = (R + r * np.cos(V)) * np.sin(U)
    Z = r * np.sin(V)
    
    return {
        "x": X.flatten().tolist(),
        "y": Y.flatten().tolist(),
        "z": Z.flatten().tolist(),
        "dimension": 3,
        "tipo": "superficie"
    }
```

---

### 5. DISEÑO RESPONSIVE (adaptarse a pantallas)

**Archivo:** `frontend/css/styles.css`

```css
/* === VARIABLES CSS === */
:root {
    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    --bg-tertiary: #334155;
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;
    --accent-blue: #3b82f6;
    --accent-purple: #8b5cf6;
    --accent-green: #10b981;
}

/* === LAYOUT PRINCIPAL === */
.app-container {
    display: grid;
    grid-template-rows: auto 1fr auto;
    min-height: 100vh;
    background: var(--bg-primary);
}

/* === ÁREA DE VISUALIZACIÓN === */
.visualization-area {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 1rem;
}

.graph-container {
    width: 100%;
    max-width: 1400px;
    aspect-ratio: 16/10;
    min-height: 400px;
    background: var(--bg-secondary);
    border-radius: 16px;
    border: 1px solid var(--bg-tertiary);
    overflow: hidden;
}

/* === RESPONSIVE === */

/* Móvil */
@media (max-width: 639px) {
    .graph-container {
        aspect-ratio: 4/3;
        min-height: 300px;
        border-radius: 12px;
    }
    
    .control-panel {
        flex-direction: column;
    }
    
    .input-variable {
        width: 100%;
    }
}

/* Tablet */
@media (min-width: 640px) and (max-width: 1023px) {
    .graph-container {
        aspect-ratio: 16/10;
        min-height: 450px;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    .graph-container {
        min-height: 550px;
    }
}

/* Monitor grande (27"+) */
@media (min-width: 1920px) {
    .graph-container {
        min-height: 700px;
        max-width: 1600px;
    }
    
    .visualization-area {
        padding: 2rem;
    }
}

/* Ultrawide */
@media (min-width: 2560px) {
    .graph-container {
        min-height: 800px;
        max-width: 2000px;
    }
}
```

---

### 6. PALETA DE COLORES PROFESIONAL

Inspirada en editores de código y Desmos:

```css
/* Fondo oscuro elegante */
--bg-gradient: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);

/* Acentos para gráficos */
--graph-line-1: #3b82f6;  /* Azul principal */
--graph-line-2: #8b5cf6;  /* Púrpura */
--graph-line-3: #10b981;  /* Verde */
--graph-line-4: #f59e0b;  /* Naranja */
--graph-line-5: #ef4444;  /* Rojo */

/* Gradientes para superficies 3D */
--surface-cool: Viridis;
--surface-warm: Inferno;
--surface-diverging: RdBu;
```

---

## 📋 PLAN DE IMPLEMENTACIÓN

### Fase 6.1: Correcciones Urgentes (2-3h)
1. ✅ Arreglar variables_usuario en Supabase (script Python)
2. ✅ CSS para ocultar spinners
3. ✅ Verificar que todo funciona

### Fase 6.2: Rediseño UI Base (4-6h)
1. Nuevo layout con grid CSS
2. Header con tabs 2D/3D
3. Panel de controles rediseñado
4. Responsive para móvil/tablet/desktop

### Fase 6.3: Sistema de Animación (4-6h)
1. Implementar animarCurva2D()
2. Implementar animarCurva3D()
3. Controles play/pause/slider
4. Integrar con cálculos existentes

### Fase 6.4: Nuevas Fórmulas 3D (6-8h)
1. Añadir fórmulas a Supabase
2. Implementar funciones en calculadora.py
3. Actualizar calculos.py con nuevos casos
4. Probar cada fórmula

### Fase 6.5: Polish y Testing (2-3h)
1. Ajustar colores y tipografía
2. Testing en diferentes dispositivos
3. Optimizar rendimiento
4. Deploy final

---

## 📊 MÉTRICAS DE ÉXITO

| Métrica | Actual | Objetivo |
|---------|--------|----------|
| Tamaño gráfico en desktop | ~30% pantalla | 70-80% pantalla |
| Tiempo de carga inicial | ~2s | < 1s |
| Fórmulas con animación | 0 | 15+ |
| Fórmulas 3D | 0 | 8-10 |
| Score móvil (Lighthouse) | No medido | > 90 |

---

## 🎨 REFERENCIAS DE DISEÑO

1. **Desmos** - Layout limpio, gráfico protagonista
2. **GeoGebra 3D** - Controles intuitivos para rotación
3. **Observable** - Notebooks interactivos
4. **Three.js examples** - Animaciones fluidas
5. **Awwwards data viz** - Estética premium

---

*Documento de arquitectura creado por Claude Opus*
*Para implementación por Claude Code*
