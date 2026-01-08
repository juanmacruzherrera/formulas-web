# Estado FASE 6.4 - Problemas y Soluciones Pendientes
**Fecha**: 2026-01-08
**Sesión**: Después de compactación y continuación
**Contexto**: Implementación de fórmulas 3D (Hélice, Lorenz, Toro, Ondas)

---

## ✅ LO QUE ESTÁ COMPLETO (FASES ANTERIORES)

### FASE 6.1 ✅
- [x] Variables parseadas correctamente (JSON string → object)
- [x] Inputs sin spinners (CSS cross-browser)
- [x] Commit: `95ccda5` + `9adb3db`

### FASE 6.2 ✅
- [x] Layout lateral 75%-25% (luego 80%-20%)
- [x] Header con tabs 2D/3D (UI creada)
- [x] Sin scroll infinito
- [x] Commit: `d35def1` + `011d51a` + `4f44ff9`

### FASE 6.3 ✅
- [x] Sistema de animación 2D creado (`frontend/js/animacion.js`)
- [x] Funciones: `animarCurva2D()`, `animarCurva3D()`
- [x] Integrado en `graficos.js`
- [x] Commit: `011d51a`

### FASE 6.4 - BACKEND ✅
- [x] 4 funciones 3D añadidas a `calculadora.py`:
  - `calcular_helice()` → x, y, z
  - `calcular_lorenz()` → x, y, z (atractor caótico)
  - `calcular_toro()` → x, y, z (superficie)
  - `calcular_ondas_3d()` → x, y, z (ondas circulares)
- [x] Rutas añadidas a `calculos.py` (elif blocks)
- [x] 4 fórmulas insertadas en Supabase (IDs 16-19)
- [x] Script: `backend/scripts/insertar_formulas_3d.py`
- [x] Fix Lemniscata NaN (filtrado con máscara booleana)

---

## ❌ PROBLEMAS ACTUALES (FASE 6.4 - FRONTEND)

### **PROBLEMA 1: Filtrado de Fórmulas por Tab** ❌
**Síntomas:**
- Tab "Gráficos 2D" muestra TODAS las fórmulas (2D + 3D)
- Tab "Gráficos 3D" muestra TODAS las fórmulas (2D + 3D)
- Captura 2: "Ondas 3D" aparece cuando está en tab 3D
- Captura 3: "Hélice 3D" aparece cuando está en tab 3D

**Causa:**
- `frontend/js/app.js` NO filtra el selector por categoría
- Los event listeners de los tabs (`tab2D`, `tab3D`) no existen o no filtran
- `cargarFormulas()` muestra todas sin distinción

**Ubicación:**
- `frontend/js/app.js` líneas ~60-90 (cargarFormulas)
- `frontend/js/app.js` líneas ~40-50 (inicialización)

**Solución requerida:**
```javascript
// En app.js, añadir:
let modoActual = '2d'; // Estado global

document.getElementById('tab2D').addEventListener('click', () => {
    modoActual = '2d';
    filtrarFormulas('2d');
    // Cambiar estilos de tabs
});

document.getElementById('tab3D').addEventListener('click', () => {
    modoActual = '3d';
    filtrarFormulas('3d');
    // Cambiar estilos de tabs
});

function filtrarFormulas(modo) {
    const formulas = todasLasFormulas; // Variable global
    const selector = document.getElementById('formulaSelector');
    selector.innerHTML = '<option disabled selected>Selecciona una fórmula</option>';

    const filtradas = modo === '2d'
        ? formulas.filter(f => f.categoria !== 'geometria_3d')
        : formulas.filter(f => f.categoria === 'geometria_3d');

    filtradas.forEach(f => {
        const option = document.createElement('option');
        option.value = f.id;
        option.textContent = f.nombre;
        selector.appendChild(option);
    });
}
```

---

### **PROBLEMA 2: Gráficos 3D se Renderizan en 2D** ❌
**Síntomas:**
- Captura 1 (Lorenz): Se ve como líneas 2D planas (sin profundidad)
- Captura 2 (Ondas 3D): Se ve como líneas 2D horizontales
- Captura 3 (Hélice 3D): Se ve como elipse 2D plana
- Los datos SÍ tienen x, y, z (verificado con API test)

**Causa:**
- `frontend/js/graficos.js` usa `renderizarGrafico()` para TODO
- `renderizarGrafico()` SIEMPRE usa `type: 'scatter'` (2D)
- NO detecta si resultado tiene propiedad `z`
- NO usa `type: 'scatter3d'` de Plotly

**Ubicación:**
- `frontend/js/graficos.js` líneas ~50-150 (`renderizarGrafico()`)
- `frontend/js/app.js` líneas ~330-340 (llama a renderizarGrafico)

**Solución requerida:**
```javascript
// En graficos.js, modificar renderizarGrafico():
function renderizarGrafico(datosCalculo, formula) {
    const resultado = datosCalculo.resultado;
    const es3D = resultado.z !== undefined && resultado.z.length > 0;

    if (es3D) {
        // Renderizar 3D con scatter3d
        const trace = {
            type: 'scatter3d',
            mode: 'lines',
            x: resultado.x,
            y: resultado.y,
            z: resultado.z,
            line: {
                color: resultado.z,  // Color basado en Z
                colorscale: 'Viridis',
                width: 4
            },
            name: formula.nombre
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
            font: { color: '#94a3b8' },
            showlegend: false,
            margin: { l: 0, r: 0, t: 0, b: 0 }
        };

        Plotly.newPlot(container, [trace], layout, config);
    } else {
        // Código 2D existente...
    }
}
```

---

### **PROBLEMA 3: Sin Controles 3D (Play/Pause/Slider)** ❌
**Síntomas:**
- Captura 1, 2, 3: No aparece botón Play/Pause
- No aparece slider de progreso
- No hay animación de construcción progresiva de la curva

**Causa:**
- `animacion.js` tiene `animarCurva3D()` implementada ✅
- Pero `graficos.js` NO la llama
- `renderizarGraficoAnimado()` existe pero no se integró
- `app.js` llama a `renderizarGrafico()` directamente, no a `renderizarGraficoAnimado()`

**Ubicación:**
- `frontend/js/graficos.js` líneas ~327-381 (`renderizarGraficoAnimado()`)
- `frontend/js/app.js` líneas ~330-340 (realizarCalculo)

**Solución requerida:**
```javascript
// En app.js, cambiar la llamada:
// ANTES:
window.graficos.renderizarGrafico(datosCalculo, formulaSeleccionada);

// DESPUÉS:
const es3D = datosCalculo.resultado.z !== undefined;
if (es3D) {
    window.animacion.animarCurva3D(datosCalculo.resultado, 5000);
} else {
    window.graficos.renderizarGrafico(datosCalculo, formulaSeleccionada);
}
```

**Nota:** La función `animarCurva3D()` ya tiene:
- Botones Play/Pause (updatemenus)
- Slider de progreso (sliders)
- Frames de animación (addFrames)

---

### **PROBLEMA 4: Atractor de Lorenz - Error NaN** ❌
**Síntomas:**
- Captura 1 (error toast): "Error al procesar el cálculo: Out of range float values are not JSON compliant: nan"
- Similar al error de Lemniscata (ya resuelto)

**Causa:**
- `calcular_lorenz()` usa integración de Euler
- Con parámetros clásicos (σ=10, ρ=28, β=8/3), el sistema puede generar valores muy grandes
- Si x, y o z crecen sin límite → overflow → `inf` o `-inf`
- Si hay división por cero → `nan`
- PostgreSQL/Supabase rechaza `nan` e `inf` en JSON

**Ubicación:**
- `backend/services/calculadora.py` líneas 230-269 (`calcular_lorenz()`)

**Solución requerida:**
```python
def calcular_lorenz(sigma: float, rho: float, beta: float, t_max: float, puntos: int = 2000) -> dict:
    """Atractor de Lorenz con filtrado de NaN/Inf"""
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

        # FILTRAR: Si algún valor es NaN o Inf, detener
        if not (np.isfinite(x) and np.isfinite(y) and np.isfinite(z)):
            print(f"⚠️ Lorenz: Valores infinitos detectados en iteración {_}")
            break

        xs.append(x)
        ys.append(y)
        zs.append(z)

    return {"x": xs, "y": ys, "z": zs}
```

**Alternativa:** Usar límites (clipping):
```python
# Limitar valores a rango razonable
MAX_VAL = 1000
x = np.clip(x, -MAX_VAL, MAX_VAL)
y = np.clip(y, -MAX_VAL, MAX_VAL)
z = np.clip(z, -MAX_VAL, MAX_VAL)
```

---

### **PROBLEMA 5: Tab Switching Visual** ❌
**Síntomas:**
- Captura 1, 2, 3: Los tabs 2D y 3D se ven, pero no cambian de estilo al hacer clic
- No hay indicador visual de cuál está activo

**Causa:**
- CSS tiene clase `.tab-active` definida
- Pero JS no añade/quita esta clase al hacer clic

**Ubicación:**
- `frontend/index.html` líneas 80-91 (tabs HTML)
- `frontend/css/styles.css` (estilos de `.tab-redesign` y `.tab-active`)
- `frontend/js/app.js` (event listeners faltantes)

**Solución requerida:**
```javascript
// En app.js:
document.getElementById('tab2D').addEventListener('click', () => {
    modoActual = '2d';

    // Cambiar estilos
    document.getElementById('tab2D').classList.add('tab-active');
    document.getElementById('tab3D').classList.remove('tab-active');

    filtrarFormulas('2d');
    limpiarGrafico();
});

document.getElementById('tab3D').addEventListener('click', () => {
    modoActual = '3d';

    // Cambiar estilos
    document.getElementById('tab3D').classList.add('tab-active');
    document.getElementById('tab2D').classList.remove('tab-active');

    filtrarFormulas('3d');
    limpiarGrafico();
});
```

---

## 📋 CHECKLIST DE TAREAS PENDIENTES

### Frontend (JavaScript)
- [ ] **TAREA 1**: Añadir filtrado de fórmulas por categoría
  - Archivo: `frontend/js/app.js`
  - Función: `filtrarFormulas(modo)`
  - Variable global: `let todasLasFormulas = []`

- [ ] **TAREA 2**: Añadir event listeners para tabs 2D/3D
  - Archivo: `frontend/js/app.js`
  - Eventos: `tab2D.click`, `tab3D.click`
  - Cambiar clase `.tab-active`

- [ ] **TAREA 3**: Detectar datos 3D y usar scatter3d
  - Archivo: `frontend/js/graficos.js`
  - Modificar: `renderizarGrafico()`
  - Condición: `if (resultado.z !== undefined)`

- [ ] **TAREA 4**: Integrar animación 3D con controles
  - Archivo: `frontend/js/app.js`
  - Modificar: `realizarCalculo()`
  - Llamar: `window.animacion.animarCurva3D()`

### Backend (Python)
- [ ] **TAREA 5**: Filtrar NaN/Inf en Lorenz
  - Archivo: `backend/services/calculadora.py`
  - Función: `calcular_lorenz()`
  - Añadir: `np.isfinite()` check o `np.clip()`

---

## 🔧 ARCHIVOS A MODIFICAR

### 1. `frontend/js/app.js`
**Líneas a modificar:**
- ~40-50: Añadir `let modoActual = '2d'` y `let todasLasFormulas = []`
- ~60-90: Modificar `cargarFormulas()` para guardar en variable global
- ~350-370: Añadir event listeners tabs + función `filtrarFormulas()`
- ~330-340: Modificar `realizarCalculo()` para detectar 3D y usar animación

### 2. `frontend/js/graficos.js`
**Líneas a modificar:**
- ~50-150: Modificar `renderizarGrafico()` para detectar `resultado.z`
- ~60-80: Añadir bloque `if (es3D)` con `type: 'scatter3d'`

### 3. `backend/services/calculadora.py`
**Líneas a modificar:**
- ~230-269: Modificar `calcular_lorenz()` para filtrar NaN/Inf

---

## 📊 ESTADO ACTUAL DEL CÓDIGO

### Backend ✅
```
backend/services/calculadora.py
  ├─ calcular_helice()          ✅ Funciona (test API OK)
  ├─ calcular_lorenz()          ❌ Genera NaN/Inf
  ├─ calcular_toro()            ⚠️  No testeado
  └─ calcular_ondas_3d()        ⚠️  No testeado

backend/routes/calculos.py
  ├─ elif "Hélice"              ✅ Ruta OK
  ├─ elif "Lorenz"              ✅ Ruta OK (pero cálculo falla)
  ├─ elif "Toro"                ✅ Ruta OK
  └─ elif "Ondas 3D"            ✅ Ruta OK
```

### Frontend ❌
```
frontend/js/app.js
  ├─ cargarFormulas()           ❌ No filtra por categoría
  ├─ Event listeners tabs       ❌ No existen
  └─ realizarCalculo()          ❌ No detecta 3D

frontend/js/graficos.js
  ├─ renderizarGrafico()        ❌ Solo 2D (scatter)
  └─ renderizarGraficoAnimado() ✅ Existe pero no se usa

frontend/js/animacion.js
  ├─ animarCurva2D()            ✅ Funciona
  └─ animarCurva3D()            ✅ Existe pero no se llama
```

---

## 🎯 PRIORIDAD DE CORRECCIONES

### Alta Prioridad (Bloquean funcionalidad básica)
1. **Filtrado de fórmulas** (TAREA 1 + 2) → Sin esto, UX confusa
2. **Renderizado 3D** (TAREA 3) → Sin esto, 3D se ve plano
3. **Fix Lorenz NaN** (TAREA 5) → Sin esto, Lorenz no funciona

### Media Prioridad (Mejoran experiencia)
4. **Animación 3D** (TAREA 4) → Sin esto, no hay controles
5. **Estilos tabs** (parte de TAREA 2) → Feedback visual

---

## 📝 NOTAS PARA PRÓXIMA SESIÓN

### Contexto importante:
- Layout 80%-20% funcionando ✅
- Lemniscata NaN corregida ✅
- Backend 3D implementado ✅
- Frontend 3D PENDIENTE ❌

### Tests a realizar después de fixes:
1. Tab 2D → Solo muestra fórmulas 2D
2. Tab 3D → Solo muestra fórmulas 3D
3. Hélice 3D → Gráfico rotable con profundidad
4. Lorenz → Sin error NaN, atractor caótico visible
5. Toro → Superficie toroidal visible
6. Ondas 3D → Ondas circulares con altura

### Commits pendientes:
- Commit 1: Fix filtrado tabs + renderizado 3D
- Commit 2: Fix Lorenz NaN + animación 3D
- Commit 3: Tests completos FASE 6.4

---

## 🔗 REFERENCIAS

### Archivos clave:
- `/Volumes/Akitio01/Claude_MCP/formulas-web/frontend/js/app.js`
- `/Volumes/Akitio01/Claude_MCP/formulas-web/frontend/js/graficos.js`
- `/Volumes/Akitio01/Claude_MCP/formulas-web/backend/services/calculadora.py`

### Documentación relacionada:
- `docs/REDISENO_COMPLETO_V2.md` → Plan original FASE 6
- `docs/aprendizaje/17_rediseno_v2.md` → Cambios documentados

### Chat completo:
- `docs/chats_register/20250108_formulas_web_Claude_Code_CHAT_COMPLETO.txt`

---

**FIN DEL DOCUMENTO**
**Última actualización:** 2026-01-08 15:45
