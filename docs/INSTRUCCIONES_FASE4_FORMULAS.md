# INSTRUCCIONES FASE 4: Integración y 15 Fórmulas

> **Objetivo:** Corregir bugs detectados + añadir las 15 fórmulas completas
> **Prioridad:** Primero bugs, luego fórmulas

---

## PARTE 1: BUGS A CORREGIR

### Bug 1: LaTeX no renderiza correctamente

**Problema:** La fórmula muestra `vcdott` en lugar del símbolo `·`

**Causa probable:** MathJax no está procesando el LaTeX o el delimitador es incorrecto.

**Solución:** Verificar en `index.html`:
1. Que MathJax esté cargado correctamente
2. Que los delimitadores sean `\(...\)` para inline o `$$...$$` para bloque
3. Que después de insertar LaTeX dinámicamente se llame a `MathJax.typeset()`

**Código a verificar/añadir en app.js:**
```javascript
// Después de insertar fórmula LaTeX en el DOM:
if (window.MathJax) {
    MathJax.typeset();
}
```

**Verificar configuración MathJax en index.html:**
```html
<script>
MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['$$', '$$']]
  }
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
```

---

## PARTE 2: LAS 15 FÓRMULAS

### Estructura de cada fórmula en Supabase

La tabla `formulas` tiene estas columnas:
- `id` (auto)
- `nombre` (texto)
- `categoria` (texto: "fisica", "matematicas", "curvas_exoticas")
- `formula_latex` (texto)
- `descripcion` (texto)
- `variables_usuario` (JSONB) - qué inputs mostrar
- `variable_rango` (texto) - variable independiente (t, x, theta...)
- `rango_min` (float)
- `rango_max` (float)

---

### SQL para insertar las 14 fórmulas nuevas

Ejecutar en Supabase SQL Editor:

```sql
-- =============================================
-- FÍSICA (5 fórmulas) - Ya existe MRU (id=1)
-- =============================================

-- 2. MRUA - Movimiento Rectilíneo Uniformemente Acelerado
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'MRUA - Movimiento Uniformemente Acelerado',
  'fisica',
  'x = x_0 + v_0 \cdot t + \frac{1}{2} a \cdot t^2',
  'Posición en movimiento con aceleración constante. Genera una parábola.',
  '{"x0": {"nombre": "Posición inicial (x₀)", "default": 0, "unidad": "m"}, "v0": {"nombre": "Velocidad inicial (v₀)", "default": 5, "unidad": "m/s"}, "a": {"nombre": "Aceleración (a)", "default": 2, "unidad": "m/s²"}}',
  't',
  0,
  10
);

-- 3. Caída Libre
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Caída Libre',
  'fisica',
  'y = y_0 - \frac{1}{2} g \cdot t^2',
  'Altura de un objeto en caída libre desde una altura inicial.',
  '{"y0": {"nombre": "Altura inicial (y₀)", "default": 100, "unidad": "m"}, "g": {"nombre": "Gravedad (g)", "default": 9.8, "unidad": "m/s²"}}',
  't',
  0,
  5
);

-- 4. Tiro Parabólico (componente Y)
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Tiro Parabólico',
  'fisica',
  'y = v_0 \cdot \sin(\theta) \cdot t - \frac{1}{2} g \cdot t^2',
  'Trayectoria vertical de un proyectil lanzado con ángulo.',
  '{"v0": {"nombre": "Velocidad inicial (v₀)", "default": 20, "unidad": "m/s"}, "theta": {"nombre": "Ángulo (θ)", "default": 45, "unidad": "grados"}, "g": {"nombre": "Gravedad (g)", "default": 9.8, "unidad": "m/s²"}}',
  't',
  0,
  5
);

-- 5. Movimiento Armónico Simple
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Movimiento Armónico Simple',
  'fisica',
  'x = A \cdot \cos(\omega \cdot t + \phi)',
  'Oscilación periódica como la de un péndulo o resorte.',
  '{"A": {"nombre": "Amplitud (A)", "default": 5, "unidad": "m"}, "omega": {"nombre": "Frecuencia angular (ω)", "default": 2, "unidad": "rad/s"}, "phi": {"nombre": "Fase inicial (φ)", "default": 0, "unidad": "rad"}}',
  't',
  0,
  10
);

-- 6. Onda Sinusoidal
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Onda Sinusoidal',
  'fisica',
  'y = A \cdot \sin(k \cdot x - \omega \cdot t)',
  'Propagación de una onda en el espacio. Visualización en t=0.',
  '{"A": {"nombre": "Amplitud (A)", "default": 3, "unidad": "m"}, "k": {"nombre": "Número de onda (k)", "default": 1, "unidad": "rad/m"}, "omega": {"nombre": "Frecuencia angular (ω)", "default": 0, "unidad": "rad/s"}}',
  'x',
  0,
  20
);

-- =============================================
-- MATEMÁTICAS (5 fórmulas)
-- =============================================

-- 7. Parábola
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Parábola',
  'matematicas',
  'y = a \cdot x^2 + b \cdot x + c',
  'Función cuadrática. La forma depende del signo de a.',
  '{"a": {"nombre": "Coeficiente a", "default": 1, "unidad": ""}, "b": {"nombre": "Coeficiente b", "default": 0, "unidad": ""}, "c": {"nombre": "Coeficiente c", "default": 0, "unidad": ""}}',
  'x',
  -10,
  10
);

-- 8. Función Exponencial
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Función Exponencial',
  'matematicas',
  'y = a \cdot e^{b \cdot x}',
  'Crecimiento o decrecimiento exponencial.',
  '{"a": {"nombre": "Coeficiente a", "default": 1, "unidad": ""}, "b": {"nombre": "Exponente b", "default": 0.5, "unidad": ""}}',
  'x',
  -2,
  5
);

-- 9. Función Logarítmica
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Función Logarítmica',
  'matematicas',
  'y = a \cdot \ln(x) + b',
  'Logaritmo natural. Definido solo para x > 0.',
  '{"a": {"nombre": "Coeficiente a", "default": 1, "unidad": ""}, "b": {"nombre": "Desplazamiento b", "default": 0, "unidad": ""}}',
  'x',
  0.1,
  10
);

-- 10. Función Seno
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Función Seno',
  'matematicas',
  'y = A \cdot \sin(B \cdot x + C)',
  'Función trigonométrica seno con amplitud, frecuencia y fase.',
  '{"A": {"nombre": "Amplitud", "default": 1, "unidad": ""}, "B": {"nombre": "Frecuencia", "default": 1, "unidad": ""}, "C": {"nombre": "Fase", "default": 0, "unidad": ""}}',
  'x',
  0,
  12.57
);

-- 11. Circunferencia (paramétrica)
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Circunferencia',
  'matematicas',
  'x = r \cdot \cos(\theta), \quad y = r \cdot \sin(\theta)',
  'Circunferencia de radio r centrada en el origen. Curva paramétrica.',
  '{"r": {"nombre": "Radio", "default": 5, "unidad": ""}}',
  'theta',
  0,
  6.28
);

-- =============================================
-- CURVAS EXÓTICAS (4 fórmulas)
-- =============================================

-- 12. Espiral de Arquímedes
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Espiral de Arquímedes',
  'curvas_exoticas',
  'r = a + b \cdot \theta',
  'Espiral donde la distancia al centro crece linealmente con el ángulo.',
  '{"a": {"nombre": "Radio inicial", "default": 0, "unidad": ""}, "b": {"nombre": "Velocidad de expansión", "default": 0.5, "unidad": ""}}',
  'theta',
  0,
  31.4
);

-- 13. Espiral Logarítmica
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Espiral Logarítmica',
  'curvas_exoticas',
  'r = a \cdot e^{b \cdot \theta}',
  'Espiral que aparece en la naturaleza: conchas, galaxias, huracanes.',
  '{"a": {"nombre": "Factor de escala", "default": 0.5, "unidad": ""}, "b": {"nombre": "Factor de crecimiento", "default": 0.15, "unidad": ""}}',
  'theta',
  0,
  25
);

-- 14. Cardioide
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Cardioide',
  'curvas_exoticas',
  'r = a \cdot (1 + \cos(\theta))',
  'Curva con forma de corazón. Aparece en óptica y acústica.',
  '{"a": {"nombre": "Tamaño", "default": 3, "unidad": ""}}',
  'theta',
  0,
  6.28
);

-- 15. Lemniscata de Bernoulli
INSERT INTO formulas (nombre, categoria, formula_latex, descripcion, variables_usuario, variable_rango, rango_min, rango_max)
VALUES (
  'Lemniscata de Bernoulli',
  'curvas_exoticas',
  'r^2 = a^2 \cdot \cos(2\theta)',
  'Curva en forma de infinito (∞). Solo existe donde cos(2θ) ≥ 0.',
  '{"a": {"nombre": "Tamaño", "default": 5, "unidad": ""}}',
  'theta',
  0,
  6.28
);
```

---

## PARTE 3: FUNCIONES DE CÁLCULO

### Archivo: `backend/services/calculadora.py`

Añadir estas funciones (mantener la existente `calcular_mru`):

```python
import numpy as np

# Ya existe: calcular_mru

def calcular_mrua(x0: float, v0: float, a: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """MRUA: x = x0 + v0*t + 0.5*a*t²"""
    t = np.linspace(t_min, t_max, puntos)
    x = x0 + v0 * t + 0.5 * a * t**2
    return {"t": t.tolist(), "x": x.tolist()}

def calcular_caida_libre(y0: float, g: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """Caída libre: y = y0 - 0.5*g*t²"""
    t = np.linspace(t_min, t_max, puntos)
    y = y0 - 0.5 * g * t**2
    y = np.maximum(y, 0)  # No puede bajar de 0
    return {"t": t.tolist(), "y": y.tolist()}

def calcular_tiro_parabolico(v0: float, theta: float, g: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """Tiro parabólico: calcula x e y"""
    theta_rad = np.radians(theta)
    t = np.linspace(t_min, t_max, puntos)
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    y = np.maximum(y, 0)
    return {"t": t.tolist(), "x": x.tolist(), "y": y.tolist()}

def calcular_armonico_simple(A: float, omega: float, phi: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """MAS: x = A*cos(ω*t + φ)"""
    t = np.linspace(t_min, t_max, puntos)
    x = A * np.cos(omega * t + phi)
    return {"t": t.tolist(), "x": x.tolist()}

def calcular_onda_sinusoidal(A: float, k: float, omega: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Onda: y = A*sin(k*x - ω*t) en t=0"""
    x = np.linspace(x_min, x_max, puntos)
    y = A * np.sin(k * x)  # t=0
    return {"x": x.tolist(), "y": y.tolist()}

def calcular_parabola(a: float, b: float, c: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Parábola: y = ax² + bx + c"""
    x = np.linspace(x_min, x_max, puntos)
    y = a * x**2 + b * x + c
    return {"x": x.tolist(), "y": y.tolist()}

def calcular_exponencial(a: float, b: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Exponencial: y = a*e^(bx)"""
    x = np.linspace(x_min, x_max, puntos)
    y = a * np.exp(b * x)
    return {"x": x.tolist(), "y": y.tolist()}

def calcular_logaritmica(a: float, b: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Logarítmica: y = a*ln(x) + b"""
    x = np.linspace(max(x_min, 0.001), x_max, puntos)  # Evitar ln(0)
    y = a * np.log(x) + b
    return {"x": x.tolist(), "y": y.tolist()}

def calcular_seno(A: float, B: float, C: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Seno: y = A*sin(Bx + C)"""
    x = np.linspace(x_min, x_max, puntos)
    y = A * np.sin(B * x + C)
    return {"x": x.tolist(), "y": y.tolist()}

def calcular_circunferencia(r: float, theta_min: float, theta_max: float, puntos: int = 100) -> dict:
    """Circunferencia paramétrica"""
    theta = np.linspace(theta_min, theta_max, puntos)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}

def calcular_espiral_arquimedes(a: float, b: float, theta_min: float, theta_max: float, puntos: int = 200) -> dict:
    """Espiral de Arquímedes: r = a + b*θ"""
    theta = np.linspace(theta_min, theta_max, puntos)
    r = a + b * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}

def calcular_espiral_logaritmica(a: float, b: float, theta_min: float, theta_max: float, puntos: int = 200) -> dict:
    """Espiral logarítmica: r = a*e^(b*θ)"""
    theta = np.linspace(theta_min, theta_max, puntos)
    r = a * np.exp(b * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}

def calcular_cardioide(a: float, theta_min: float, theta_max: float, puntos: int = 200) -> dict:
    """Cardioide: r = a*(1 + cos(θ))"""
    theta = np.linspace(theta_min, theta_max, puntos)
    r = a * (1 + np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}

def calcular_lemniscata(a: float, theta_min: float, theta_max: float, puntos: int = 200) -> dict:
    """Lemniscata: r² = a²*cos(2θ)"""
    theta = np.linspace(theta_min, theta_max, puntos)
    cos_2theta = np.cos(2 * theta)
    # Solo donde cos(2θ) >= 0
    valid = cos_2theta >= 0
    r = np.where(valid, a * np.sqrt(np.abs(cos_2theta)), np.nan)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    # También el lado negativo
    r_neg = np.where(valid, -a * np.sqrt(np.abs(cos_2theta)), np.nan)
    x_neg = r_neg * np.cos(theta)
    y_neg = r_neg * np.sin(theta)
    # Combinar ambos lados
    x_full = np.concatenate([x, x_neg])
    y_full = np.concatenate([y, y_neg])
    return {"x": x_full.tolist(), "y": y_full.tolist()}
```

---

## PARTE 4: ACTUALIZAR ENDPOINT DE CÁLCULO

### Archivo: `backend/routes/calculos.py`

El endpoint debe reconocer cada fórmula por su nombre e invocar la función correcta.

**Lógica a implementar:**

```python
# Mapeo nombre -> función
if "MRU" in formula["nombre"] and "Uniformemente" not in formula["nombre"]:
    resultado = calcular_mru(...)
elif "MRUA" in formula["nombre"] or "Uniformemente Acelerado" in formula["nombre"]:
    resultado = calcular_mrua(...)
elif "Caída Libre" in formula["nombre"]:
    resultado = calcular_caida_libre(...)
elif "Tiro Parabólico" in formula["nombre"]:
    resultado = calcular_tiro_parabolico(...)
elif "Armónico Simple" in formula["nombre"]:
    resultado = calcular_armonico_simple(...)
elif "Onda Sinusoidal" in formula["nombre"]:
    resultado = calcular_onda_sinusoidal(...)
elif "Parábola" in formula["nombre"]:
    resultado = calcular_parabola(...)
elif "Exponencial" in formula["nombre"]:
    resultado = calcular_exponencial(...)
elif "Logarítmica" in formula["nombre"]:
    resultado = calcular_logaritmica(...)
elif "Seno" in formula["nombre"]:
    resultado = calcular_seno(...)
elif "Circunferencia" in formula["nombre"]:
    resultado = calcular_circunferencia(...)
elif "Arquímedes" in formula["nombre"]:
    resultado = calcular_espiral_arquimedes(...)
elif "Logarítmica" in formula["nombre"] and "Espiral" in formula["nombre"]:
    resultado = calcular_espiral_logaritmica(...)
elif "Cardioide" in formula["nombre"]:
    resultado = calcular_cardioide(...)
elif "Lemniscata" in formula["nombre"]:
    resultado = calcular_lemniscata(...)
```

**Importante:** Importar todas las funciones nuevas de calculadora.py

---

## PARTE 5: ACTUALIZAR FRONTEND PARA CURVAS PARAMÉTRICAS

### Archivo: `frontend/js/graficos.js`

Las curvas paramétricas (circunferencia, espirales, cardioide, lemniscata) devuelven `x` e `y` en lugar de `t` y `x`.

**El gráfico debe detectar qué ejes usar:**

```javascript
function dibujarGrafico(resultado, nombreFormula) {
    let xData, yData, xLabel, yLabel;
    
    // Detectar tipo de datos
    if (resultado.t !== undefined) {
        // Fórmulas con tiempo
        xData = resultado.t;
        xLabel = 't (tiempo)';
        yData = resultado.x || resultado.y;
        yLabel = resultado.x ? 'x (posición)' : 'y (altura)';
    } else if (resultado.theta !== undefined) {
        // Curvas paramétricas polares
        xData = resultado.x;
        yData = resultado.y;
        xLabel = 'x';
        yLabel = 'y';
    } else {
        // Funciones y = f(x)
        xData = resultado.x;
        yData = resultado.y;
        xLabel = 'x';
        yLabel = 'y';
    }
    
    // Plotly trace
    const trace = {
        x: xData,
        y: yData,
        type: 'scatter',
        mode: 'lines',
        // ... resto de config
    };
}
```

---

## COMANDO PARA CLAUDE CODE

```
Lee estos archivos en /Volumes/Akitio01/Claude_MCP/formulas-web:
1. CLAUDE.md
2. PLAN.md
3. docs/INSTRUCCIONES_FASE4_FORMULAS.md (ESTE ARCHIVO)

Ejecuta la FASE 4 en este orden:

PASO 1 - CORREGIR BUG LATEX:
- Verificar que MathJax está bien configurado en index.html
- Asegurar que app.js llama a MathJax.typeset() después de insertar LaTeX
- Probar que la fórmula se renderiza correctamente

PASO 2 - INSERTAR FÓRMULAS EN SUPABASE:
- Usar el cliente Python para insertar las 14 fórmulas nuevas
- O proporcionar el SQL para que Juan lo ejecute manualmente
- Verificar que las 15 fórmulas están en la BD

PASO 3 - AÑADIR FUNCIONES DE CÁLCULO:
- Añadir las 14 funciones nuevas a calculadora.py
- Mantener calcular_mru() existente
- Probar cada función individualmente

PASO 4 - ACTUALIZAR ENDPOINT:
- Modificar calculos.py para reconocer cada fórmula
- Importar todas las funciones de calculadora.py
- Manejar los diferentes formatos de respuesta (t/x vs x/y vs theta/x/y)

PASO 5 - ACTUALIZAR FRONTEND:
- Modificar graficos.js para detectar tipo de datos
- Manejar curvas paramétricas (x,y) vs funciones temporales (t,x)
- Asegurar que el aspect ratio es correcto para circunferencias/espirales

PASO 6 - PROBAR TODO:
- Probar al menos 3 fórmulas de cada categoría
- Verificar que el gráfico se ve correcto
- Verificar que el historial funciona

Documenta en docs/aprendizaje/13_integracion.md y docs/aprendizaje/14_todas_formulas.md
Actualiza PLAN.md y bitacora.md
```

---

## VERIFICACIÓN FINAL

Después de completar, probar:

1. **MRU** → Línea recta ✓
2. **Parábola** → Curva en U ✓
3. **Seno** → Onda ✓
4. **Circunferencia** → Círculo cerrado ✓
5. **Espiral logarítmica** → Espiral que crece ✓
6. **Cardioide** → Forma de corazón ✓

---

*Documento preparado: 29 diciembre 2024*
*Para: Claude Code - Fase 4*
