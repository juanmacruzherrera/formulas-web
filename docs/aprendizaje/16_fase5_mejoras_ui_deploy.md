# 16. Fase 5: Mejoras de UI y Preparación para Deploy

**Fecha:** 7 de enero de 2026
**Fase del Proyecto:** Fase 5 - Correcciones finales y preparación para producción

---

## 1. ¿Qué vamos a hacer?

Mejorar la experiencia de usuario de la aplicación y prepararla para deploy en producción. Incluye:

1. **Inputs dinámicos**: Variables que cambian según la fórmula seleccionada
2. **Sliders para rangos**: Controles más intuitivos para ajustar rangos de visualización
3. **Layout invertido**: Gráfica grande a la izquierda, controles a la derecha
4. **Historial colapsable**: Mover historial al panel lateral para ahorrar espacio
5. **Configuración para deploy**: Archivos necesarios para subir a producción

---

## 2. ¿Por qué lo necesitamos?

### Problemas identificados en Fase 4:

- **Variables hardcodeadas**: Todos los inputs mostraban "Posición inicial", "Velocidad" aunque la fórmula fuera diferente (ej: parábola necesita a, b, c)
- **Inputs numéricos para rangos**: Poco intuitivo para ajustar t_min/t_max
- **Layout inverso**: La gráfica (lo más importante) estaba a la derecha y pequeña
- **Historial ocupaba mucho espacio**: Sección completa al fondo de la página
- **No preparado para deploy**: Sin Procfile, sin detección de entorno

### Beneficios de las mejoras:

✅ **UX mejorada**: Controles adaptativos según cada fórmula
✅ **Más intuitivo**: Sliders para rangos, gráfica prominente
✅ **Mejor uso del espacio**: Historial lateral colapsable
✅ **Listo para producción**: Configuración automática de URLs

---

## 3. ¿Cómo encaja en el proyecto?

```
ANTES (Fase 4)                    DESPUÉS (Fase 5)
─────────────────                 ──────────────────
┌─────────────┐                   ┌─────────────────┐
│  CONTROLES  │ ← pequeño         │   GRÁFICA 📊    │ ← grande
│   (fixed)   │                   │   (principal)   │
└─────────────┘                   └─────────────────┘

┌─────────────┐                   ┌─────────────────┐
│  GRÁFICA 📊 │ ← grande          │   CONTROLES     │ ← fijo
│  (pequeña)  │                   │   + historial ▼ │ ← colapsable
└─────────────┘                   └─────────────────┘

┌──────────────────────────┐      (Historial integrado
│  HISTORIAL (horizontal)  │       en panel derecho)
└──────────────────────────┘
```

**Impacto en los archivos:**
- `frontend/js/app.js` → Generación dinámica de inputs + sliders
- `frontend/index.html` → Layout invertido + historial lateral
- `frontend/js/api.js` → Detección de entorno (localhost vs producción)
- `Procfile` (nuevo) → Configuración para Render
- `.gitignore` → Ya correcto (verificado)

---

## 4. Conceptos a entender

### 4.1 Inputs dinámicos con diccionario de mapeo

**Problema:** Cada fórmula tiene variables diferentes (x0, v para MRU; a, b, c para parábola)

**Solución:** Leer `variables_usuario` de Supabase y generar inputs dinámicamente

```javascript
// ANTES: hardcodeado
const inputsConfig = [
    { nombre: 'x0', label: 'Posición inicial' },
    { nombre: 'v', label: 'Velocidad' }
];

// DESPUÉS: dinámico
const variables = formula.variables_usuario; // {'x0': 0, 'v': 5}
Object.entries(variables).forEach(([nombreVar, valorDefecto]) => {
    // Generar input para cada variable
});
```

**Diccionario de etiquetas:** Como las claves son técnicas ("x0", "v"), creamos un diccionario para mostrar nombres amigables:

```javascript
const ETIQUETAS_VARIABLES = {
    'x0': { label: 'Posición inicial x₀', placeholder: 'metros' },
    'v': { label: 'Velocidad', placeholder: 'm/s' },
    'a': { label: 'Aceleración a', placeholder: 'm/s²' }
    // ... más variables
};
```

### 4.2 Sliders HTML5 con valor visible

En lugar de inputs numéricos para rangos, usamos `<input type="range">`:

```html
<!-- Estructura del slider -->
<div>
    <label>t mínimo <span id="display_t_min">0</span></label>
    <input type="range" id="input_t_min" min="-10" max="100" value="0" step="0.1">
</div>
```

**Event listener para actualizar display:**
```javascript
slider.addEventListener('input', (e) => {
    valorDisplay.textContent = e.target.value;
});
```

### 4.3 DaisyUI Collapse (componente colapsable)

Para el historial lateral:

```html
<div class="collapse collapse-arrow">
    <input type="checkbox" id="toggleHistorial" />
    <div class="collapse-title">Historial</div>
    <div class="collapse-content">
        <!-- contenido aquí -->
    </div>
</div>
```

- `collapse-arrow`: Muestra flecha para indicar que es colapsable
- `checkbox`: Controla si está expandido o colapsado
- `collapse-title`: Parte visible siempre
- `collapse-content`: Se muestra/oculta al hacer clic

### 4.4 Detección de entorno en JavaScript

```javascript
const API_BASE = window.location.hostname === 'localhost'
    ? 'http://localhost:8000'        // desarrollo
    : 'https://backend.onrender.com'; // producción
```

- `window.location.hostname`: Devuelve el dominio actual
- En desarrollo: "localhost" → usa puerto 8000 local
- En producción: "mi-app.pages.dev" → usa URL del backend desplegado

### 4.5 Procfile para Render

Render (y otras plataformas) usan `Procfile` para saber cómo ejecutar la app:

```
web: uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

- `web:` → Tipo de proceso (servicio web)
- `uvicorn backend.main:app` → Comando para iniciar FastAPI
- `--host 0.0.0.0` → Escuchar en todas las interfaces
- `--port $PORT` → Usar puerto asignado por Render (variable de entorno)

---

## 5. Implementación paso a paso

### PASO 2: Variables dinámicas

**Archivo modificado:** `frontend/js/app.js`

**Qué cambió:**

```diff
- // Inputs hardcodeados
- const inputsConfig = [
-     { nombre: 'x0', label: 'Posición inicial (x₀)' },
-     { nombre: 'v', label: 'Velocidad (v)' }
- ];

+ // Diccionario de etiquetas amigables
+ const ETIQUETAS_VARIABLES = {
+     'x0': { label: 'Posición inicial x₀', placeholder: 'metros' },
+     'v': { label: 'Velocidad', placeholder: 'm/s' },
+     'a': { label: 'Aceleración a', placeholder: 'm/s²' },
+     // ... más variables
+ };
+
+ // Generar inputs dinámicamente
+ Object.entries(variables).forEach(([nombreVar, valorDefecto]) => {
+     const config = ETIQUETAS_VARIABLES[nombreVar] || { label: nombreVar };
+     // Crear input basado en la variable
+ });
```

**Por qué:**
- Cada fórmula tiene variables diferentes
- Leer desde `formula.variables_usuario` asegura compatibilidad con todas las fórmulas
- Fallback a `nombreVar` si no hay etiqueta definida (para futuras variables)

**Resultado:**
- MRU muestra: x₀, v
- Parábola muestra: a, b, c
- Cardioide muestra: a (según sus variables específicas)

---

### PASO 3: Sliders para rangos

**Archivo modificado:** `frontend/js/app.js`

**Qué cambió:**

```diff
- // Input numérico para rango
- <input type="number" name="t_min" value="0">

+ // Slider con display del valor
+ <div class="flex justify-between">
+     <label>t mínimo</label>
+     <span id="display_t_min" class="text-blue-400">0</span>
+ </div>
+ <input type="range" name="t_min" min="-10" max="100" step="0.1" value="0">
```

**Por qué:**
- Los sliders son más intuitivos para ajustar rangos
- Permiten ver visualmente el rango completo
- Actualizan el gráfico de forma más fluida

**Configuración dinámica:**
```javascript
const rangoMin = {
    nombre: `${formula.variable_rango}_min`, // ej: "t_min"
    valor: formula.rango_min || 0,
    min: formula.rango_min - 10,  // rango del slider
    max: formula.rango_max
};
```

**Resultado:**
- Interfaz más visual e interactiva
- Valores se actualizan en tiempo real al mover el slider

---

### PASO 4: Layout invertido

**Archivo modificado:** `frontend/index.html`

**Qué cambió:**

```diff
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
-     <!-- PANEL IZQUIERDO: Controles -->
-     <div class="lg:col-span-1">...</div>
-
      <!-- ÁREA DE VISUALIZACIÓN: Gráfico -->
      <div class="lg:col-span-2">...</div>
+
+     <!-- PANEL DERECHO: Controles -->
+     <div class="lg:col-span-1">...</div>
  </div>
```

**Por qué:**
- La gráfica es el contenido principal → debe ser prominente
- Usuarios primero ven el resultado visual, luego ajustan parámetros
- Estándar en aplicaciones de visualización (ej: Desmos, GeoGebra)

**Resultado:**
- Gráfica ocupa 2/3 del ancho (más grande, a la izquierda)
- Controles ocupan 1/3 (compacto, a la derecha)

---

### PASO 5: Historial lateral colapsable

**Archivos modificados:**
- `frontend/index.html` → Estructura HTML
- `frontend/js/app.js` → Generación de cards

**Qué cambió en HTML:**

```diff
- <!-- HISTORIAL DE CÁLCULOS (sección separada abajo) -->
- <div class="card bg-slate-800">
-     <div id="historialContainer" class="overflow-x-auto">
-         <div class="flex space-x-4">...</div>
-     </div>
- </div>

+ <!-- HISTORIAL (dentro del panel derecho) -->
+ <div class="collapse collapse-arrow bg-slate-700">
+     <input type="checkbox" id="toggleHistorial" />
+     <div class="collapse-title">Historial</div>
+     <div class="collapse-content">
+         <div id="historialContainer" class="space-y-2 max-h-96 overflow-y-auto">
+             <!-- Cards verticalmente -->
+         </div>
+     </div>
+ </div>
```

**Qué cambió en JavaScript:**

```diff
- container.innerHTML = `<div class="flex space-x-4">${cardsHTML}</div>`;
+ container.innerHTML = cardsHTML; // Sin wrapper horizontal

  // Cards más compactas para layout vertical
- <div class="card min-w-[280px]">
+ <div class="card"> <!-- Sin min-width, ocupa ancho del panel -->
-     <div class="h-24">miniatura</div>
+     <div class="h-16">miniatura</div> <!-- Más pequeña -->
```

**Por qué:**
- Ahorra espacio vertical en la página
- Historial siempre accesible sin scroll largo
- Panel derecho agrupa toda la interacción (controles + historial)

**Resultado:**
- Historial colapsado por defecto (no distrae)
- Click en "Historial" lo expande
- Cards verticales adaptadas al espacio estrecho

---

### PASO 6: Preparación para deploy

#### 6.1 Verificar .gitignore

**Archivo:** `.gitignore`

**Verificación:** ✅ Ya incluye:
```
.env
venv/
__pycache__/
```

**Por qué es importante:**
- `.env` → Secretos (credenciales de Supabase)
- `venv/` → Dependencias (se instalan en producción)
- `__pycache__/` → Archivos compilados de Python

---

#### 6.2 Crear Procfile

**Archivo creado:** `Procfile` (raíz del proyecto)

**Contenido:**
```
web: uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

**Por qué:**
- Render necesita saber cómo iniciar la aplicación
- `$PORT` es variable de entorno asignada por Render
- `--host 0.0.0.0` permite conexiones externas

---

#### 6.3 Detección de entorno en api.js

**Archivo modificado:** `frontend/js/api.js`

**Qué cambió:**

```diff
- const API_BASE = 'http://localhost:8000';

+ const API_BASE = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
+     ? 'http://localhost:8000'
+     : 'https://TU-BACKEND.onrender.com';
```

**Por qué:**
- En desarrollo: frontend llama a backend local (localhost:8000)
- En producción: frontend llama a backend desplegado en Render
- Cambio automático sin modificar código

**⚠️ NOTA para Juan:**
Después de desplegar el backend en Render, cambiar `TU-BACKEND.onrender.com` por la URL real.

---

## 6. Verificación

### Test manual realizado:

1. ✅ **Inputs dinámicos funcionan:**
   - Seleccionar MRU → muestra x₀, v
   - Seleccionar Parábola → muestra a, b, c
   - Seleccionar Cardioide → muestra a

2. ✅ **Sliders funcionan:**
   - Mover slider → valor actualizado en tiempo real
   - Valores correctos enviados al backend

3. ✅ **Layout invertido:**
   - Gráfica ocupa 2/3 a la izquierda
   - Controles ocupan 1/3 a la derecha

4. ✅ **Historial colapsable:**
   - Por defecto colapsado
   - Click expande/contrae
   - Cards verticales en panel estrecho

5. ✅ **Archivos de deploy:**
   - `.gitignore` correcto
   - `Procfile` creado
   - `api.js` con detección de entorno

---

## 7. Problemas encontrados y soluciones

### Problema 1: Variables de Supabase como string

**Error:** `AttributeError: 'str' object has no attribute 'keys'`

**Causa:** Supabase devuelve `variables_usuario` como string JSON en algunos casos

**Solución:**
```python
vars_dict = f['variables_usuario'] if isinstance(f['variables_usuario'], dict) else json.loads(f['variables_usuario'])
```

### Problema 2: Miniaturas de historial muy grandes

**Causa:** Las miniaturas ocupaban h-24 (96px) en panel estrecho

**Solución:** Reducir a h-16 (64px) para historial lateral

---

## 8. ¿Qué aprendimos?

### Conceptos técnicos:

1. **Renderizado dinámico de formularios:**
   - Generar inputs basándose en datos de la BD
   - Diccionarios de mapeo para labels amigables
   - Fallbacks para variables no definidas

2. **HTML5 range inputs:**
   - Más intuitivos que inputs numéricos para rangos
   - Sincronización con displays de valor
   - Configuración dinámica de min/max

3. **Diseño responsive:**
   - Grid de Tailwind CSS (lg:col-span-X)
   - Componentes colapsables de DaisyUI
   - Adaptación de contenido a espacios estrechos

4. **Preparación para deploy:**
   - Detección automática de entorno
   - Procfile para plataformas cloud
   - Gestión de secretos (.gitignore)

### Buenas prácticas:

- ✅ **Verificar estructura de datos antes de escribir código**
  - Ejecutar query de Supabase para ver estructura real
  - Evita errores de "campo no existe"

- ✅ **Diseño mobile-first**
  - Panel derecho se adapta bien a pantallas pequeñas
  - Historial colapsable ahorra espacio

- ✅ **Comentarios claros en código de producción**
  - `// ⚠️ IMPORTANTE: Cambiar URL después del deploy`
  - Ayuda al futuro mantenimiento

---

## 9. Próximos pasos

### Para Juan (pasos manuales):

**⚠️ PASO PREVIO - Git y GitHub:**
El proyecto NO está en GitHub todavía. **DEBES HACER ESTO PRIMERO:**

👉 **Guía completa:** `docs/GUIA_GIT_GITHUB.md`

Resumen:
1. Inicializar Git: `git init`
2. Primer commit: `git add . && git commit -m "Fase 5 completa"`
3. Crear repositorio en GitHub (público)
4. Conectar: `git remote add origin URL`
5. Subir: `git push -u origin main`
6. **Verificar que `.env` NO se subió** (debe estar en .gitignore)

**PASO 1:** Configurar RLS en Supabase
```sql
ALTER TABLE formulas ENABLE ROW LEVEL SECURITY;
CREATE POLICY "formulas_select_public" ON formulas FOR SELECT USING (true);
-- etc.
```

**PASO 7-8:** Deploy (requiere GitHub)
1. Backend → Render
2. Frontend → Cloudflare Pages
3. Actualizar URL en `api.js`

**Orden completo:**
```
0. Subir a GitHub (GUIA_GIT_GITHUB.md) ← OBLIGATORIO
1. RLS en Supabase
2-6. Pasos completados por Claude Code ✅
7. Deploy backend en Render
8. Deploy frontend en Cloudflare
```

### Documentación generada:

- ✅ Este archivo (`16_fase5_mejoras_ui_deploy.md`)
- ✅ `docs/bitacora.md` actualizada
- ✅ `docs/GUIA_JUAN_PASOS_MANUALES.md` actualizada
- ✅ `docs/GUIA_GIT_GITHUB.md` creada (nueva)

---

## 10. Archivos modificados

| Archivo | Cambios | Líneas |
|---------|---------|--------|
| `frontend/js/app.js` | Inputs dinámicos + sliders + historial vertical | ~100 |
| `frontend/index.html` | Layout invertido + historial colapsable | ~30 |
| `frontend/js/api.js` | Detección de entorno | 4 |
| `Procfile` | **Creado** | 1 |
| `.gitignore` | Verificado (sin cambios) | 0 |

**Total:** ~135 líneas modificadas/añadidas

---

**Conclusión:**

La Fase 5 completa las mejoras de experiencia de usuario y prepara la aplicación para producción. Los cambios son principalmente de interfaz (frontend) con configuración para deploy. El proyecto está listo para que Juan ejecute los pasos manuales de seguridad (RLS) y deploy.

**Estado del proyecto:** 🟢 Listo para deploy tras configurar RLS
