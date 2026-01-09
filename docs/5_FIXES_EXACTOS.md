# 5 FIXES EXACTOS - Copiar y Ejecutar
# Fecha: 9 Enero 2026
# Sin documentación extra, solo código que funciona

## FIX 1: Lorenz NaN (Backend)

**Archivo:** `backend/services/calculadora.py`
**Buscar función:** `calcular_lorenz`
**Reemplazar TODA la función por:**

```python
def calcular_lorenz(sigma: float = 10.0, rho: float = 28.0, beta: float = 2.667, 
                    t_max: float = 50.0, puntos: int = 5000) -> dict:
    """Atractor de Lorenz con protección contra NaN/Inf"""
    dt = t_max / puntos
    x, y, z = 1.0, 1.0, 1.0
    xs, ys, zs = [x], [y], [z]
    
    for _ in range(puntos - 1):
        dx = sigma * (y - x) * dt
        dy = (x * (rho - z) - y) * dt
        dz = (x * y - beta * z) * dt
        
        x += dx
        y += dy
        z += dz
        
        # Protección: si explota, parar
        if not (np.isfinite(x) and np.isfinite(y) and np.isfinite(z)):
            break
        if abs(x) > 1000 or abs(y) > 1000 or abs(z) > 1000:
            break
            
        xs.append(x)
        ys.append(y)
        zs.append(z)
    
    return {"x": xs, "y": ys, "z": zs}
```

---

## FIX 2: Renderizado 3D (Frontend)

**Archivo:** `frontend/js/graficos.js`
**Buscar función:** `renderizarGrafico`
**Añadir AL INICIO de la función, después de obtener `resultado`:**

```javascript
function renderizarGrafico(datosCalculo, formula) {
    const container = document.getElementById('graficoContainer');
    const resultado = datosCalculo.resultado || datosCalculo;
    
    // NUEVO: Detectar si es 3D
    const es3D = resultado.z !== undefined && Array.isArray(resultado.z) && resultado.z.length > 0;
    
    if (es3D) {
        // Renderizado 3D
        const trace = {
            type: 'scatter3d',
            mode: 'lines',
            x: resultado.x,
            y: resultado.y,
            z: resultado.z,
            line: {
                color: resultado.z,
                colorscale: 'Viridis',
                width: 3
            }
        };
        
        const layout = {
            scene: {
                xaxis: { title: 'X', gridcolor: '#334155', color: '#94a3b8' },
                yaxis: { title: 'Y', gridcolor: '#334155', color: '#94a3b8' },
                zaxis: { title: 'Z', gridcolor: '#334155', color: '#94a3b8' },
                bgcolor: '#0f172a',
                camera: { eye: { x: 1.5, y: 1.5, z: 1.2 } }
            },
            paper_bgcolor: '#0f172a',
            margin: { l: 0, r: 0, t: 30, b: 0 }
        };
        
        Plotly.newPlot(container, [trace], layout, { responsive: true });
        return; // Salir, no ejecutar código 2D
    }
    
    // ... resto del código 2D existente continúa aquí ...
```

---

## FIX 3: Filtrado por Tabs (Frontend)

**Archivo:** `frontend/js/app.js`
**Añadir AL INICIO del archivo (después de las primeras variables):**

```javascript
// Variables globales para filtrado
let todasLasFormulas = [];
let modoActual = '2d';
```

**Buscar función:** `cargarFormulas`
**Modificar para guardar todas las fórmulas:**

```javascript
async function cargarFormulas() {
    const selector = document.getElementById('formulaSelector');
    
    // Obtener fórmulas
    const formulas = await api.obtenerFormulas();
    todasLasFormulas = formulas; // NUEVO: Guardar todas
    
    // Filtrar según modo actual
    filtrarFormulas(modoActual);
}
```

**Añadir función nueva (después de cargarFormulas):**

```javascript
function filtrarFormulas(modo) {
    const selector = document.getElementById('formulaSelector');
    selector.innerHTML = '';
    
    // Opción por defecto
    const optDefault = document.createElement('option');
    optDefault.disabled = true;
    optDefault.selected = true;
    optDefault.textContent = 'Selecciona una fórmula...';
    selector.appendChild(optDefault);
    
    // Filtrar: 3D = categoria 'geometria_3d', 2D = todo lo demás
    const filtradas = modo === '3d'
        ? todasLasFormulas.filter(f => f.categoria === 'geometria_3d')
        : todasLasFormulas.filter(f => f.categoria !== 'geometria_3d');
    
    filtradas.forEach(formula => {
        const option = document.createElement('option');
        option.value = formula.id;
        option.textContent = formula.nombre;
        selector.appendChild(option);
    });
    
    // Seleccionar primera si hay
    if (filtradas.length > 0) {
        selector.selectedIndex = 1;
    }
}
```

---

## FIX 4: Event Listeners Tabs (Frontend)

**Archivo:** `frontend/js/app.js`
**Buscar función:** `configurarEventListeners`
**Añadir dentro de esa función:**

```javascript
function configurarEventListeners() {
    // ... código existente ...
    
    // NUEVO: Tabs 2D/3D
    const tab2D = document.getElementById('tab2D');
    const tab3D = document.getElementById('tab3D');
    
    if (tab2D && tab3D) {
        tab2D.addEventListener('click', () => {
            modoActual = '2d';
            tab2D.classList.add('tab-active');
            tab3D.classList.remove('tab-active');
            filtrarFormulas('2d');
        });
        
        tab3D.addEventListener('click', () => {
            modoActual = '3d';
            tab3D.classList.add('tab-active');
            tab2D.classList.remove('tab-active');
            filtrarFormulas('3d');
        });
        
        // Activar 2D por defecto
        tab2D.classList.add('tab-active');
    }
}
```

---

## FIX 5: CSS Tab Activo (Frontend)

**Archivo:** `frontend/css/styles.css`
**Buscar:** `.tab-redesign` o similar
**Añadir si no existe:**

```css
.tab-active {
    background: linear-gradient(135deg, #3b82f6, #8b5cf6) !important;
    color: white !important;
    border-color: #3b82f6 !important;
}
```

---

## ORDEN DE EJECUCIÓN

```bash
# 1. Backend primero
cd /Volumes/Akitio01/Claude_MCP/formulas-web
# Editar backend/services/calculadora.py (FIX 1)

# 2. Probar backend
source venv/bin/activate
uvicorn backend.main:app --reload
# En otra terminal:
curl "http://localhost:8000/api/calcular" -X POST -H "Content-Type: application/json" -d '{"formula_id": 17, "valores": {"sigma": 10, "rho": 28, "beta": 2.667, "t_max": 50}}'
# Debe devolver JSON con x, y, z (sin error NaN)

# 3. Frontend
# Editar frontend/js/graficos.js (FIX 2)
# Editar frontend/js/app.js (FIX 3 + 4)
# Editar frontend/css/styles.css (FIX 5)

# 4. Probar frontend
cd frontend
python3 -m http.server 3000
# Abrir http://localhost:3000
# - Click tab 3D → solo fórmulas 3D
# - Seleccionar Hélice → gráfico rotable 3D
# - Seleccionar Lorenz → atractor sin error

# 5. Si todo OK
git add .
git commit -m "Fix: 3D rendering, tabs filtering, Lorenz NaN"
git push
```

---

## TESTS DE VERIFICACIÓN

| Test | Resultado esperado |
|------|-------------------|
| Tab 2D click | Solo MRU, MRUA, Parábola, etc. |
| Tab 3D click | Solo Hélice, Lorenz, Toro, Ondas |
| Hélice calcular | Gráfico 3D rotable con espiral |
| Lorenz calcular | Atractor caótico 3D (sin error) |
| Tab activo | Fondo azul/púrpura en tab seleccionado |
