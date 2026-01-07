# Bitácora del Proyecto - Fórmulas Web

Registro de cambios y decisiones del proyecto.

---

## 2026-01-07 - FASE 5 COMPLETA: Mejoras de UX y preparación para deploy 🚀

### Resumen de cambios

Implementación de mejoras de interfaz de usuario y configuración para desplegar en producción.

**Pasos completados:** 2, 3, 4, 5, 6 (pasos 1, 7, 8 pendientes - manuales de Juan)

---

### ✨ PASO 2: Inputs dinámicos por fórmula

**Problema anterior:**
Todos los inputs mostraban "Posición inicial", "Velocidad" independientemente de la fórmula seleccionada.

**Solución implementada:**
- Creado diccionario `ETIQUETAS_VARIABLES` en `frontend/js/app.js` con 18 variables
- Función `generarInputsDinamicos()` ahora lee `formula.variables_usuario` y genera inputs según las claves
- Mapeo automático a etiquetas amigables (x0 → "Posición inicial x₀", etc.)
- Fallback: si variable no está en diccionario, usa el nombre técnico

**Resultado:**
✅ MRU muestra: x₀, v
✅ Parábola muestra: a, b, c
✅ Cardioide muestra: a
✅ Cada fórmula muestra solo sus variables específicas

**Archivo modificado:** `frontend/js/app.js` (líneas 135-204)

---

### 🎚️ PASO 3: Sliders para rangos

**Problema anterior:**
Los rangos (t_min, t_max) eran inputs numéricos poco intuitivos.

**Solución implementada:**
- Convertidos inputs a `<input type="range">` (sliders HTML5)
- Display del valor en tiempo real al mover el slider
- Configuración dinámica de min/max basada en `formula.rango_min`, `formula.rango_max`
- Clases de TailwindCSS: `range range-primary range-sm`

**Código clave:**
```javascript
slider.addEventListener('input', (e) => {
    valorDisplay.textContent = e.target.value;
});
```

**Resultado:**
✅ Interfaz más visual e interactiva
✅ Valores se actualizan en tiempo real
✅ Rango visible en el control

**Archivo modificado:** `frontend/js/app.js` (líneas 206-261)

---

### 🖼️ PASO 4: Layout invertido

**Problema anterior:**
Gráfica (contenido principal) a la derecha y pequeña. Controles a la izquierda.

**Solución implementada:**
- Invertido orden de columnas en `index.html`
- Gráfica ahora: `lg:col-span-2` (2/3 del ancho) a la IZQUIERDA
- Controles: `lg:col-span-1` (1/3 del ancho) a la DERECHA

**Resultado:**
✅ Gráfica prominente (lo primero que ve el usuario)
✅ Mejor uso del espacio de pantalla
✅ Sigue estándar de apps de visualización (Desmos, GeoGebra)

**Archivo modificado:** `frontend/index.html` (líneas 85-160)

---

### 📜 PASO 5: Historial lateral colapsable

**Problema anterior:**
Historial ocupaba sección completa al fondo de la página.

**Solución implementada:**

**En HTML:**
- Movido historial al panel derecho (dentro de la columna de controles)
- Implementado con componente `collapse` de DaisyUI
- Añadido `max-h-96 overflow-y-auto` para scroll vertical si hay muchos items

**En JavaScript:**
- Cambiado layout de cards de horizontal (`flex space-x-4`) a vertical (`space-y-2`)
- Reducido tamaño de miniaturas: `h-24` → `h-16`
- Ajustado padding y tamaños de fuente para espacio estrecho

**Resultado:**
✅ Historial colapsado por defecto (no distrae)
✅ Siempre accesible sin scroll largo
✅ Cards adaptadas a panel estrecho
✅ Mejor organización del espacio

**Archivos modificados:**
- `frontend/index.html` (líneas 158-179)
- `frontend/js/app.js` (líneas 357-392)

---

### 🚢 PASO 6: Preparación para deploy

#### 6.1 Verificar .gitignore ✅

**Resultado:** Ya incluye `.env`, `venv/`, `__pycache__/` - Sin cambios necesarios

---

#### 6.2 Crear Procfile ✅

**Archivo creado:** `Procfile` (raíz del proyecto)

**Contenido:**
```
web: uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

**Por qué:**
- Render necesita este archivo para saber cómo iniciar la app
- `$PORT` es variable de entorno asignada por Render
- `--host 0.0.0.0` permite conexiones externas

---

#### 6.3 Detección automática de entorno ✅

**Archivo modificado:** `frontend/js/api.js` (líneas 11-15)

**Cambio implementado:**
```javascript
const API_BASE = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:8000'
    : 'https://TU-BACKEND.onrender.com';
```

**Por qué:**
- En desarrollo: usa `localhost:8000`
- En producción: usa URL del backend desplegado
- **⚠️ IMPORTANTE para Juan:** Cambiar `TU-BACKEND.onrender.com` por URL real después del deploy

**Resultado:**
✅ Sin necesidad de cambiar código manualmente al desplegar
✅ Funciona automáticamente en ambos entornos

---

### 📊 Resumen de archivos modificados

| Archivo | Cambios | Líneas |
|---------|---------|--------|
| `frontend/js/app.js` | Inputs dinámicos + sliders + historial vertical | ~100 |
| `frontend/index.html` | Layout invertido + historial colapsable | ~30 |
| `frontend/js/api.js` | Detección de entorno | 4 |
| `Procfile` | **Creado** | 1 |
| `.gitignore` | Verificado (sin cambios) | 0 |

**Total:** ~135 líneas modificadas/añadidas

---

### 🎯 Estado del proyecto

**Fase 5 completada:** Pasos 2-6 ✅

**⚠️ IMPORTANTE - El proyecto NO está en GitHub todavía:**
- Ver guía completa: `docs/GUIA_GIT_GITHUB.md`
- Render y Cloudflare requieren que el código esté en GitHub

**Pendiente (pasos manuales de Juan):**
- **PASO 0 (PREVIO):** Subir a GitHub (ver `docs/GUIA_GIT_GITHUB.md`) ← **OBLIGATORIO PRIMERO**
- **PASO 1:** Configurar RLS en Supabase (SQL en `INSTRUCCIONES_FASE5.md`)
- **PASO 7-8:** Deploy backend en Render + frontend en Cloudflare Pages
- Actualizar URL en `api.js` tras deploy

**Documentación generada:**
- ✅ `docs/aprendizaje/16_fase5_mejoras_ui_deploy.md` - Documentación completa socratizada
- ✅ `docs/GUIA_JUAN_PASOS_MANUALES.md` - Actualizada con orden correcto
- ✅ `docs/GUIA_GIT_GITHUB.md` - Nueva guía para subir a GitHub
- ✅ Esta entrada en `docs/bitacora.md`

---

### 🎓 Aprendizajes clave

1. **Renderizado dinámico de UI**: Generar formularios basándose en estructura de datos de BD
2. **Mejora de UX**: Sliders > inputs numéricos para rangos
3. **Diseño responsive**: Uso efectivo de Tailwind Grid + DaisyUI components
4. **Deploy preparado**: Separación de entornos con detección automática

**Proyecto listo para producción** tras configuración manual de seguridad (RLS) y deploy 🚀

---

## 2025-12-30 - FASE 4 COMPLETA: Integración total con 15 fórmulas funcionando 🎉

### 🐛 Bug LaTeX corregido

**Problema detectado:**
La fórmula LaTeX mostraba `vcdott` en lugar del símbolo `·` (punto centrado).

**Causa:**
MathJax no estaba configurado correctamente. Necesita que el objeto de configuración exista **ANTES** de cargar el script.

**Solución aplicada:**
Modificado `frontend/index.html` para añadir configuración MathJax antes del CDN:

```html
<script>
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
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```

**Resultado:**
✅ Ahora `v \cdot t` se renderiza correctamente como v·t

---

### 📊 14 Fórmulas nuevas insertadas en Supabase

**Qué se hizo:**
- Creado script `insertar_formulas.py` en la raíz del proyecto
- Adaptada estructura de datos al esquema real de Supabase:
  - NO incluir columna "descripcion" (no existe)
  - `variables_usuario`: objeto plano `{variable: valor_default}`
  - Añadir campo `rango_dinamico: false`

**Fórmulas insertadas:**
1. **Física (5):** MRUA, Caída Libre, Tiro Parabólico, MAS, Onda Sinusoidal
2. **Matemáticas (5):** Parábola, Exponencial, Logarítmica, Seno, Circunferencia
3. **Curvas Exóticas (4):** Espiral de Arquímedes, Espiral Logarítmica, Cardioide, Lemniscata

**Resultado:**
✅ Total: **15 fórmulas** en la base de datos (1 existente + 14 nuevas)

**Verificación:**
```bash
python insertar_formulas.py
# Output: ✅ 14/14 fórmulas insertadas correctamente
```

---

### ⚙️ 14 Funciones de cálculo añadidas

**Archivo modificado:** `backend/services/calculadora.py`

**Funciones añadidas:**
- `calcular_mrua()`, `calcular_caida_libre()`, `calcular_tiro_parabolico()`
- `calcular_armonico_simple()`, `calcular_onda_sinusoidal()`
- `calcular_parabola()`, `calcular_exponencial()`, `calcular_logaritmica()`, `calcular_seno()`
- `calcular_circunferencia()`, `calcular_espiral_arquimedes()`, `calcular_espiral_logaritmica()`
- `calcular_cardioide()`, `calcular_lemniscata()`

**Características especiales:**
- `calcular_lemniscata()`: Maneja valores válidos con `np.where(cos_2theta >= 0)` y combina ambos lados de la curva
- `calcular_logaritmica()`: Evita `ln(0)` con `max(x_min, 0.001)`
- `calcular_caida_libre()`: Limita `y >= 0` con `np.maximum(y, 0)`

---

### 🔄 Endpoint actualizado para 15 fórmulas

**Archivo modificado:** `backend/routes/calculos.py`

**Cambios:**
1. Importadas las 15 funciones de calculadora.py
2. Añadidas 15 condiciones `if/elif` para detectar fórmula por nombre
3. Extracción dinámica de rangos usando `formula["variable_rango"]`

**Lógica de detección:**
```python
if "MRU" in formula["nombre"] and "Uniformemente Acelerado" not in formula["nombre"]:
    resultado = calcular_mru(...)
elif "MRUA" in formula["nombre"]:
    resultado = calcular_mrua(...)
elif "Parábola" in formula["nombre"]:
    resultado = calcular_parabola(...)
# ... 12 condiciones más
```

**Ventaja:** Sistema extensible. Añadir nueva fórmula = insertar en BD + añadir condición.

---

### 🎨 Frontend actualizado para curvas paramétricas

**Archivo modificado:** `frontend/js/graficos.js`

**Problema:**
El frontend solo manejaba datos `{t, x}`. Pero el backend devuelve 3 formatos:
1. **Temporal:** `{t, x}` o `{t, y}`
2. **Matemática:** `{x, y}`
3. **Paramétrica:** `{theta, x, y}`

**Solución:**
Detección automática del tipo de datos:

```javascript
if (resultado.t !== undefined) {
    // TIPO 1: Temporal
    xData = resultado.t;
    yData = resultado.x || resultado.y;
    xLabel = 't (tiempo)';
} else if (resultado.theta !== undefined) {
    // TIPO 2: Paramétrica
    xData = resultado.x;
    yData = resultado.y;
    xLabel = 'x';
    yLabel = 'y';
    // Aspect ratio 1:1 para círculos
    layout.yaxis.scaleanchor = 'x';
    layout.yaxis.scaleratio = 1;
} else {
    // TIPO 3: Matemática
    xData = resultado.x;
    yData = resultado.y;
}
```

**Resultado:**
✅ Circunferencias se ven como **círculos perfectos**, no elipses
✅ Espirales mantienen proporciones correctas
✅ Cardioide tiene forma de corazón correcta

**Funciones actualizadas:**
- `renderizarGrafico()`: Detecta tipo y configura ejes automáticamente
- `renderizarMiniaturaGrafico()`: Detecta tipo para historial

---

### ✅ Pruebas realizadas

**Backend:**
```bash
# Parábola (matemática)
curl -X POST http://localhost:8000/api/calcular \
  -d '{"formula_id": 7, "valores": {"a": 1, "b": 0, "c": 0}}'
# ✅ Devuelve {x: [...], y: [...]}

# Circunferencia (paramétrica)
curl -X POST http://localhost:8000/api/calcular \
  -d '{"formula_id": 11, "valores": {"r": 5}}'
# ✅ Devuelve {theta: [...], x: [...], y: [...]}
```

**Frontend:**
- ✅ MRU (id=1): Línea recta
- ✅ Parábola (id=7): Curva en U
- ✅ Función Seno (id=10): Onda senoidal
- ✅ Circunferencia (id=11): Círculo perfecto
- ✅ Espiral Logarítmica (id=13): Espiral que crece exponencialmente
- ✅ Cardioide (id=14): Forma de corazón ❤️

---

### 📚 Documentación creada

**Archivos generados:**
1. `docs/aprendizaje/13_integracion.md`:
   - Flujo completo extremo a extremo
   - Conceptos: 3 tipos de datos, detección automática, configuración MathJax
   - Lecciones: Verificar destino antes de escribir, diseño extensible, separación de responsabilidades

2. `docs/aprendizaje/14_todas_formulas.md`:
   - Catálogo completo de las 15 fórmulas
   - Parámetros, funciones de cálculo, gráficos esperados
   - Tabla resumen y guía para añadir nuevas fórmulas

---

### 🏆 Estado final del proyecto

| Fase | Tareas | Estado |
|------|--------|--------|
| 0. Preparación | 1/1 | ✅ 100% |
| 1. Conexión Python ↔ Supabase | 4/4 | ✅ 100% |
| 2. Lógica de cálculo | 3/3 | ✅ 100% |
| 3. Frontend básico | 4/4 | ✅ 100% |
| 4. Integración completa | 2/2 | ✅ 100% |
| **TOTAL** | **14/14** | **✅ 100%** |

**Componentes funcionando:**
- ✅ Backend FastAPI (puerto 8000)
- ✅ Frontend (puerto 3000)
- ✅ Supabase con 15 fórmulas
- ✅ Renderizado LaTeX con MathJax
- ✅ Gráficos interactivos con Plotly
- ✅ Detección automática de tipos de datos
- ✅ Historial con miniaturas
- ✅ Sistema extensible

---

### 🎓 Lecciones aprendidas

**1. Verificar destino antes de escribir código**
Principio aplicado en toda la fase:
- Backend → Frontend: Verificamos formato de respuesta ANTES de modificar graficos.js
- Python → Supabase: Verificamos columnas de la tabla ANTES de insertar
- Frontend → Plotly: Verificamos qué espera Plotly ANTES de construir trazas

**2. Error no encontrado != Bug inexistente**
El bug de LaTeX no generaba error en consola, solo se veía mal. Solución: inspección visual + lectura de documentación de MathJax.

**3. Diseño extensible es clave**
Sistema antes: `if formula_id == 1: calcular_mru()`
Sistema ahora: `if "MRU" in formula["nombre"]: calcular_mru()`

Añadir nueva fórmula ahora requiere:
- Insertar en Supabase
- Añadir función en calculadora.py
- Añadir condición en calculos.py
- **NO** modificar graficos.js ni app.js (detección automática)

---

## 2025-12-29 - FASE 3 COMPLETA: Frontend elegante con Tailwind + Plotly

### 🎨 PASO 0 (CRÍTICO): CORS añadido al backend

**Qué se hizo:**
- Modificado `backend/main.py` para añadir CORSMiddleware
- Importado `from fastapi.middleware.cors import CORSMiddleware`
- Configurado middleware con `allow_origins=["*"]` (desarrollo)

**Código añadido:**
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Por qué es crítico:**
Sin CORS, el navegador **bloquea** las peticiones HTTP desde el frontend (localhost:3000) al backend (localhost:8000). Esto es una política de seguridad del navegador llamada "Same-Origin Policy".

---

### 🚀 Tareas 3.1-3.4: Frontend completo con stack moderno

**Stack tecnológico implementado:**
- ✅ **Tailwind CSS + DaisyUI:** Estilos modernos con componentes pre-diseñados
- ✅ **Plotly.js:** Gráficos interactivos con zoom, hover, animaciones
- ✅ **MathJax:** Renderizado de fórmulas LaTeX ($$x = x_0 + v \cdot t$$)
- ✅ **Google Fonts Inter:** Tipografía moderna y limpia
- ✅ **Tema oscuro:** Paleta slate-900/800 + blue-500

**Archivos creados:**

1. **`frontend/index.html` (280 líneas)**
   - Estructura HTML5 semántica
   - CDNs cargados: Tailwind, DaisyUI, Plotly, MathJax, Google Fonts
   - Layout responsive 3 áreas:
     - Panel izquierdo: selector fórmula + inputs dinámicos + botón calcular
     - Área derecha: gráfico Plotly grande (min-height 500px)
     - Abajo: historial en cards horizontales con scroll
   - Header con logo y badge de conexión
   - Footer con info del stack
   - Toast notifications (DaisyUI)

2. **`frontend/js/api.js` (210 líneas)**
   - Funciones async/await para comunicación con backend
   - `obtenerFormulas()`: GET /api/formulas
   - `obtenerFormula(id)`: GET /api/formula/{id}
   - `calcularFormula(formulaId, valores)`: POST /api/calcular
   - `obtenerHistorial(limite)`: GET /api/historial
   - `verificarBackend()`: GET /health
   - Sistema de notificaciones toast (success, error, info, warning)
   - Indicador de estado de conexión (punto verde/loading)
   - Manejo completo de errores con try/catch

3. **`frontend/js/graficos.js` (190 líneas)**
   - Configuración Plotly tema oscuro
   - `renderizarGrafico(datosCalculo, formula)`: Gráfico principal
   - `actualizarGrafico(datosCalculo)`: Con animación suave
   - `limpiarGrafico()`: Resetear y mostrar placeholder
   - `renderizarMiniaturaGrafico(id, datos)`: Para historial
   - Layout oscuro:
     - Fondo slate-800 (#1e293b)
     - Grilla slate-700 (#334155)
     - Línea azul suave (spline, smoothing 1.3)
     - Hover tooltips customizados
     - Botones de herramientas (zoom, pan, descarga PNG)

4. **`frontend/js/app.js` (280 líneas)**
   - Lógica principal y controlador de eventos
   - `cargarFormulas()`: Poblar selector al iniciar
   - `cargarFormulaSeleccionada()`: Mostrar LaTeX + inputs dinámicos
   - `generarInputsDinamicos(formula)`: Crear inputs según variables
   - `realizarCalculo()`: Validar, llamar API, renderizar gráfico
   - `cargarHistorial()`: Mostrar últimos 5 cálculos con miniaturas
   - `cargarCalculoDeHistorial(id)`: Click en historial → cargar valores
   - Event listeners: selector, botón calcular, botón refrescar
   - Estado global: formulasDisponibles, formulaActual
   - Verificación de backend al iniciar

5. **`frontend/css/styles.css` (270 líneas)**
   - Animaciones: fadeIn, scaleIn, pulse, shake
   - Transiciones suaves en cards (hover: translateY(-4px))
   - Efecto glow en botón principal
   - Ripple effect en botones al click
   - Scrollbar personalizado para historial
   - Input error con animación shake
   - Focus states accesibles (outline blue)
   - Responsive: ajustes para móvil
   - Pulse-glow en indicador de conexión
   - Smooth scroll global

**Características implementadas:**

✅ **Responsive Design:**
- Desktop: 2 columnas (1/3 controles, 2/3 gráfico)
- Móvil: 1 columna apilada
- Historial: scroll horizontal en móvil

✅ **Interactividad:**
- Selector de fórmula → carga LaTeX + inputs
- Inputs dinámicos prellenados con valores BD
- Botón calcular con loading state
- Gráfico con animación de entrada
- Click en historial → cargar cálculo
- Hover en cards → efecto elevación

✅ **Validaciones:**
- Verificar backend al iniciar
- Validar inputs numéricos antes de calcular
- Shake animation en inputs inválidos
- Toasts informativos (éxito/error)

✅ **Estética:**
- Tema oscuro elegante (slate-900, blue-500)
- Tipografía Inter (Google Fonts)
- Iconos SVG inline (sin dependencias extras)
- Sombras y bordes sutiles
- Animaciones suaves (cubic-bezier)
- Glow effects en elementos interactivos

**Pruebas pendientes:**
- Iniciar backend: `uvicorn backend.main:app --reload`
- Servir frontend: `cd frontend && python -m http.server 3000`
- Abrir: http://localhost:3000

**Logro importante:**
✅ **FASE 3 COMPLETA** - Frontend funcional y elegante

**Próximo paso:**
- Fase 4: Integración y pruebas completas

---

## 2025-12-29 - Tarea 2.3 completada: Endpoint GET /api/historial

**Qué se hizo:**
- Añadido endpoint GET `/api/historial` en `backend/routes/calculos.py`
- Implementado JOIN automático entre tablas `calculos` y `formulas`
- Añadido parámetro query opcional `limite` (por defecto 20)
- Ordenamiento descendente por `created_at` (más recientes primero)
- Actualizado comentario de cabecera del archivo

**Código añadido:**
```python
@router.get("/historial")
def obtener_historial(limite: int = 20):
    response = supabase.table("calculos") \
        .select("*, formulas(*)") \
        .order("created_at", desc=True) \
        .limit(limite) \
        .execute()

    return {"data": response.data, "error": None}
```

**Características técnicas:**
- **JOIN automático:** `.select("*, formulas(*)")` trae todos los campos de calculos + todos los campos de formulas
- **Ordenamiento:** `.order("created_at", desc=True)` devuelve más recientes primero
- **Límite personalizable:** `/api/historial?limite=5` permite al usuario controlar cantidad
- **1 sola consulta:** Eficiente, no hace N+1 queries
- **Objeto anidado:** La respuesta tiene `formulas` anidado en cada cálculo

**Validaciones exitosas:**
- ✅ Endpoint GET /api/historial responde correctamente
- ✅ Devuelve array de cálculos ordenados DESC por created_at
- ✅ JOIN funciona: cada registro tiene objeto `formulas` anidado completo
- ✅ Parámetro query `limite` funciona (probado con limite=1)
- ✅ Formato estándar: `{"data": [...], "error": null}`
- ✅ Sin errores - Funcionó a la primera

**Pruebas realizadas:**
1. **Sin parámetros:** Devolvió 2 registros (todos), ordenados correctamente
2. **Con limite=1:** Devolvió solo el más reciente (id=2)

**Estructura de respuesta:**
```json
{
  "data": [
    {
      "id": 2,
      "formula_id": 1,
      "valores_entrada": {"v": 5, "x0": 0, ...},
      "resultado": {"t": [...], "x": [...]},
      "created_at": "2025-12-29T18:16:31.796161+00:00",
      "formulas": {
        "id": 1,
        "nombre": "MRU - Movimiento Rectilíneo Uniforme",
        "categoria": "fisica",
        "formula_latex": "x = x_0 + v \\cdot t",
        ...
      }
    }
  ],
  "error": null
}
```

**Archivos modificados:**
- `backend/routes/calculos.py` - Añadido endpoint GET /historial (70 líneas)
- `docs/aprendizaje/08_endpoint_historial.md` - Documentación educativa completa

**Conceptos documentados:**
- JOIN entre tablas (relaciones)
- Sintaxis de JOIN en Supabase: `.select("*, formulas(*)")`
- ORDER BY y DESC (ordenamiento descendente)
- LIMIT (limitar resultados)
- Query parameters en FastAPI (parámetro opcional con valor por defecto)
- Objetos anidados en respuesta JSON
- Eficiencia de 1 query vs N+1 queries

**Logro importante:**
✅ **FASE 2 COMPLETA** - Lógica de cálculo 100%

Backend completo para la fórmula MRU:
- ✅ GET /health → Verificar servidor
- ✅ GET /api/formulas → Listar fórmulas disponibles
- ✅ GET /api/formula/{id} → Obtener fórmula específica
- ✅ POST /api/calcular → Calcular, guardar y devolver resultado
- ✅ GET /api/historial → Ver cálculos anteriores

**Próximo paso:**
- Fase 3: Frontend básico (HTML/JS/CSS)
- Tarea 3.1: Estructura HTML base

---

## 2025-12-29 - Tarea 2.2 completada: Endpoint POST /api/calcular

**Qué se hizo:**
- Creado archivo `backend/routes/calculos.py` con router de cálculos
- Implementado endpoint POST `/api/calcular` que recibe fórmula_id + valores
- Añadido modelo Pydantic `DatosCalculo` para validación de datos
- Integrado con `calcular_mru()` de calculadora.py
- Guardado de resultados en tabla `calculos` de Supabase
- Registrado router en `backend/main.py`

**Flujo completo implementado:**
1. Frontend/usuario envía POST con `{formula_id: 1, valores: {x0, v, t_min, t_max}}`
2. Pydantic valida los datos automáticamente
3. Endpoint consulta tabla `formulas` en Supabase para obtener info de la fórmula
4. Identifica tipo de fórmula (MRU) por el nombre
5. Llama a `calcular_mru()` con los valores del usuario
6. Guarda resultado en tabla `calculos` (historial)
7. Devuelve puntos calculados + info de la fórmula + calculo_id

**Errores encontrados y solucionados (aprendizaje importante):**

❌ **Error #1 - Campo 'tipo' no existe:**
- Código asumía `formula["tipo"] == "MRU"`
- Pero tabla `formulas` no tiene campo `tipo`
- **Solución:** Cambiar a `"MRU" in formula["nombre"]`
- **Lección:** Siempre verificar estructura real de la BD antes de asumir

❌ **Error #2 - Columna 'valores' no existe:**
- Código usaba `"valores": datos.valores`
- Pero columna en Supabase se llama `valores_entrada`
- **Solución:** Cambiar a `"valores_entrada": datos.valores`
- **Lección:** Nombres de columnas deben coincidir exactamente (case-sensitive)
- **Diagnóstico:** Insert de prueba reveló columnas: `['id', 'formula_id', 'valores_entrada', 'resultado', 'created_at']`

**Validaciones exitosas:**
- ✅ Endpoint POST /api/calcular responde correctamente
- ✅ Pydantic valida tipos de datos (rechaza si formula_id no es int)
- ✅ Validación de valores requeridos (x0, v, t_min, t_max)
- ✅ Cálculo matemático correcto: x = x₀ + v·t
- ✅ 100 puntos generados para graficar
- ✅ Resultado guardado en BD con calculo_id
- ✅ Formato de respuesta estándar: `{"data": {...}, "error": null}`
- ✅ Primer punto: t=0, x=0 ✓
- ✅ Último punto: t=10, x=50 (con v=5, x₀=0) ✓

**Archivos creados/modificados:**
- `backend/routes/calculos.py` - Nuevo router con endpoint POST (146 líneas)
- `backend/main.py` - Añadido import y registro de calculos_router
- `docs/aprendizaje/07_endpoint_calcular.md` - Documentación educativa completa con errores documentados

**Conceptos documentados:**
- POST vs GET (enviar datos vs pedir datos)
- Pydantic y BaseModel (validación automática de datos)
- Request Body (cuerpo de petición JSON)
- Estructura de tabla `calculos` en Supabase
- Flujo completo: API → BD consulta → cálculo → BD guardado → respuesta
- Type hints con `Dict[str, Any]`
- Manejo de errores con try/except

**Próximo paso:**
- Tarea 2.3: Endpoint GET /api/historial para consultar cálculos anteriores
- Esto completará la Fase 2 del proyecto

---

## 2025-12-29 - Tarea 2.1 completada: Función de cálculo para MRU

**Qué se hizo:**
- Instalado NumPy 2.0.2 en el entorno virtual
- Creado archivo `backend/services/calculadora.py` con lógica de cálculo matemático
- Implementada función `calcular_mru(x0, v, t_min, t_max, puntos)`
- Añadidas 5 pruebas completas en bloque `if __name__ == "__main__"`
- Actualizado `requirements.txt` con numpy

**Código de la función:**
- Usa `np.linspace()` para generar puntos igualmente espaciados
- Aplica operación vectorizada: `x = x0 + v * t`
- Convierte NumPy arrays a listas Python con `.tolist()`
- Devuelve diccionario: `{"t": [...], "x": [...]}`
- Type hints completos y docstring detallado

**Pruebas realizadas:**
- ✅ Prueba 1: Caso básico (v=5, x₀=0, 5 puntos)
- ✅ Prueba 2: Posición inicial (v=3, x₀=10, 6 puntos)
- ✅ Prueba 3: Velocidad negativa (v=-2, retroceso)
- ✅ Prueba 4: Reposo (v=0, posición constante)
- ✅ Prueba 5: 100 puntos (típico para gráfico)

**Validaciones matemáticas:**
- ✅ Fórmula MRU correcta: x = x₀ + v·t
- ✅ Velocidades positivas: movimiento hacia adelante
- ✅ Velocidades negativas: movimiento hacia atrás (retroceso)
- ✅ Velocidad cero: posición constante (reposo)
- ✅ Valores numéricos precisos en todos los casos

**Validaciones técnicas:**
- ✅ np.linspace() genera puntos igualmente espaciados
- ✅ Operaciones vectorizadas funcionan correctamente
- ✅ .tolist() convierte a listas Python (JSON-serializables)
- ✅ Estructura de retorno correcta (diccionario con "t" y "x")
- ✅ Type hints aplicados correctamente
- ✅ Parámetro opcional `puntos=100` funciona

**Archivos creados/modificados:**
- `backend/services/calculadora.py` - Función de cálculo MRU (117 líneas)
- `requirements.txt` - Añadido numpy==2.0.2
- `docs/aprendizaje/06_logica_calculo.md` - Documentación educativa completa

**Conceptos documentados:**
- NumPy y cálculo numérico
- np.linspace() para valores igualmente espaciados
- Operaciones vectorizadas
- Conversión NumPy arrays a listas (.tolist())
- Type hints para retorno de función
- Separación de lógica matemática de HTTP/BD

**Dependencia instalada:**
- numpy==2.0.2 (6.9 MB, compilado para macOS x86_64)

**Logro importante:**
- Primera función de lógica matemática del proyecto
- Base para todas las demás fórmulas (MRUV, caída libre, etc.)
- Listo para ser usado por el endpoint POST /api/calcular

**Estado del proyecto:**
- Fase 0 (Preparación): 1/1 ✅ Completada
- Fase 1 (Conexión Python ↔ Supabase): 4/4 ✅ Completada
- Fase 2 (Lógica de cálculo): 1/3 tareas completadas (33%)
- Siguiente tarea: 2.2 - Endpoint POST /api/calcular

---

## 2025-12-29 - Tarea 1.4 completada: Endpoint para obtener fórmula por ID - ✅ FASE 1 COMPLETA

**Qué se hizo:**
- Modificado archivo `backend/routes/formulas.py`
- Añadido endpoint GET `/api/formula/{formula_id}` con parámetro de ruta
- Implementado filtrado en Supabase con `.eq("id", formula_id)`
- Añadido manejo del caso "fórmula no encontrada"
- Implementada respuesta con objeto único (no lista) usando `response.data[0]`

**Código del endpoint:**
- Parámetro de ruta: `{formula_id}` tipado como `int`
- Consulta: `supabase.table("formulas").select("*").eq("id", formula_id).execute()`
- Validación: `if not response.data` para detectar fórmula inexistente
- Respuesta éxito: `{"data": response.data[0], "error": None}`
- Respuesta no encontrada: `{"data": None, "error": "Fórmula no encontrada"}`

**Pruebas realizadas:**
- ✅ Probado con ID existente (1): Devolvió fórmula MRU correctamente
- ✅ Probado con ID inexistente (999): Devolvió error "Fórmula no encontrada"
- ✅ Formato de respuesta: objeto `{...}` no lista `[...]` ✓
- ✅ Manejo de errores consistente con formato estándar

**Datos de prueba:**
- ID 1 → Fórmula MRU completa con todos los campos
- ID 999 → Error controlado, sin excepción
- Respuesta contiene: id, nombre, formula_latex, categoria, variables, etc.

**Validaciones confirmadas:**
- ✅ Parámetros de ruta funcionan en FastAPI
- ✅ Validación automática de tipo (int)
- ✅ Filtrado `.eq()` en Supabase funciona
- ✅ Detección de lista vacía con `if not response.data`
- ✅ Extracción de primer elemento con `[0]`
- ✅ Manejo de excepciones con try/except
- ✅ Formato estándar mantenido en todos los casos

**Archivos creados/modificados:**
- `backend/routes/formulas.py` - Añadidas ~73 líneas (nuevo endpoint)
- `docs/aprendizaje/05_endpoint_formula_id.md` - Documentación educativa completa

**Conceptos documentados:**
- Parámetros de ruta (path parameters) en FastAPI
- Filtrado con `.eq()` en Supabase
- Manejo del caso "no encontrado"
- Diferencia entre lista y objeto único
- Truthiness en Python para validar datos
- Comparación entre obtener todos vs uno específico

**🎉 HITO IMPORTANTE: FASE 1 COMPLETADA**

La Fase 1 "Conexión Python ↔ Supabase" está 100% completa:
1. ✅ Cliente de Supabase funcionando
2. ✅ Servidor FastAPI operativo
3. ✅ Endpoint para listar todas las fórmulas
4. ✅ Endpoint para obtener una fórmula por ID

**Arquitectura backend operativa:**
- Backend puede comunicarse con Supabase
- Endpoints organizados con APIRouter
- Formato de respuesta estándar implementado
- Manejo de errores consistente
- Base sólida para la siguiente fase

**Estado del proyecto:**
- Fase 0 (Preparación): 1/1 ✅ Completada
- Fase 1 (Conexión Python ↔ Supabase): 4/4 ✅ Completada
- Siguiente: Fase 2 - Lógica de cálculo (Tarea 2.1: Función de cálculo para MRU)

---

## 2025-12-29 - Tarea 1.3 completada: Endpoint para listar fórmulas

**Qué se hizo:**
- Creado directorio `backend/routes/` para organizar endpoints
- Creado archivo `backend/routes/__init__.py` (ya existía con comentario básico)
- Creado archivo `backend/routes/formulas.py` con APIRouter
- Modificado `backend/main.py` para incluir el router de fórmulas
- Implementado endpoint GET `/api/formulas` que consulta Supabase

**Código del router:**
- APIRouter con prefix="/api" y tags=["formulas"]
- Endpoint `@router.get("/formulas")` que:
  - Importa el cliente Supabase
  - Consulta `supabase.table("formulas").select("*").execute()`
  - Devuelve formato estándar: `{"data": [...], "error": None}`
  - Maneja errores con try/except

**Pruebas realizadas:**
- ✅ Servidor arrancado con uvicorn
- ✅ Endpoint `/api/formulas` respondió correctamente
- ✅ Recuperada fórmula MRU de la base de datos
- ✅ Respuesta en formato JSON con estructura estándar
- ✅ Endpoint `/health` sigue funcionando (no se rompió nada)

**Datos recuperados:**
- ID: 1
- Nombre: "MRU - Movimiento Rectilíneo Uniforme"
- Categoría: "fisica"
- Fórmula LaTeX: "x = x_0 + v \\cdot t"
- Variable de rango: "t" (0 a 10)
- Variables de usuario: v=5, x0=0

**Validaciones confirmadas:**
- ✅ APIRouter funciona correctamente con prefijo
- ✅ app.include_router() integra routers exitosamente
- ✅ Importación del cliente Supabase funciona
- ✅ Consulta a Supabase ejecuta sin errores
- ✅ Formato de respuesta estándar implementado
- ✅ Manejo de errores con try/except
- ✅ Organización modular del código (separación de concerns)

**Archivos creados/modificados:**
- `backend/routes/formulas.py` - Router con endpoint de fórmulas (72 líneas)
- `backend/main.py` - Modificado para incluir router (añadidas 3 líneas)
- `docs/aprendizaje/04_endpoint_formulas.md` - Documentación educativa completa

**Conceptos documentados:**
- APIRouter y organización de rutas
- Prefijos en routers
- Tags para documentación automática
- Formato estándar de respuestas
- Importaciones absolutas vs relativas
- Manejo de errores consistente

**Logro importante:**
- **Primera integración completa FastAPI + Supabase**
- Demuestra que toda la arquitectura backend funciona end-to-end
- Establece el patrón para futuros endpoints

**Estado del proyecto:**
- Fase 1 (Conexión Python ↔ Supabase): 3/4 tareas completadas (75%)
- Siguiente tarea: 1.4 - Endpoint `/api/formula/{id}` para obtener una fórmula específica

---

## 2025-12-29 - Tarea 1.2 completada: Endpoint Health Check con FastAPI

**Qué se hizo:**
- Creado archivo `backend/main.py` con la aplicación FastAPI
- Configurada aplicación FastAPI con metadatos:
  - title: "API Fórmulas Matemáticas"
  - description: "Backend para visualización de fórmulas matemáticas y físicas"
  - version: "0.1.0"
- Implementado endpoint GET `/health` para verificar estado del servidor
- Probado servidor con uvicorn en modo desarrollo (--reload)

**Pruebas realizadas:**
- ✅ Servidor uvicorn arrancado en http://127.0.0.1:8000
- ✅ Endpoint /health respondió correctamente
- ✅ Respuesta JSON válida: `{"status":"ok","message":"Servidor funcionando correctamente"}`
- ✅ Hot-reload activado para desarrollo

**Validaciones confirmadas:**
- ✅ FastAPI instalado y funcionando correctamente
- ✅ Uvicorn puede ejecutar la aplicación
- ✅ Decorador @app.get funciona correctamente
- ✅ Conversión automática de dict Python a JSON
- ✅ Servidor HTTP respondiendo peticiones
- ✅ Documentación automática disponible en /docs (no probada pero disponible)

**Archivos creados:**
- `backend/main.py` - Aplicación FastAPI con endpoint health (48 líneas)
- `docs/aprendizaje/03_primer_endpoint.md` - Documentación educativa completa

**Conceptos documentados:**
- Qué es FastAPI y por qué lo usamos
- Decoradores en Python (@app.get)
- Métodos HTTP (GET, POST, PUT, DELETE)
- Qué es Uvicorn y cómo funciona
- localhost:8000 (concepto de puerto)
- JSON y conversión automática

**Estado del proyecto:**
- Fase 1 (Conexión Python ↔ Supabase): 2/4 tareas completadas
- Siguiente tarea: 1.3 - Crear endpoint `/api/formulas` que devuelva todas las fórmulas usando el cliente de Supabase

---

## 2025-12-29 - Tarea 1.1 completada: Cliente de Supabase

**Qué se hizo:**
- Creada estructura de directorios: `backend/` y `backend/services/`
- Creados archivos `__init__.py` para indicar módulos de Python
- Creado archivo `backend/services/supabase_client.py` con:
  - Importación de librerías necesarias (os, dotenv, supabase)
  - Lectura de credenciales desde archivo `.env`
  - Validación de que las credenciales existen
  - Creación del cliente de Supabase (patrón singleton)
  - Función `test_conexion()` para verificar conectividad
  - Bloque `if __name__ == "__main__"` para pruebas directas

**Pruebas realizadas:**
- ✅ Ejecución del script: `python backend/services/supabase_client.py`
- ✅ Conexión exitosa con Supabase
- ✅ Recuperación correcta de datos de la tabla `formulas`
- ✅ Fórmula MRU encontrada: ID 1, nombre "MRU - Movimiento Rectilíneo Uniforme", categoría "fisica"

**Observaciones técnicas:**
- Warning de urllib3/OpenSSL apareció pero no afecta la funcionalidad
- El warning se debe a que urllib3 v2 recomienda OpenSSL 1.1.1+ pero macOS usa LibreSSL 2.8.3
- Es común en macOS y no requiere corrección

**Validaciones confirmadas:**
- ✅ Archivo `.env` se lee correctamente
- ✅ Credenciales SUPABASE_URL y SUPABASE_KEY son válidas
- ✅ Tabla `formulas` existe y es accesible
- ✅ Permisos de lectura funcionan correctamente
- ✅ Patrón singleton implementado correctamente (un solo cliente reutilizable)

**Archivos creados:**
- `backend/__init__.py` - Módulo backend
- `backend/services/__init__.py` - Submódulo services
- `backend/services/supabase_client.py` - Cliente de Supabase (67 líneas)
- `docs/aprendizaje/02_conexion_supabase.md` - Documentación educativa completa

**Conceptos documentados:**
- Variables de entorno y python-dotenv
- Clientes de API
- Patrón Singleton
- Type hints en Python
- Uso de `if __name__ == "__main__"`

**Estado del proyecto:**
- Fase 1 (Conexión Python ↔ Supabase): 1/4 tareas completadas
- Siguiente tarea: 1.2 - Crear endpoint de prueba (health check) con FastAPI

---

## 2025-12-29 - Tarea 0.1 completada: Entorno virtual e instalación de dependencias

**Qué se hizo:**
- Creado entorno virtual en `venv/` usando `python3 -m venv venv`
- Instaladas las 4 librerías principales del proyecto:
  - `fastapi` 0.128.0 - Framework para crear la API REST
  - `uvicorn` 0.39.0 - Servidor ASGI para ejecutar FastAPI
  - `supabase` 2.27.0 - Cliente de Python para Supabase
  - `python-dotenv` 1.2.1 - Lector de variables de entorno desde `.env`
- Generado archivo `requirements.txt` con 58 dependencias totales
- Documentación completa creada en `docs/aprendizaje/01_entorno_virtual.md`

**Versiones instaladas:**
Las versiones obtenidas son más recientes que las especificadas en el plan original:
- fastapi: 0.128.0 (vs 0.115.6 esperado)
- uvicorn: 0.39.0 (vs 0.34.0 esperado)
- supabase: 2.27.0 (vs 2.11.1 esperado)
- python-dotenv: 1.2.1 (vs 1.0.1 esperado)

Esto es positivo porque incluye mejoras y correcciones de seguridad recientes.

**Verificación:**
- ✅ Python del venv en ruta correcta: `/Volumes/Akitio01/Claude_MCP/formulas-web/venv/bin/python3`
- ✅ Todas las librerías instaladas sin errores
- ✅ requirements.txt generado correctamente
- ✅ Documentación socrática completada

**Archivos creados:**
- `venv/` - Entorno virtual de Python
- `requirements.txt` - Lista de dependencias con versiones exactas
- `docs/aprendizaje/01_entorno_virtual.md` - Documentación educativa completa

**Estado del proyecto:**
- Fase 0 (Preparación): 1/1 tareas completadas ✅
- Siguiente tarea: 1.1 - Crear el cliente de Supabase

---

## 2024-12-29 - Regla anti-sobreescritura + documentar diffs

**Qué se añadió:**
- Regla crítica en CLAUDE.md: NUNCA sobreescribir documentación
- Sección 5.1 en plantilla: Historial de cambios de código con diffs
- Recordatorios en PLAN.md y plantilla

**Por qué:**
- Juan aprende del PROCESO, no solo del resultado
- Los errores y cambios de código son material de aprendizaje
- Ver el diff (rojo/verde) ayuda a entender qué cambió y por qué

**Archivos modificados:**
- `CLAUDE.md` - Regla al principio + sección de diffs
- `PLAN.md` - Recordatorio en cabecera
- `docs/aprendizaje/00_PLANTILLA.md` - Sección 5.1 + regla de oro

---

## 2024-12-29 - Sistema de documentación socrática creado

**Qué se hizo:**
- Creado `CLAUDE.md` completo con instrucciones para Claude Code
- Creado `PLAN.md` con todas las tareas detalladas
- Creada carpeta `docs/aprendizaje/` con:
  - `00_PLANTILLA.md` - Plantilla para documentar cada tarea
  - `INDICE.md` - Índice de todos los documentos de aprendizaje

**Por qué:**
- Juan quiere entender CÓMO se construye el proyecto, no solo que funcione
- Cada paso se documenta con método socrático (qué, por qué, cómo)
- Los errores también se documentan como oportunidades de aprendizaje

**Estructura de documentación:**
```
docs/aprendizaje/
├── 00_PLANTILLA.md      ← Cómo documentar cada tarea
├── INDICE.md            ← Lista de todos los documentos
├── 01_entorno_virtual.md    ← (pendiente)
├── 02_conexion_supabase.md  ← (pendiente)
└── ...
```

---

## 2024-12-29 - Supabase configurado y tablas creadas

**Qué se hizo:**
- Proyecto Supabase creado (región EU West - Ireland)
- Credenciales obtenidas y configuradas en `.env`
- Tabla `formulas` creada con estructura completa
- Tabla `calculos` creada con referencia a `formulas`
- Fórmula de prueba insertada (MRU)

**Verificación:**
- SQL ejecutado: `Success. No rows returned` (correcto)
- Table Editor muestra ambas tablas
- Fórmula MRU visible en `formulas`

**Credenciales configuradas:**
- URL: `https://qfeatlcnilhqjcacniih.supabase.co`
- API Key: Secret key (service_role) en `.env`

**Archivos modificados:**
- `.env` - Credenciales reales
- `_local_info/tutorial_supabase.md` - Tutorial actualizado

---

## 2024-12-29 - Inicio del proyecto

**Archivos creados:**
- Estructura de carpetas completa
- CLAUDE.md (instrucciones para Claude Code)
- .env.example (plantilla de credenciales)
- .gitignore (protege secretos)
- docs/MAESTRO.md (documentación completa)
- Este archivo de bitácora

**Decisiones tomadas:**
- Stack: FastAPI + Supabase + Vanilla JS + Plotly
- Arquitectura de tres capas (frontend → backend → BD)
- 15 fórmulas iniciales definidas
- Metodología: Opus diseña, Claude Code implementa

---

<!-- Claude Code: añade nuevas entradas ARRIBA de esta línea -->
